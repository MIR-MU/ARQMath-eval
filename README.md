# ARQMath-eval
### Description

This repository evaluates the performance of your information retrieval system
on a number of *tasks*:

- `task1/` – [ARQMath Task1][arqmath-task1] validation dataset,
- `task1-votes/` – [ARQMath Task1][arqmath-task1] Math StackExchange [user votes][],
- `ntcir-11-math-2-main/` – [NTCIR-11 Math-2 Task Main Subtask][ntcir-11-math-2], and
- `ntcir-12-mathir-arxiv-main/` – [NTCIR-12 MathIR Task ArXiv Main Subtask][ntcir-12-mathir].
- `ntcir-12-mathir-math-wiki-formula/` – [NTCIR-12 MathIR Task MathWikiFormula Subtask][ntcir-12-mathir].

### Usage

Place your results in [the trec\_eval format][treceval-format] into your
dedicated directory *task/user*. To evaluate and publish your results,
execute the following commands:

``` sh
$ git add task/user/result.tsv     # track your new result with Git
$ pip install -e .                 # run the evaluation
$ python -m scripts.evaluate
$ git add -u                       # add the updated leaderboard to Git
$ git push                         # publish your new result and the updated leaderboard
```

 [arqmath-task1]:   https://www.cs.rit.edu/~dprl/ARQMath/Task1-answers.html (Task 1: Find Answers)
 [treceval-format]: https://stackoverflow.com/a/8175382/657401 (How to evaluate a search/retrieval engine using trec_eval?)
 [ntcir-11-math-2]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.686.444&rep=rep1&type=pdf (NTCIR-11 Math-2 Task Overview)
 [ntcir-12-mathir]: https://www.cs.rit.edu/~rlaz/files/ntcir12-mathir.pdf (NTCIR-12 MathIR Task Overview)
 [user votes]:      https://gitlab.fi.muni.cz/xnovot32/arqmath-data-preprocessing/-/blob/master/scripts/xml_to_qrels_tsv.py
