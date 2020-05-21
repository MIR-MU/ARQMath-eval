This table contains all results for user *xnovot32* in descending order of task
performance.  Result names are based on the filenames of the results with
underscores (`_`) replaced with a comma and a space for improved readability.

| nDCG | Result name |
|------|:------------|
| 0.7614 | prefix, phrases=2, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7613 | prefix, phrases=6, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7613 | prefix, phrases=5, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7613 | prefix, phrases=1, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7613 | infix, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7612 | prefix, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7612 | prefix, phrases=10, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7612 | prefix, phrases=3, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7610 | prefix, phrases=4, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7607 | slt, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7606 | opt, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7602 | latex, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7600 | nomath, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| *0.7578* | *random* |

## Legend

The [SCM system][scm-at-arqmath] recogizes the following parameters:

- Dataset:
  - arxmliv, 08, 2019, no-problem – the no\_problem subset (150,701 documents) of [the arXMLiv 08.2019 dataset][arxmliv-08-2019]
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
- FastText:
  - alpha – initial learning rate
  - bucket – hash table bucket size
  - iter – the number of epochs
  - min-alpha – minimum learning rate
  - min-n, max-n – the range of modeled subword sizes
  - min-count – the minimum term frequency
  - negative – the number of negative samples
  - sample – sampling threshold
  - sg – the skipgram model
  - size – vector dimensions
  - window – window size
  - workers – the number of threads used for [hogwild][]
- Soft Cosine Measure:
  - dominant – whether the term similarity matrix will be strongly diagonally dominant
  - nonzero-limit – the maximum number of non-zero elements outside the diagonal in a single column of the term similarity matrix
  - symmetric – whether the term similarity matrix will be symmetric
  - exponent – parameter *o* in the [term similarity matrix formula][]
  - threshold – parameter *t* in the [term similarity matrix formula][]

 [arxmliv-08-2019]: https://sigmathling.kwarc.info/resources/arxmliv-dataset-082019/
 [collocation detection]: https://radimrehurek.com/gensim/models/phrases.html
 [hogwild]: https://papers.nips.cc/paper/4390-hogwild-a-lock-free-approach-to-parallelizing-stochastic-gradient-descent
 [scm-at-arqmath]: https://gitlab.fi.muni.cz/xnovot32/scm-at-arqmath (Soft Cosine Measure at ARQMath)
 [term similarity matrix formula]: https://arxiv.org/pdf/2003.05019.pdf#page=4
