# -*- coding:utf-8 -*-

from copy import deepcopy

import numpy as np

from .configuration import EVALUATORS, PARSED_RELEVANCE_JUDGEMENTS


def remove_nonjudged_topics_and_documents(parsed_run, task, subset):
    parsed_relevance_judgements = PARSED_RELEVANCE_JUDGEMENTS[subset][task]
    only_judged_parsed_run = deepcopy(parsed_run)
    for topic_name, results in parsed_run.items():
        if topic_name not in parsed_relevance_judgements:
            del only_judged_parsed_run[topic_name]
        else:
            judgements = parsed_relevance_judgements[topic_name]
            for document_name in results.keys():
                if document_name not in judgements:
                    del only_judged_parsed_run[topic_name][document_name]
    return only_judged_parsed_run


def get_topics(task='task1-votes', subset=None):
    topics = set()
    subsets = [
        PARSED_RELEVANCE_JUDGEMENTS['train'],
        PARSED_RELEVANCE_JUDGEMENTS['test'],
    ] if subset is None else [PARSED_RELEVANCE_JUDGEMENTS[subset]]
    for subset in subsets:
        for topic in subset[task].keys():
            topics.add(topic)
    return topics


def get_judged_documents(task='task1-votes', subset=None, topic=None):
    judged_documents = set()
    subsets = [
        PARSED_RELEVANCE_JUDGEMENTS['train'],
        PARSED_RELEVANCE_JUDGEMENTS['test'],
    ] if subset is None else [PARSED_RELEVANCE_JUDGEMENTS[subset]]
    for subset in subsets:
        topics = subset[task].values() if topic is None else [subset[task][topic]]
        for documents in topics:
            judged_documents.update(documents)
    return judged_documents


def ndcg(parsed_run, task='task1-votes', subset='train-validation'):
    evaluator = EVALUATORS[subset][task]
    only_judged_parsed_run = remove_nonjudged_topics_and_documents(parsed_run, task, subset)
    evaluation = evaluator.evaluate(only_judged_parsed_run)
    ndcg = np.mean([measures['ndcg'] for topic, measures in evaluation.items()])
    return ndcg
