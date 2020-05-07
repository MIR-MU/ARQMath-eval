# -*- coding:utf-8 -*-

from glob import glob
import os.path
import re

from pytrec_eval import parse_run
from tqdm import tqdm

from .common import get_ndcg, get_random_ndcg
from .configuration import TASKS, USER_README_HEAD


if __name__ == '__main__':
    for task in TASKS:
        random_ndcg = get_random_ndcg(task, 'validation')
        users = glob(os.path.join(task, '*', ''))
        for user in users:
            user = os.path.normpath(user)
            user_name = os.path.basename(user)
            user_results = [(random_ndcg, 'random')]
            results = glob(os.path.join(user, '*.tsv'))
            if results:
                for result in tqdm(results, desc='Evaluating {} systems'.format(user)):
                    result_name = re.sub('_', ', ', os.path.basename(result)[:-4])
                    with open(result, 'rt') as f:
                        parsed_result = parse_run(f)
                    ndcg = get_ndcg(parsed_result, task, 'validation')
                    user_results.append((ndcg, result_name))
                with open(os.path.join(user, 'README.md'), 'wt') as f:
                    f.write(USER_README_HEAD % user_name)
                    f.write('\n')
                    for ndcg, result_name in sorted(user_results, reverse=True):
                        if result_name == 'random':
                            f.write('| *%.4f* | *%s* |\n' % (ndcg, result_name))
                        else:
                            f.write('| %.4f | %s |\n' % (ndcg, result_name))
