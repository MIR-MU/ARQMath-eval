from math import log2
import unittest

from arqmath_eval import get_random_ndcg, get_random_normalized_ndcg


class TestGetRandomNormalizedNDCG(unittest.TestCase):
    def test_hand_picked(self):
        parsed_run = {}
        random_ndcg = get_random_ndcg('task1-example', 'test')

        random_normalized_ndcg = get_random_normalized_ndcg(parsed_run, 'task1-example', 'test', ndcg=1.0)
        expected_random_normalized_ndcg = 1.0
        self.assertEqual(expected_random_normalized_ndcg, random_normalized_ndcg)

        random_normalized_ndcg = get_random_normalized_ndcg(parsed_run, 'task1-example', 'test', ndcg=random_ndcg)
        expected_random_normalized_ndcg = 0.0
        self.assertEqual(expected_random_normalized_ndcg, random_normalized_ndcg)

    def test_best(self):
        parsed_run = {
            'A.78': {
                '493782':  1.00,
                '493764':  0.95,
                '2008712': 0.90,
                '1282166': 0.85,
                '2008631': 0.80,
                '2008628': 0.75,
                '2008609': 0.70,
                '1116378': 0.65,
                '2008650': 0.60,
                '2008616': 0.55,
                '2008449': 0.50,
                '1282180': 0.45,
                '1282116': 0.40,
                '1282112': 0.35,
                '1116370': 0.30,
                '1116368': 0.25,
                '1282155': 0.20,
                '1282114': 0.15,
            }
        }
        random_normalized_ndcg = get_random_normalized_ndcg(parsed_run, 'task1-example', 'test')

        expected_random_normalized_ndcg = 1.0

        self.assertEqual(expected_random_normalized_ndcg, random_normalized_ndcg)

    def test_worst(self):
        parsed_run = {
            'A.78': {
                '493782':  0.15,
                '493764':  0.20,
                '2008712': 0.25,
                '1282166': 0.30,
                '2008631': 0.35,
                '2008628': 0.40,
                '2008609': 0.45,
                '1116378': 0.50,
                '2008650': 0.55,
                '2008616': 0.60,
                '2008449': 0.65,
                '1282180': 0.70,
                '1282116': 0.75,
                '1282112': 0.80,
                '1116370': 0.85,
                '1116368': 0.90,
                '1282155': 0.95,
                '1282114': 1.00,
            }
        }
        random_normalized_ndcg = get_random_normalized_ndcg(parsed_run, 'task1-example', 'test')

        expected_dcg = 0.0
        for i in range(1, 3):
            expected_dcg += 0.0 / log2(i + 1)
        for i in range(3, 11):
            expected_dcg += 1.0 / log2(i + 1)
        for i in range(11, 15):
            expected_dcg += 2.0 / log2(i + 1)
        for i in range(15, 19):
            expected_dcg += 3.0 / log2(i + 1)

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
        random_ndcg = get_random_ndcg('task1-example', 'test')
        expected_random_normalized_ndcg = (expected_ndcg - random_ndcg) / (1.0 - random_ndcg)
        self.assertEqual(expected_random_normalized_ndcg, random_normalized_ndcg)

    def test_best_with_topn(self):
        parsed_run = {
            'A.78': {
                '493782':  1.00,
                '493764':  0.95,
                '2008712': 0.90,
                '1282166': 0.85,
                '2008631': 0.80,
                '2008628': 0.75,
                '2008609': 0.70,
                '1116378': 0.65,
                '2008650': 0.60,
                '2008616': 0.55,
                '2008449': 0.50,
                '1282180': 0.45,
                '1282116': 0.40,
                '1282112': 0.35,
                '1116370': 0.30,
                '1116368': 0.25,
                '1282155': 0.20,
                '1282114': 0.15,
            }
        }
        random_normalized_ndcg = get_random_normalized_ndcg(parsed_run, 'task1-example', 'test', 4)

        expected_dcg = 0.0
        for i in range(1, 5):
            expected_dcg += 3.0 / log2(i + 1)

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
        random_ndcg = get_random_ndcg('task1-example', 'test', 4)
        expected_random_normalized_ndcg = (expected_ndcg - random_ndcg) / (1.0 - random_ndcg)
        self.assertEqual(expected_random_normalized_ndcg, random_normalized_ndcg)

    def test_worst_with_topn(self):
        parsed_run = {
            'A.78': {
                '493782':  0.15,
                '493764':  0.20,
                '2008712': 0.25,
                '1282166': 0.30,
                '2008631': 0.35,
                '2008628': 0.40,
                '2008609': 0.45,
                '1116378': 0.50,
                '2008650': 0.55,
                '2008616': 0.60,
                '2008449': 0.65,
                '1282180': 0.70,
                '1282116': 0.75,
                '1282112': 0.80,
                '1116370': 0.85,
                '1116368': 0.90,
                '1282155': 0.95,
                '1282114': 1.00,
            }
        }
        random_normalized_ndcg = get_random_normalized_ndcg(parsed_run, 'task1-example', 'test', 4)

        expected_dcg = 0.0
        for i in range(1, 3):
            expected_dcg += 0.0 / log2(i + 1)
        for i in range(3, 5):
            expected_dcg += 1.0 / log2(i + 1)

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
        random_ndcg = get_random_ndcg('task1-example', 'test', 4)
        expected_random_normalized_ndcg = (expected_ndcg - random_ndcg) / (1.0 - random_ndcg)
        self.assertEqual(expected_random_normalized_ndcg, random_normalized_ndcg)
