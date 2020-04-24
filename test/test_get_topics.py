import unittest

from arqmath_eval import get_topics
from arqmath_eval.configuration import TASKS


class TestGetTopics(unittest.TestCase):
    def test_all_subsets(self):
        topics = get_topics('task1')
        expected_topics = {'A.31', 'A.101', 'A.78'}
        self.assertEqual(expected_topics, topics)

    def test_selected_subsets(self):
        topics = get_topics('task1', 'train')
        expected_topics = {'A.31'}
        self.assertEqual(expected_topics, topics)

        topics = get_topics('task1', 'validation')
        expected_topics = {'A.101'}
        self.assertEqual(expected_topics, topics)

        topics = get_topics('task1', 'test')
        expected_topics = {'A.78'}
        self.assertEqual(expected_topics, topics)

    def test_train_validation_test_split(self):
        for task in TASKS:
            train_topics = get_topics('task1', 'train')
            validation_topics = get_topics('task1', 'validation')
            test_topics = get_topics('task1', 'test')
            all_topics = get_topics('task1')
            self.assertEqual(len(validation_topics), len(test_topics))

            train_ratio = len(train_topics) / len(all_topics)
            validation_ratio = len(validation_topics) / len(all_topics)
            self.assertTrue(
                train_ratio == validation_ratio or
                (
                    0.7 < train_ratio and 0.9 > train_ratio and
                    0.1 < validation_ratio and 0.3 > validation_ratio
                )
            )
