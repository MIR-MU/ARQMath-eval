### Description
#### Tasks
This repository evaluates the performance of your information retrieval system
on a number of *tasks*:

- `task1-example` – [ARQMath Task1][arqmath-task1] example dataset,
- `task1-votes` – [ARQMath Task1][arqmath-task1] Math StackExchange [user votes][],
- `task1`, `task1-2020` – [ARQMath Task1][arqmath-task1] final dataset,
- `task1-2021` – [ARQMath-2 Task1][arqmath-task1] final dataset,
- `ntcir-11-math-2-main` – [NTCIR-11 Math-2 Task Main Subtask][ntcir-11-math-2],
- `ntcir-12-mathir-arxiv-main` – [NTCIR-12 MathIR Task ArXiv Main Subtask][ntcir-12-mathir],
- `ntcir-12-mathir-math-wiki-formula` – [NTCIR-12 MathIR Task MathWikiFormula Subtask][ntcir-12-mathir],
- `task2`, `task2-2020` – [ARQMath Task2][arqmath-task2] final dataset, and
- `task2-2021` – [ARQMath-2 Task2][arqmath-task2] final dataset.

The main tasks are:

- `task1` – Use this task to evaluate your ARQMath task 1 system, and
- `task2` – Use this task to evaluate your ARQMath task 2 system.

#### Subsets
Each task comes with three *subsets*:

- `train` – The training set, which you can use for supervised training of your
  system.
- `validation` – The validation set, which you can use to compare the
  performance of your system with different parameters. The validation set is
  used to compute the leaderboards in this repository.
- `test` – The test set, which you currently should not use at all. It will be
  used at the end to compare the systems, which performed best on the
  validation set.

The `task1` and `task2` tasks also come with the `all` subset, which contains
all relevance judgements. Use these to evaluate a system that has not been
trained using subsets of the `task1` and `task2` tasks.

The `task1` and `task2` tasks also come with a different subset split used by
the MIRMU and MSM teams in the ARQMath-2 competition submissions. This split is
also used in [the pv211-utils library][pv211-utils]:

- `train-pv211-utils` – The training set, which you can use for supervised
  training of your system.
- `validation-pv211-utils` – The validation set, which you can use for
  hyperparameter optimization or model selection.

The training set is futher split into the `smaller-train-pv211-utils` and
`smaller-validation` subsets in case you need two validation sets for e.g.
hyperparameter optimization and model selection. If you don't use either
hyperparameter optimization or model selection, you can use the
`bigger-train-pv211-utils` subset, which combines the `train-pv211-utils` and
`validation-pv211-utils` subsets.

- `test-pv211-utils` – The test set, which you currently should only use for
  the final performance estimation of your system.

### Examples
#### Using the `train` subset to train your supervised system

``` sh
$ pip install --force-reinstall git+https://github.com/MIR-MU/ARQMath-eval@0.0.21
$ python
>>> from arqmath_eval import get_topics, get_judged_documents, get_ndcg
>>>
>>> task = 'task1'
>>> subset = 'train'
>>> results = {}
>>> for topic in get_topics(task=task, subset=subset):
>>>     results[topic] = {}
>>>     for document in get_judged_documents(task=task, subset=subset, topic=topic):
>>>        similarity_score = compute_similarity_score(topic, document)
>>>        results[topic][document] = similarity_score
>>>
>>> get_ndcg(results, task='task1-votes', subset='train', topn=1000)
0.5876
```

#### Using the `validation` subset to compare various parameters of your system

``` sh
$ pip install --force-reinstall git+https://github.com/MIR-MU/ARQMath-eval@0.0.21
$ python
>>> from arqmath_eval import get_topics, get_judged_documents
>>>
>>> task = 'task1'
>>> subset = 'validation'
>>> results = {}
>>> for topic in get_topics(task=task, subset=subset):
>>>     results[topic] = {}
>>>     for document in get_judged_documents(task=task, subset=subset, topic=topic):
>>>        similarity_score = compute_similarity_score(topic, document)
>>>        results[topic][document] = similarity_score
>>>
>>> user = 'xnovot32'
>>> description = 'parameter1=value_parameter2=value'
>>> filename = '{}/{}/{}.tsv'.format(task, user, description)
>>> with open(filename, 'wt') as f:
>>>     for topic, documents in results.items():
>>>         top_documents = sorted(documents.items(), key=lambda x: x[1], reverse=True)[:1000]
>>>         for rank, (document, score) in enumerate(top_documents):
>>>             line = '{}\txxx\t{}\t{}\t{}\txxx'.format(topic, document, rank + 1, score)
>>>             print(line, file=f)
$ git add task1-votes/xnovot32/result.tsv  # track your new result with Git
$ python -m arqmath_eval.evaluate          # run the evaluation
$ git add -u                               # add the updated leaderboard to Git
$ git push                                 # publish your new result and the updated leaderboard
```

#### Using the `all` subset to compute the NDCG' score of an ARQMath submission

``` sh
$ pip install --force-reinstall git+https://github.com/MIR-MU/ARQMath-eval@0.0.21
$ python -m arqmath_eval.evaluate MIRMU-task1-Ensemble-auto-both-A.tsv all 2020
0.238, 95% CI: [0.198; 0.278]
```

 [arqmath-task1]:              https://www.cs.rit.edu/~dprl/ARQMath/Task1-answers.html (Task 1: Find Answers)
 [arqmath-task2]:              https://www.cs.rit.edu/~dprl/ARQMath/task2-formulas.html (Task 2: Formula Search)
 [ntcir-11-math-2]:            http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.686.444&rep=rep1&type=pdf (NTCIR-11 Math-2 Task Overview)
 [ntcir-12-mathir]:            https://www.cs.rit.edu/~rlaz/files/ntcir12-mathir.pdf (NTCIR-12 MathIR Task Overview)
 [treceval-format]:            https://stackoverflow.com/a/8175382/657401 (How to evaluate a search/retrieval engine using trec_eval?)
 [user votes]:                 https://gitlab.fi.muni.cz/xnovot32/arqmath-data-preprocessing/-/blob/master/scripts/xml_to_qrels_tsv.py
 [pv211-utils]:                https://gitlab.fi.muni.cz/xstefan3/pv211-utils (Utilities for PV211 project)
