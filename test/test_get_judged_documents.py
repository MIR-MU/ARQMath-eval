import unittest

from arqmath_eval import get_judged_documents


class TestGetJudgedDocuments(unittest.TestCase):
    def test_all_subsets_and_all_topics(self):
        documents = get_judged_documents('task1')
        expected_documents = {
            '48162',
            '48164',
            '48165',
            '48167',
            '48172',
            '48181',
            '48184',
            '48202',
            '48219',
            '48235',
            '48241',
            '48260',
            '53779',
            '53781',
            '53784',
            '53790',
            '69435',
            '70739',
            '70741',
            '98328',
            '168286',
            '168290',
            '168305',
            '168323',
            '263828',
            '264299',
            '264315',
            '264329',
            '319916',
            '319917',
            '319919',
            '319938',
            '319993',
            '439027',
            '439044',
            '439055',
            '439132',
            '472635',
            '493764',
            '493782',
            '496898',
            '496909',
            '574514',
            '616315',
            '616321',
            '616373',
            '616514',
            '672516',
            '692232',
            '743738',
            '860842',
            '876137',
            '876221',
            '897705',
            '982759',
            '1018719',
            '1116368',
            '1116370',
            '1116378',
            '1282112',
            '1282114',
            '1282116',
            '1282155',
            '1282166',
            '1282180',
            '1489896',
            '1596444',
            '1609339',
            '1623400',
            '1639289',
            '2008449',
            '2008609',
            '2008616',
            '2008628',
            '2008631',
            '2008650',
            '2008712',
            '2170920',
            '2227543',
            '2362771',
            '2602592',
            '2780928',
            '2968174',
        }
        self.assertEqual(expected_documents, documents)

    def test_selected_subsets_all_topics(self):
        documents = get_judged_documents('task1', 'train')
        expected_documents = {
            '48162',
            '48164',
            '48165',
            '48167',
            '48172',
            '48181',
            '48184',
            '48202',
            '48219',
            '48235',
            '48241',
            '48260',
            '53779',
            '53781',
            '53784',
            '53790',
            '69435',
            '70739',
            '70741',
            '98328',
            '168286',
            '168290',
            '168305',
            '168323',
            '263828',
            '264299',
            '264315',
            '264329',
            '319916',
            '319917',
            '319919',
            '319938',
            '319993',
            '439027',
            '439044',
            '439055',
            '439132',
            '472635',
            '496898',
            '496909',
            '574514',
            '616315',
            '616321',
            '616373',
            '616514',
            '672516',
            '692232',
            '743738',
            '860842',
            '876137',
            '876221',
            '897705',
            '982759',
            '1018719',
            '1116368',
            '1282180',
            '1489896',
            '1596444',
            '1609339',
            '1623400',
            '1639289',
            '2170920',
            '2227543',
            '2362771',
            '2602592',
            '2780928',
            '2968174',
        }
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', 'test')
        expected_documents = {
            '493764',
            '493782',
            '1116368',
            '1116370',
            '1116378',
            '1282112',
            '1282114',
            '1282116',
            '1282155',
            '1282166',
            '1282180',
            '2008449',
            '2008609',
            '2008616',
            '2008628',
            '2008631',
            '2008650',
            '2008712',
        }
        self.assertEqual(expected_documents, documents)

    def test_all_subsets_selected_topics(self):
        documents = get_judged_documents('task1', topic='A.31')
        expected_documents = {
            '48162',
            '48164',
            '48165',
            '48167',
            '48172',
            '48181',
            '48184',
            '48202',
            '48219',
            '48235',
            '48241',
            '48260',
            '53779',
            '53781',
            '53784',
            '53790',
            '69435',
            '70739',
            '70741',
            '98328',
            '168286',
            '168290',
            '168305',
            '168323',
            '264329',
            '439044',
            '472635',
            '574514',
            '616315',
            '616321',
            '616373',
            '616514',
            '672516',
            '692232',
            '743738',
            '860842',
            '897705',
            '982759',
            '1018719',
            '1116368',
            '1282180',
            '1596444',
            '1609339',
            '1623400',
            '1639289',
            '2170920',
            '2227543',
            '2362771',
            '2602592',
            '2968174',
        }
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', topic='A.101')
        expected_documents = {
            '263828',
            '264299',
            '264315',
            '264329',
            '319916',
            '319917',
            '319919',
            '319938',
            '319993',
            '439027',
            '439044',
            '439055',
            '439132',
            '496898',
            '496909',
            '876137',
            '876221',
            '1489896',
            '2780928',
        }
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', topic='A.78')
        expected_documents = {
            '493764',
            '493782',
            '1116368',
            '1116370',
            '1116378',
            '1282112',
            '1282114',
            '1282116',
            '1282155',
            '1282166',
            '1282180',
            '2008449',
            '2008609',
            '2008616',
            '2008628',
            '2008631',
            '2008650',
            '2008712',
        }
        self.assertEqual(expected_documents, documents)

    def test_selected_subsets_selected_topics(self):
        documents = get_judged_documents('task1', 'train', 'A.31')
        expected_documents = {
            '48162',
            '48164',
            '48165',
            '48167',
            '48172',
            '48181',
            '48184',
            '48202',
            '48219',
            '48235',
            '48241',
            '48260',
            '53779',
            '53781',
            '53784',
            '53790',
            '69435',
            '70739',
            '70741',
            '98328',
            '168286',
            '168290',
            '168305',
            '168323',
            '264329',
            '439044',
            '472635',
            '574514',
            '616315',
            '616321',
            '616373',
            '616514',
            '672516',
            '692232',
            '743738',
            '860842',
            '897705',
            '982759',
            '1018719',
            '1116368',
            '1282180',
            '1596444',
            '1609339',
            '1623400',
            '1639289',
            '2170920',
            '2227543',
            '2362771',
            '2602592',
            '2968174',
        }
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', 'test', 'A.31')
        expected_documents = set()
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', 'train', 'A.101')
        expected_documents = {
            '263828',
            '264299',
            '264315',
            '264329',
            '319916',
            '319917',
            '319919',
            '319938',
            '319993',
            '439027',
            '439044',
            '439055',
            '439132',
            '496898',
            '496909',
            '876137',
            '876221',
            '1489896',
            '2780928',
        }
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', 'test', 'A.101')
        expected_documents = set()
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', 'train', 'A.78')
        expected_documents = set()
        self.assertEqual(expected_documents, documents)

        documents = get_judged_documents('task1', 'test', 'A.78')
        expected_documents = {
            '493764',
            '493782',
            '1116368',
            '1116370',
            '1116378',
            '1282112',
            '1282114',
            '1282116',
            '1282155',
            '1282166',
            '1282180',
            '2008449',
            '2008609',
            '2008616',
            '2008628',
            '2008631',
            '2008650',
            '2008712',
        }
        self.assertEqual(expected_documents, documents)
