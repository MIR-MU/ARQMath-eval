import unittest

from arqmath_eval import get_topics


class TestGetTopics(unittest.TestCase):
    def test_all_subsets(self):
        topics = get_topics('task1')
        expected_topics = {'A.31', 'A.101', 'A.78'}
        self.assertEqual(expected_topics, topics)

    def test_selected_subsets(self):
        topics = get_topics('task1', 'train')
        expected_topics = {'A.31', 'A.101'}
        self.assertEqual(expected_topics, topics)

        topics = get_topics('task1', 'test')
        expected_topics = {'A.78'}
        self.assertEqual(expected_topics, topics)
