from math import log2
from random import random
import unittest

from arqmath_eval import get_random_ndcg, get_ndcg, get_topics, get_judged_documents


class TestGetRandomNDCG(unittest.TestCase):
    def test_using_equation(self):
        ndcg = get_random_ndcg('task1', 'test')

        expected_judgement = (
            4 * 3.0 +
            4 * 2.0 +
            8 * 1.0 +
            2 * 0.0
        ) / 18
        expected_dcg = 0.0
        for i in range(1, 19):
            expected_dcg += expected_judgement / log2(i + 1)

        expected_idcg = 0.0
        for i in range(1, 5):
            expected_idcg += 3.0 / log2(i + 1)
        for i in range(5, 9):
            expected_idcg += 2.0 / log2(i + 1)
        for i in range(9, 17):
            expected_idcg += 1.0 / log2(i + 1)
        for i in range(17, 19):
            expected_idcg += 0.0 / log2(i + 1)

        expected_ndcg = expected_dcg / expected_idcg
        self.assertEqual(expected_ndcg, ndcg)

    def test_using_estimation(self):
        task = 'task1-votes'
        subset = 'small-validation'

        results = {}
        for topic in get_topics(task, subset):
            results[topic] = {}
            for document in get_judged_documents(task, subset, topic):
                similarity = random()
                results[topic][document] = similarity

        ndcg = get_ndcg(results, task, subset)
        expected_ndcg = get_random_ndcg(task, subset)
        self.assertAlmostEqual(expected_ndcg, ndcg, places=2)

    def test_with_topn(self):
        ndcg = get_random_ndcg('task1', 'test', 4)

        expected_judgement = (
            4 * 3.0 +
            4 * 2.0 +
            8 * 1.0 +
            2 * 0.0
        ) / 18
        expected_dcg = 0.0
        for i in range(1, 5):
            expected_dcg += expected_judgement / log2(i + 1)

        expected_idcg = 0.0
        for i in range(1, 5):
            expected_idcg += 3.0 / log2(i + 1)
        for i in range(5, 9):
            expected_idcg += 2.0 / log2(i + 1)
        for i in range(9, 17):
            expected_idcg += 1.0 / log2(i + 1)
        for i in range(17, 19):
            expected_idcg += 0.0 / log2(i + 1)

        expected_ndcg = expected_dcg / expected_idcg
        self.assertEqual(expected_ndcg, ndcg)
