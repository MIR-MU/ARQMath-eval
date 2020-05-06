# -*- coding:utf-8 -*-

from glob import glob
import os.path
import re

from pytrec_eval import parse_run

from .common import get_ndcg, get_random_normalized_ndcg
from .configuration import TASKS, USER_README_HEAD


if __name__ == '__main__':
    for task in TASKS:
        for user in glob(os.path.join(task, '*', '')):
            user = os.path.normpath(user)
            user_name = os.path.basename(user)
            user_results = []
            for result in glob(os.path.join(user, '*.tsv')):
                result_name = re.sub('_', ', ', os.path.basename(result)[:-4])
                with open(result, 'rt') as f:
                    parsed_result = parse_run(f)
                params = (parsed_result, task, 'validation')
                ndcg = get_ndcg(*params)
                random_normalized_ndcg = get_random_normalized_ndcg(*params)
                user_results.append((ndcg, random_normalized_ndcg, result_name))
            with open(os.path.join(user, 'README.md'), 'wt') as f:
                f.write(USER_README_HEAD % user_name)
                f.write('\n')
                for ndcg, random_normalized_ndcg, result_name in sorted(user_results, reverse=True):
                    f.write('| %.4f | %.4f | %s |\n' % (ndcg, random_normalized_ndcg, result_name))
