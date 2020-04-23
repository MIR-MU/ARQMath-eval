### Description
#### Tasks
This repository evaluates the performance of your information retrieval system
on a number of *tasks*:

- `task1` – [ARQMath Task1][arqmath-task1] validation dataset,
- `task1-votes` – [ARQMath Task1][arqmath-task1] Math StackExchange [user votes][],
- `ntcir-11-math-2-main` – [NTCIR-11 Math-2 Task Main Subtask][ntcir-11-math-2], and
- `ntcir-12-mathir-arxiv-main` – [NTCIR-12 MathIR Task ArXiv Main Subtask][ntcir-12-mathir].
- `ntcir-12-mathir-math-wiki-formula` – [NTCIR-12 MathIR Task MathWikiFormula Subtask][ntcir-12-mathir].

#### Subsets
Each task comes with a number of *subsets*:

- `train` – the training set, which you should use for parameter optimization
  before publishing the results for the best parameters of your system,
- `test` – the test set, which you should use *only for your best system* after
  parameter optimization on the training set,
- `train-train` – a subset of the training set for the `task1-votes` task,
  which you can use for training if you also require a validation subset (e.g.
  for early stopping), and
- `train-validation` – a subset of the training set for the `task1-votes` task,
  which you can use for training if you also require a validation subset (e.g.
  for early stopping).

### Usage
#### Evaluating your model with various parameters
Place your results in [the trec\_eval format][treceval-format] into the
`results.csv` file. To evaluate your results e.g. on the `train` subset of the
`task1-votes` task, execute the following commands:

``` sh
$ pip install git+https://gitlab.fi.muni.cz/xstefan3/arqmath-eval@master
$ python
>>> from arqmath_eval import get_ndcg
>>> from pytrec_eval import parse_run
>>>
>>> with open('results.csv', 'rt') as f:
>>>     results = parse_run(f)
>>> get_ndcg(results, task='task1-votes', subset='train')
0.5876
```

Beside `get_ndcg`, the Python interface of the package also provides the
following functions:

- [`get_topics(task, subset=None)`][get_topics],
- [`get_judged_documents(task, subset=None, topic=None)`][get_judged_documents],
- [`get_random_ndcg(task, subset)`][get_random_ndcg],
- [`get_ndcg(parsed_run, task, subset)`][get_ndcg], and
- [`get_random_normalized_ndcg(parsed_run, task, subset)`][get_random_ndcg].

#### Placing your results to the leaderboard
Place your results in [the trec\_eval format][treceval-format] into your
dedicated directory *task/user*, e.g. `task1-votes/xnovot32` for the user
@xnovot32 and the `task1-votes` task. To evaluate your results on the `test`
set of the `task1-votes` and publish the results into the leaderboard, execute
the following commands:

``` sh
$ git add task1-votes/xnovot32/result.tsv  # track your new result with Git
$ pip install git+https://gitlab.fi.muni.cz/xstefan3/arqmath-eval@master
$ python -m scripts.evaluate               # run the evaluation
$ git add -u                               # add the updated leaderboard to Git
$ git push                                 # publish your new result and the updated leaderboard
```

 [arqmath-task1]:              https://www.cs.rit.edu/~dprl/ARQMath/Task1-answers.html (Task 1: Find Answers)
 [get_judged_documents]:       https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L54
 [get_ndcg]:                   https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L86
 [get_random_ndcg]:            https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L115
 [get_random_normalized_ndcg]: https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L154
 [get_topics]:                 https://gitlab.fi.muni.cz/xstefan3/arqmath-eval/-/blob/master/scripts/common.py#L26
 [ntcir-11-math-2]:            http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.686.444&rep=rep1&type=pdf (NTCIR-11 Math-2 Task Overview)
 [ntcir-12-mathir]:            https://www.cs.rit.edu/~rlaz/files/ntcir12-mathir.pdf (NTCIR-12 MathIR Task Overview)
 [treceval-format]:            https://stackoverflow.com/a/8175382/657401 (How to evaluate a search/retrieval engine using trec_eval?)
 [user votes]:                 https://gitlab.fi.muni.cz/xnovot32/arqmath-data-preprocessing/-/blob/master/scripts/xml_to_qrels_tsv.py
