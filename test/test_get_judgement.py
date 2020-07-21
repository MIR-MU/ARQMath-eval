from math import log2
import unittest

from arqmath_eval import get_judgement


class TestGetJudgement(unittest.TestCase):
    def test_existent(self):
        judgement = get_judgement('task1-example', 'test', 'A.78', '493764')
        expected_judgement = 3
        self.assertEqual(expected_judgement, judgement)

    def test_nonexistent_judged_document(self):
        judgement = get_judgement('task1-example', 'test', 'A.78', 'nonexistent')
        expected_judgement = None
        self.assertEqual(expected_judgement, judgement)

    def test_nonexistent_topic(self):
        judgement = get_judgement('task1-example', 'test', 'nonexistent', '493764')
        expected_judgement = None
        self.assertEqual(expected_judgement, judgement)

    def test_nonexistent_subset(self):
        judgement = get_judgement('task1-example', 'nonexistent', 'A.79', '493764')
        expected_judgement = None
        self.assertEqual(expected_judgement, judgement)

    def test_nonexistent_task(self):
        judgement = get_judgement('nonexistent', 'test', 'A.78', '493764')
        expected_judgement = None
        self.assertEqual(expected_judgement, judgement)
