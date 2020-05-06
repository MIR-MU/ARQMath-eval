# -*- coding:utf-8 -*-

from glob import glob
import os.path
import re

from pytrec_eval import parse_run

from .common import get_ndcg, get_random_ndcg
from .configuration import TASKS, USER_README_HEAD


if __name__ == '__main__':
    for task in TASKS:
        random_ndcg = get_random_ndcg(task, 'validation')
        for user in glob(os.path.join(task, '*', '')):
            user = os.path.normpath(user)
            user_name = os.path.basename(user)
            user_results = []
            for result in glob(os.path.join(user, '*.tsv')):
                result_name = re.sub('_', ', ', os.path.basename(result)[:-4])
                with open(result, 'rt') as f:
                    parsed_result = parse_run(f)
                ndcg = get_ndcg(parsed_result, task, 'validation')
                user_results.append((ndcg, result_name))
            with open(os.path.join(user, 'README.md'), 'wt') as f:
                f.write(USER_README_HEAD % (user_name, random_ndcg))
                f.write('\n')
                for ndcg, result_name in sorted(user_results, reverse=True):
                    f.write('| %.4f | %s |\n' % (ndcg, result_name))
