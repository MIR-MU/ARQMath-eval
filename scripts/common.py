# -*- coding:utf-8 -*-

from copy import deepcopy
from itertools import chain
from math import log2

import numpy as np

from .configuration import EVALUATORS, PARSED_RELEVANCE_JUDGEMENTS


def _remove_nonjudged_topics_and_documents(parsed_run, task, subset):
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


def _clip_topn(parsed_run, topn):
    clipped_parsed_run = {}
    for topic, documents in parsed_run.items():
        clipped_documents = sorted(documents.items(), key=lambda x: x[1], reverse=True)[:topn]
        clipped_parsed_run[topic] = dict(clipped_documents)
    return clipped_parsed_run


def get_topics(task, subset=None):
    """Returns the identifiers of topics for a subset of a task.

    Parameters
    ----------
    task : str
        A task.
    subset : str or None, optional
        A subset of the task. If None, topics for all subsets will be returned.
        Default is None.

    Returns
    -------
    topics : set of str
        The identifiers of topics for the subset of the task.

    """
    topics = set()
    subsets = PARSED_RELEVANCE_JUDGEMENTS.values() if subset is None else [PARSED_RELEVANCE_JUDGEMENTS[subset]]
    for subset in subsets:
        for topic in subset[task].keys():
            topics.add(topic)
    return topics


def get_judged_documents(task, subset=None, topic=None):
    """Returns the judged documents of a topic in a subset of a task.

    Parameters
    ----------
    task : str
        A task.
    subset : str or None, optional
        A subset of the task. If None, topics for all subsets will be
        considered.  Default is None.
    topic : str or None, optional
        A topic in the subset of the task. If None, judged documents for
        all topics will be returned. Default is None.

    Returns
    -------
    judged_documents : set of str
        The judged documents of a topic in the subset of the task.

    """
    judged_documents = set()
    subsets = PARSED_RELEVANCE_JUDGEMENTS.values() if subset is None else [PARSED_RELEVANCE_JUDGEMENTS[subset]]
    for subset in subsets:
        if topic is not None and topic not in subset[task]:
            continue
        topics = subset[task].values() if topic is None else [subset[task][topic]]
        for documents in topics:
            judged_documents.update(documents)
    return judged_documents


def get_ndcg(parsed_run, task, subset, topn=1000):
    """Returns the NDCG' of a system's run on a subset of a task.

    NDCG' is the same as NDCG (Normalized Discounted Cumulative Gain), but all
    non-judged documents in the run are disregarded, see
    https://www.cs.rit.edu/~dprl/ARQMath/, section Ranking metrics.

    Parameters
    ----------
    parsed_run : dict of (str, dict of (str, float))
        The run of an information retrieval system.
    task : str
        A task.
    subset : str
        A subset of the task.
    topn : int, optional
        The top N results, which will be considered in computing the NDCG.
        Default is 1000.

    Returns
    -------
    ndcg : float
        The NDCG' of the system's run on the subset of the task.

    """
    evaluator = EVALUATORS[subset][task]
    parsed_run = _remove_nonjudged_topics_and_documents(parsed_run, task, subset)
    parsed_run = _clip_topn(parsed_run, topn)
    if not parsed_run:
        return 0.0
    evaluation = evaluator.evaluate(parsed_run)
    ndcg = np.mean([measures['ndcg'] for topic, measures in evaluation.items()])
    return ndcg


def get_random_ndcg(task, subset, topn=1000):
    """Returns the expected NDCG' of a random system on a subset of a task.

    NDCG' is the same as NDCG (Normalized Discounted Cumulative Gain), but all
    non-judged documents in the run are disregarded, see
    https://www.cs.rit.edu/~dprl/ARQMath/, section Ranking metrics.

    Parameters
    ----------
    task : str
        A task.
    subset : str
        A subset of the task.
    topn : int, optional
        The top N results, which will be considered in computing the NDCG.
        Default is 1000.

    Returns
    -------
    ndcg : float
        The expected NDCG' of a random system on the subset of the task.

    """
    judgements = sorted([
        judgement
        for subset in PARSED_RELEVANCE_JUDGEMENTS[subset][task].values()
        for judgement in subset.values()
    ], reverse=True)
    expected_judgement = np.mean(judgements)

    random_dcg = 0.0
    for i in range(min(len(judgements), topn)):
        random_dcg += expected_judgement / log2(i + 2)

    ideal_dcg = 0.0
    for i, judgement in enumerate(judgements):
        ideal_dcg += judgement / log2(i + 2)

    random_ndcg = random_dcg / ideal_dcg
    return random_ndcg


def get_random_normalized_ndcg(parsed_run, task, subset, topn=1000):
    """Returns the random-normalized NDCG' of a system's run on a subset of a task.

    NDCG' is the same as NDCG (Normalized Discounted Cumulative Gain), but all
    non-judged documents in the run are disregarded, see
    https://www.cs.rit.edu/~dprl/ARQMath/, section Ranking metrics.

    The random-normalized NDCG' takes the expected NDCG' of a random system
    into account. NDCG' of 1.0 is normalized to 1.0, NDCG' of a random system
    is normalized to 0.0, NDCG' worse that a random system is normalized to 0.0.

    Parameters
    ----------
    parsed_run : dict of (str, dict of (str, float))
        The run of an information retrieval system.
    task : str
        A task.
    subset : str
        A subset of the task.
    topn : int, optional
        The top N results, which will be considered in computing the NDCG.
        Default is 1000.

    Returns
    -------
    ndcg : float
        The random-normalized NDCG' of the system's run on the subset of the task.

    """
    ndcg = get_ndcg(parsed_run, task, subset, topn)
    random_ndcg = get_random_ndcg(task, subset, topn)
    random_normalized_ndcg = (ndcg - random_ndcg) / (1.0 - random_ndcg)
    return random_normalized_ndcg
