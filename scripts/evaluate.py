# -*- coding:utf-8 -*-

from glob import glob
from multiprocessing import Pool
import os.path
import re

from pytrec_eval import parse_run
from tqdm import tqdm

from .common import get_ndcg, get_random_ndcg
from .configuration import TASKS, USER_README_HEAD, TASK_README_HEAD


def evaluate_worker(result_filename):
    result_name = re.sub('_', ', ', os.path.basename(result_filename)[:-4])
    with open(result_filename, 'rt') as f:
        parsed_result = parse_run(f)
    ndcg = get_ndcg(parsed_result, task, 'validation')
    return (result_name, ndcg)


if __name__ == '__main__':
    for task in TASKS:
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
