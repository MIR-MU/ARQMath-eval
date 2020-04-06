#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='arqmath_eval',
    version='0.0.1',
    description='Evaluation of ARQMath systens',
    packages=['arqmath_eval'],
    package_dir={'arqmath_eval': 'scripts'},
    install_requires=[
        'numpy~=1.18.2',
        'pytrec-eval~=0.4',
    ],
    package_data={
        'arqmath_eval': [
            'NTCIR11_Math-qrels-train.dat',
            'NTCIR11_Math-qrels-test.dat',
            'NTCIR12_Math-qrels_agg-train.dat',
            'NTCIR12_Math-qrels_agg-test.dat',
            'NTCIR12_MathWikiFrm-qrels_agg-train.dat',
            'NTCIR12_MathWikiFrm-qrels_agg-test.dat',
            'qrel.V1.0-train.tsv',
            'qrel.V1.0-test.tsv',
        ],
    },
    include_package_data=True,
)
