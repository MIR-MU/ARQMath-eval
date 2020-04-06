# -*- coding:utf-8 -*-

import numpy as np

from .configuration import PARSED_RELEVANCE_JUDGEMENTS


def ndcg(parsed_run, task='task1', subset='test'):
    evaluator = PARSED_RELEVANCE_JUDGEMENTS[subset][task]
    evaluation = evaluator.evaluate(parsed_run)
    ndcg = np.mean([
        measures['ndcg']
        for topic, measures
        in evaluation.items()
    ])
    return ndcg
