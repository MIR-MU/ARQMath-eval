#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='arqmath_eval',
    version='0.0.18',
    description='Evaluation of ARQMath systems',
    packages=['arqmath_eval'],
    package_dir={'arqmath_eval': 'scripts'},
    install_requires=[
        'numpy~=1.18.2',
        'pytrec-eval~=0.4',
        'scipy~=1.5.2',
        'tqdm~=4.46.0',
    ],
    package_data={
        'arqmath_eval': [
            'NTCIR11_Math-qrels-train.dat',
            'NTCIR11_Math-qrels-validation.dat',
            'NTCIR11_Math-qrels-test.dat',
            'NTCIR12_Math-qrels_agg-train.dat',
            'NTCIR12_Math-qrels_agg-validation.dat',
            'NTCIR12_Math-qrels_agg-test.dat',
            'NTCIR12_MathWikiFrm-qrels_agg-train.dat',
            'NTCIR12_MathWikiFrm-qrels_agg-validation.dat',
            'NTCIR12_MathWikiFrm-qrels_agg-test.dat',
            'qrel.V1.0-train.tsv',
            'qrel.V1.0-validation.tsv',
            'qrel.V1.0-test.tsv',
            'votes-qrels-train.V1.0.tsv',
            'votes-qrels-small-validation.V1.0.tsv',
            'votes-qrels-validation.V1.0.tsv',
            'votes-qrels-test.V1.0.tsv',
            'votes-qrels.V1.2.tsv',
            'topics-formula_ids-qrels.V1.1.tsv',
            'qrel_task1-test.tsv',
            'qrel_task1-train.tsv',
            'qrel_task1.tsv',
            'qrel_task1-validation.tsv',
            'qrel_task2-test.tsv',
            'qrel_task2-train.tsv',
            'qrel_task2.tsv',
            'qrel_task2-validation.tsv',
        ],
    },
    include_package_data=True,
)
