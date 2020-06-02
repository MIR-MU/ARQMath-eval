This table contains all results for user *ayetiran* in descending order of task
performance.  Result names are based on the filenames of the results with
underscores (`_`) replaced with a comma and a space for improved readability.

| nDCG | Result name |
|------|:------------|
| 0.7604 | prefix, phrases=2, alpha=0.1, dm=0, dm-concat=1, epochs=5, hs=0, min-alpha=0, min-count=5, negative=12, vector-size=300, window=8 |
| 0.7579 | prefix, phrases=2, alpha=0.05, dm=1, dm-concat=1, epochs=5, hs=1, min-alpha=0, min-count=5, vector-size=400, window=4 |
| *0.7578* | *random* |

## Legend

The [Formula2Vec system][scm-at-arqmath] recogizes the following parameters:

- Dataset:
  - phrases – how many times [collocation detection][] and bigram merging are iteratively applied to the corpus:
    - 0 – the text and math tokens in the corpus are unchanged,
    - N –  [collocation detection][] and bigram merging are iteratively applied to both text and math tokens in the corpus N times
- Math representation:
  - opt – paths in operator tree
  - slt – paths in syntax layout tree
  - infix – nodes in operator tree in infix notation
  - prefix – nodes in operator tree in prefix notation
  - latex – untokenized LaTeX formulae
  - nomath – no math formulae
- Doc2Vec:
  - alpha – initial learning rate
  - min-alpha – minimum learning rate
  - dm – whether the distributed memory architecture is used instead of the distributed bag of words
  - dm-concat – whether the concatenation of context vectors is used instead of sum/average
  - hs – whether hierarchical softmax is used instead of softmax
  - min-count – the minimum term frequency
  - vector-size – vector dimensions
  - window – window size
  - epochs – the number of epochs

 [arxmliv-08-2019]: https://sigmathling.kwarc.info/resources/arxmliv-dataset-082019/
 [collocation detection]: https://radimrehurek.com/gensim/models/phrases.html
 [scm-at-arqmath]: https://gitlab.fi.muni.cz/xnovot32/scm-at-arqmath (Soft Cosine Measure at ARQMath)
