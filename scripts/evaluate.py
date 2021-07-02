# -*- coding:utf-8 -*-

from glob import glob
from itertools import repeat
from multiprocessing import Pool
import os.path
import re
import sys
from typing import Tuple

from pytrec_eval import parse_run
from tqdm import tqdm

from .common import get_ndcg, get_random_ndcg
from .configuration import TASKS, USER_README_HEAD, TASK_README_HEAD


def evaluate_worker(args) -> Tuple[str, float]:
    task, result_filename = args
    result_name = re.sub('_', ', ', os.path.basename(result_filename)[:-4])
    with open(result_filename, 'rt') as f:
        parsed_result = parse_run(f)
    ndcg = get_ndcg(parsed_result, task, 'validation')
    return (result_name, ndcg)


def produce_leaderboards() -> None:
    for task in TASKS:
        if not os.path.exists(task):
            continue
        random_ndcg = get_random_ndcg(task, 'validation')
        users = glob(os.path.join(task, '*', ''))
        task_results = [(random_ndcg, 'random', 'xrando42')]
        for user in users:
            user = os.path.normpath(user)
            user_name = os.path.basename(user)
            user_results = [(random_ndcg, 'random')]
            results = glob(os.path.join(user, '*.tsv'))
            if results:
                results = tqdm(results, desc='Evaluating {} results'.format(user))
                results = zip(repeat(task), results)
                with Pool(None) as pool:
                    for result_name, ndcg in pool.map(evaluate_worker, results):
                        user_results.append((ndcg, result_name))
                    with open(os.path.join(user, 'README.md'), 'wt') as f_readme:
                        f_readme.write(USER_README_HEAD % user_name)
                        f_readme.write('\n')
                        task_results.append((*max(user_results), user_name))
                        for ndcg, result_name in sorted(user_results, reverse=True):
                            if result_name == 'random':
                                f_readme.write('| *%.4f* | *%s* |\n' % (ndcg, result_name))
                            else:
                                f_readme.write('| %.4f | %s |\n' % (ndcg, result_name))
                        try:
                            with open(os.path.join(user, 'LEGEND.md'), 'rt') as f_legend:
                                f_readme.write('\n## Legend\n\n')
                                f_readme.write(f_legend.read())
                        except IOError:
                            pass
        with open(os.path.join(task, 'README.md'), 'wt') as f_readme:
            f_readme.write(TASK_README_HEAD % task)
            f_readme.write('\n')
            for ndcg, result_name, user_name in sorted(task_results, reverse=True):
                if result_name == 'random':
                    f_readme.write('| *%.4f* | *%s* | *%s* |\n' % (ndcg, result_name, user_name))
                else:
                    f_readme.write('|  %.4f  |  %s  |  %s  |\n' % (ndcg, result_name, user_name))


def evaluate_run(filename, subset, year, confidence=95.0) -> Tuple[float, float]:
    with open(filename, 'rt') as f:
        lines = [line.strip().split() for line in f]
    first_line = lines[0]
    n = len(first_line)
    if n == 5:
        task = 'task1-{}'.format(year)
    elif n == 6:
        task = 'task2-{}'.format(year)
    else:
        raise ValueError(
            'Expected lines as 5-tuples (Query_Id, Post_Id, Rank, Score, Run_Number) for task 1, '
            'or 6-tuples (Query_Id, Formula_Id, Post_Id, Rank, Score, Run_Number) for task 2, '
            'received %d-tuples: %s' % (n, first_line)
        )
    parsed_result = dict()
    rank_offset = 0
    for line in lines:
        topic_id, result_id, *_, rank, __, ___ = line
        # support indexing of ranks starting from 0
        if int(rank) == 0:
            rank_offset = 1
        if topic_id not in parsed_result:
            parsed_result[topic_id] = dict()
        parsed_result[topic_id][result_id] = 1.0 / (int(rank) + rank_offset)
    ndcg, interval = get_ndcg(parsed_result, task, subset, confidence=confidence)
    print('%.3f, %g%% CI: [%.3f; %.3f]' % (ndcg, confidence, *interval))
    return (ndcg, interval)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        produce_leaderboards()
    elif len(sys.argv) > 1 and len(sys.argv) <= 4:
        if len(sys.argv) == 2:
            evaluate_run(sys.argv[1], 'all', 2020)
        if len(sys.argv) == 3:
            evaluate_run(sys.argv[1], sys.argv[2], 2020)
        if len(sys.argv) == 4:
            evaluate_run(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    else:
        raise ValueError("Usage: {} [TSV_FILE [SUBSET [YEAR]]]".format(sys.argv[0]))
