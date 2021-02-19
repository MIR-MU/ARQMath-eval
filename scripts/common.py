# -*- coding:utf-8 -*-

from copy import deepcopy
from math import log2

import numpy as np
import scipy.stats as st

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
        if task not in subset:
            continue
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
        if task not in subset:
            continue
        if topic is not None and topic not in subset[task]:
            continue
        topics = subset[task].values() if topic is None else [subset[task][topic]]
        for documents in topics:
            judged_documents.update(documents)
    return judged_documents


def get_ndcg(parsed_run, task, subset, topn=1000, confidence=None):
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
    confidence : float or None, optional
        The confidence level used to construct a confidence interval.
        If None, then no confidence interval is constructed. Default is None.

    Returns
    -------
    ndcg : float
        The NDCG' of the system's run on the subset of the task.
    interval : (float, float), optional
        The confidence interval for the NDCG'. Only produced when confidence is not None.

    """
    evaluator = EVALUATORS[subset][task]
    parsed_run = _remove_nonjudged_topics_and_documents(parsed_run, task, subset)
    parsed_run = _clip_topn(parsed_run, topn)
    if not parsed_run:
        return 0.0
    evaluation = evaluator.evaluate(parsed_run)
    sample = [measures['ndcg'] for topic, measures in evaluation.items()]
    ndcg = np.mean(sample)
    if confidence is not None:
        interval = st.t.interval(confidence / 100.0, len(sample) - 1, loc=ndcg, scale=st.sem(sample))
        return (ndcg, interval)
    else:
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
    random_ndcgs = []
    for topic in get_topics(task, subset):
        judgements = sorted([
            judgement
            for judgement in PARSED_RELEVANCE_JUDGEMENTS[subset][task][topic].values()
        ], reverse=True)
        expected_judgement = np.mean(judgements)

        random_dcg = 0.0
        for i in range(min(len(judgements), topn)):
            random_dcg += expected_judgement / log2(i + 2)

        ideal_dcg = 0.0
        for i, judgement in enumerate(judgements):
            ideal_dcg += judgement / log2(i + 2)

        random_ndcg = random_dcg / ideal_dcg if ideal_dcg > 0 else 0.0
        random_ndcgs.append(random_ndcg)

    return np.mean(random_ndcgs)


def get_random_normalized_ndcg(parsed_run, task, subset, topn=1000, ndcg=None):
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
    ndcg : float or None, optional
        The NDCG' to random-normalize. If not None, the parsed_run parameter
        will be ignored. Default is None.

    Returns
    -------
    ndcg : float
        The random-normalized NDCG' of the system's run on the subset of the task.

    """
    if ndcg is None:
        ndcg = get_ndcg(parsed_run, task, subset, topn)
    random_ndcg = get_random_ndcg(task, subset, topn)
    random_normalized_ndcg = (ndcg - random_ndcg) / (1.0 - random_ndcg)
    return random_normalized_ndcg


def get_judgement(task, subset, topic, judged_document):
    """Returns judgement of a document in a topic from a subset of a task, or None if none exists.

    NDCG' is the same as NDCG (Normalized Discounted Cumulative Gain), but all
    non-judged documents in the run are disregarded, see
    https://www.cs.rit.edu/~dprl/ARQMath/, section Ranking metrics.

    The random-normalized NDCG' takes the expected NDCG' of a random system
    into account. NDCG' of 1.0 is normalized to 1.0, NDCG' of a random system
    is normalized to 0.0, NDCG' worse that a random system is normalized to 0.0.

    Parameters
    ----------
    task : str
        A task.
    subset : str
        A subset of the task.
    topic : str
        A topic from the subset.
    judged_document : str
        A document in the topic.

    Returns
    -------
    judgement : int or None
        Returns judgement of a document in a topic for subset of a task, or None if none exists.

    """
    if subset not in PARSED_RELEVANCE_JUDGEMENTS \
            or task not in PARSED_RELEVANCE_JUDGEMENTS[subset] \
            or topic not in PARSED_RELEVANCE_JUDGEMENTS[subset][task] \
            or judged_document not in PARSED_RELEVANCE_JUDGEMENTS[subset][task][topic]:
        judgement = None
    else:
        judgement = PARSED_RELEVANCE_JUDGEMENTS[subset][task][topic][judged_document]
    return judgement
