# -*- coding:utf-8 -*-

from copy import deepcopy

import numpy as np

from .configuration import EVALUATORS, PARSED_RELEVANCE_JUDGEMENTS


def ndcg(parsed_run, task='task1', subset='train'):
    only_judged_parsed_run = deepcopy(parsed_run)
    parsed_relevance_judgements = PARSED_RELEVANCE_JUDGEMENTS[subset][task]
    for topic_name, results in parsed_run.items():
        if topic_name not in parsed_relevance_judgements:
            del only_judged_parsed_run[topic_name]
        else:
            judgements = parsed_relevance_judgements[topic_name]
            for document_name in results.keys():
                if document_name not in judgements:
                    del only_judged_parsed_run[topic_name][document_name]
    evaluator = EVALUATORS[subset][task]
    evaluation = evaluator.evaluate(only_judged_parsed_run)
    ndcg = np.mean([
        measures['ndcg']
        for topic, measures
        in evaluation.items()
    ])
    return ndcg
