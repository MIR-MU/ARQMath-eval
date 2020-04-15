from math import log2
import unittest

from arqmath_eval import get_random_ndcg


class TestGetRandomNDCG(unittest.TestCase):
    def test(self):
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
