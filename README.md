### Description
#### Tasks
This repository evaluates the performance of your information retrieval system
on a number of *tasks*:

- `task1` – [ARQMath Task1][arqmath-task1] validation dataset,
- `task1-votes` – [ARQMath Task1][arqmath-task1] Math StackExchange [user votes][],
- `ntcir-11-math-2-main` – [NTCIR-11 Math-2 Task Main Subtask][ntcir-11-math-2], and
- `ntcir-12-mathir-arxiv-main` – [NTCIR-12 MathIR Task ArXiv Main Subtask][ntcir-12-mathir].
- `ntcir-12-mathir-math-wiki-formula` – [NTCIR-12 MathIR Task MathWikiFormula Subtask][ntcir-12-mathir].

The main tasks are:

- `task1-votes` – Use this task to evaluate your ARQMath task 1 system.
- `ntcir-12-mathir-math-wiki-formula` – Use this task to evaluate your ARQMath task 2 system.

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

### Usage
#### Using the `train` set to train your supervised system

``` sh
$ pip install --force-reinstall git+https://gitlab.fi.muni.cz/xstefan3/arqmath-eval@0.0.5
$ python
>>> from arqmath_eval import get_topics, get_judged_documents, get_ndcg
>>>
>>> task = 'task1-votes'
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

Here is the documentation of the available evaluation functions:

- [`get_topics(task, subset=None)`][get_topics],
- [`get_judged_documents(task, subset=None, topic=None)`][get_judged_documents],
- [`get_random_ndcg(task, subset, topn=1000)`][get_random_ndcg],
- [`get_ndcg(parsed_run, task, subset, topn=1000)`][get_ndcg], and
- [`get_random_normalized_ndcg(parsed_run, task, subset, topn=1000)`][get_random_normalized_ndcg].

#### Using the `validation` set to compare various parameters of your system

``` sh
$ pip install --force-reinstall git+https://gitlab.fi.muni.cz/xstefan3/arqmath-eval@0.0.5
$ python
>>> from arqmath_eval import get_topics, get_judged_documents
>>>
>>> task = 'task1-votes'
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

``` sh
```

 [arqmath-task1]:              https://www.cs.rit.edu/~dprl/ARQMath/Task1-answers.html (Task 1: Find Answers)
 [get_judged_documents]:       https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L59
 [get_ndcg]:                   https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L90
 [get_random_ndcg]:            https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L124
 [get_random_normalized_ndcg]: https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L167
 [get_topics]:                 https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L34
 [ntcir-11-math-2]:            http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.686.444&rep=rep1&type=pdf (NTCIR-11 Math-2 Task Overview)
 [ntcir-12-mathir]:            https://www.cs.rit.edu/~rlaz/files/ntcir12-mathir.pdf (NTCIR-12 MathIR Task Overview)
 [treceval-format]:            https://stackoverflow.com/a/8175382/657401 (How to evaluate a search/retrieval engine using trec_eval?)
 [user votes]:                 https://gitlab.fi.muni.cz/xnovot32/arqmath-data-preprocessing/-/blob/master/scripts/xml_to_qrels_tsv.py
