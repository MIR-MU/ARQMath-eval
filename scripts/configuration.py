import os.path

from pytrec_eval import parse_qrel, RelevanceEvaluator


TASK_README_HEAD = r'''
This table contains the best result for every user on the *%s* task.

| nDCG | Result name | User |
|:-----|:------------|------|
'''.strip()
USER_README_HEAD = r'''
This table contains all results for user *%s* in descending order of task
performance.  Result names are based on the filenames of the results with
underscores (`_`) replaced with a comma and a space for improved readability.

| nDCG | Result name |
|------|:------------|
'''.strip()
RELEVANCE_JUDGEMENTS = {
    'train': {
        'task1': 'qrel_task1_2020-train.tsv',
        'task1-2020': 'qrel_task1_2020-train.tsv',
        'task2': 'qrel_task2_2020-train.tsv',
        'task2-2020': 'qrel_task2_2020-train.tsv',
        'task1-example': 'qrel.V1.0-train.tsv',
        'task1-votes': 'votes-qrels-train.V1.0.tsv',
        'ntcir-11-math-2-main': 'NTCIR11_Math-qrels-train.dat',
        'ntcir-12-mathir-arxiv-main': 'NTCIR12_Math-qrels_agg-train.dat',
        'ntcir-12-mathir-math-wiki-formula': 'NTCIR12_MathWikiFrm-qrels_agg-train.dat',
    },
    'train-pv211-utils': {
        'task1': 'qrel_task1_2020-train-pv211-utils.tsv',
        'task1-2020': 'qrel_task1_2020-train-pv211-utils.tsv',
    },
    'smaller-train-pv211-utils': {
        'task1': 'qrel_task1_2020-smaller-train-pv211-utils.tsv',
        'task1-2020': 'qrel_task1_2020-smaller-train-pv211-utils.tsv',
    },
    'bigger-train-pv211-utils': {
        'task1': 'qrel_task1_2020-bigger-train-pv211-utils.tsv',
        'task1-2020': 'qrel_task1_2020-bigger-train-pv211-utils.tsv',
    },
    'small-validation': {
        'task1-votes': 'votes-qrels-small-validation.V1.0.tsv',
    },
    'validation': {
        'task1': 'qrel_task1_2020-validation.tsv',
        'task1-2020': 'qrel_task1_2020-validation.tsv',
        'task2': 'qrel_task2_2020-validation.tsv',
        'task2-2020': 'qrel_task2_2020-validation.tsv',
        'task1-example': 'qrel.V1.0-validation.tsv',
        'task1-votes': 'votes-qrels-validation.V1.0.tsv',
        'ntcir-11-math-2-main': 'NTCIR11_Math-qrels-validation.dat',
        'ntcir-12-mathir-arxiv-main': 'NTCIR12_Math-qrels_agg-validation.dat',
        'ntcir-12-mathir-math-wiki-formula': 'NTCIR12_MathWikiFrm-qrels_agg-validation.dat',
    },
    'validation-pv211-utils': {
        'task1': 'qrel_task1_2020-validation-pv211-utils.tsv',
        'task1-2020': 'qrel_task1_2020-validation-pv211-utils.tsv',
    },
    'smaller-validation-pv211-utils': {
        'task1': 'qrel_task1_2020-smaller-validation-pv211-utils.tsv',
        'task1-2020': 'qrel_task1_2020-smaller-validation-pv211-utils.tsv',
    },
    'test': {
        'task1': 'qrel_task1_2020-test.tsv',
        'task1-2020': 'qrel_task1_2020-test.tsv',
        'task2': 'qrel_task2_2020-test.tsv',
        'task2-2020': 'qrel_task2_2020-test.tsv',
        'task1-example': 'qrel.V1.0-test.tsv',
        'task1-votes': 'votes-qrels-test.V1.0.tsv',
        'ntcir-11-math-2-main': 'NTCIR11_Math-qrels-test.dat',
        'ntcir-12-mathir-arxiv-main': 'NTCIR12_Math-qrels_agg-test.dat',
        'ntcir-12-mathir-math-wiki-formula': 'NTCIR12_MathWikiFrm-qrels_agg-test.dat',
    },
    'test-pv211-utils': {
        'task1': 'qrel_task1_2020-test-pv211-utils.tsv',
        'task1-2020': 'qrel_task1_2020-test-pv211-utils.tsv',
    },
    'all': {
        'task1': 'qrel_task1_2020.tsv',
        'task1-2020': 'qrel_task1_2020.tsv',
        'task1-2021': 'qrel_task1_2021.tsv',
        'task2': 'qrel_task2_2020.tsv',
        'task2-2020': 'qrel_task2_2020.tsv',
        'task2-2021': 'qrel_task2_2021.tsv',
        'task1-votes.V1.2': 'votes-qrels.V1.2.tsv',
        'task2-topics-formula_ids.V.1.1': 'topics-formula_ids-qrels.V1.1.tsv',
    }
}
TASKS = list(RELEVANCE_JUDGEMENTS['validation'].keys())
PARSED_RELEVANCE_JUDGEMENTS = {}
EVALUATORS = {}
for subset, filenames in RELEVANCE_JUDGEMENTS.items():
    PARSED_RELEVANCE_JUDGEMENTS[subset] = {}
    EVALUATORS[subset] = {}
    for task, filename in filenames.items():
        relevance_judgements_filename = os.path.join(
            os.path.dirname(__file__),
            RELEVANCE_JUDGEMENTS[subset][task],
        )
        with open(relevance_judgements_filename, 'rt') as f:
            parsed_relevance_judgements = parse_qrel(f)
        evaluator = RelevanceEvaluator(parsed_relevance_judgements, {'ndcg'})
        PARSED_RELEVANCE_JUDGEMENTS[subset][task] = parsed_relevance_judgements
        EVALUATORS[subset][task] = evaluator
