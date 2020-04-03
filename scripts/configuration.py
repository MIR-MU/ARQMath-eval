RELEVANCE_JUDGEMENTS = {
    'task1': 'qrel.V1.0-test.tsv',
    'ntcir-11-math-2-main': 'NTCIR11_Math-qrels-test.dat',
    'ntcir-12-mathir-arxiv-main': 'NTCIR12_Math-qrels_agg-test.dat',
    'ntcir-12-mathir-math-wiki-formula': 'NTCIR12_MathWikiFrm-qrels_agg-test.dat',
}
TASK_README_HEAD = r'''
This table contains the best result for every user.

| nDCG | User | Result name |
|:-----|------|:------------|
'''.strip()
USER_README_HEAD = r'''
This table contains all results for user *%s* in descending order of task
performance.  Result names are based on the filenames of the results with
underscores (`_`) replaced with a comma and a space for improved readability.

| nDCG | Result name |
|------|:------------|
'''.strip()
