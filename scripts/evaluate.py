# -*- coding:utf-8 -*-

from glob import glob
import os.path
import re

from pytrec_eval import parse_run

from .common import get_ndcg
from .configuration import TASKS, TASK_README_HEAD, USER_README_HEAD


if __name__ == '__main__':
    for task in TASKS:
        task_results = []
        for user in glob(os.path.join(task, '*', '')):
            user = os.path.normpath(user)
            user_name = os.path.basename(user)
            user_results = []
            for result in glob(os.path.join(user, '*.tsv')):
                result_name = re.sub('_', ', ', os.path.basename(result)[:-4])
                with open(result, 'rt') as f:
                    parsed_result = parse_run(f)
                user_results.append((get_ndcg(parsed_result, task, 'test'), result_name))
            best_ndcg, best_result_name = max(user_results)
            task_results.append((best_ndcg, user_name, best_result_name))
            with open(os.path.join(user, 'README.md'), 'wt') as f:
                f.write(USER_README_HEAD % user_name)
                f.write('\n')
                for ndcg, result_name in sorted(user_results, reverse=True):
                    f.write('| %.4f | %s |\n' % (ndcg, result_name))
        with open(os.path.join(task, 'README.md'), 'wt') as f:
            f.write(TASK_README_HEAD)
            f.write('\n')
            for ndcg, user_name, result_name in sorted(task_results, reverse=True):
                f.write('| %.4f | %s | %s |\n' % (ndcg, user_name, result_name))
