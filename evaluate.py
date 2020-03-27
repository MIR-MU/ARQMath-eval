# -*- coding:utf-8 -*-

from glob import glob
import os.path
import re

import numpy as np
from pytrec_eval import RelevanceEvaluator, parse_qrel, parse_run


RELEVANCE_JUDGEMENTS = {
    'task1': 'qrel.V0.1.tsv',
    'ntcir-11-math-2-main': 'NTCIR11_Math-qrels.dat',
    'ntcir-12-mathir-arxiv-main': 'NTCIR12_Math-qrels_agg.dat',
}
TASK_README_HEAD = r'''
This table contains the best result for every user.

| nDCG | User | Result name |
|:-----|------|:------------|
'''.strip()
USER_README_HEAD = r'''
This table contains all results for user *%s* in descending order of task
performance.  Result names are based on the filenames of the results with
underscores (`_`) replaced with a comma and a space for improved readability.

| nDCG | Result name |
|------|:------------|
'''.strip()


if __name__ == '__main__':
    for task, relevance_judgements in RELEVANCE_JUDGEMENTS.items():
        with open(os.path.join(task, relevance_judgements), 'rt') as f:
            parsed_relevance_judgements = parse_qrel(f)
        evaluator = RelevanceEvaluator(parsed_relevance_judgements, {'ndcg'})
        task_results = []
        for user in glob(os.path.join(task, '*', '')):
            user = os.path.normpath(user)
            user_name = os.path.basename(user)
            user_results = []
            for result in glob(os.path.join(user, '*.tsv')):
                result_name = re.sub('_', ', ', os.path.basename(result)[:-4])
                with open(result, 'rt') as f:
                    parsed_result = parse_run(f)
                evaluation = evaluator.evaluate(parsed_result)
                ndcg = np.mean([
                    measures['ndcg']
                    for topic, measures
                    in evaluation.items()
                ])
                user_results.append((ndcg, result_name))
            best_ndcg, best_result_name = max(user_results)
            task_results.append((best_ndcg, user_name, best_result_name))
            with open(os.path.join(user, 'README.md'), 'wt') as f:
                f.write(USER_README_HEAD % user_name)
                f.write('\n')
                for ndgc, result_name in sorted(user_results, reverse=True):
                    f.write('| %.4f | %s |\n' % (ndcg, result_name))
        with open(os.path.join(task, 'README.md'), 'wt') as f:
            f.write(TASK_README_HEAD)
            f.write('\n')
            for ndgc, user_name, result_name in sorted(task_results, reverse=True):
                f.write('| %.4f | %s | %s |\n' % (ndcg, user_name, result_name))
