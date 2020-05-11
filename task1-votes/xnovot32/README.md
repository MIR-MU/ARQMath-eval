This table contains all results for user *xnovot32* in descending order of task
performance.  Result names are based on the filenames of the results with
underscores (`_`) replaced with a comma and a space for improved readability.

| nDCG | Result name |
|------|:------------|
| 0.7613 | arxmliv, infix, 08, 2019, no-problem, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7612 | arxmliv, prefix, 08, 2019, no-problem, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7607 | arxmliv, slt, 08, 2019, no-problem, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7606 | arxmliv, opt, 08, 2019, no-problem, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7602 | arxmliv, latex, 08, 2019, no-problem, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| 0.7600 | arxmliv, nomath, 08, 2019, no-problem, phrases=0, alpha=0.05, bucket=2000000, iter=5, max-n=6, min-alpha=0, min-count=5, min-n=3, negative=5, sample=0.0001, sg=1, size=300, window=5, workers=64, dominant=True, nonzero-limit=100, symmetric=True, exponent=4.0, threshold=-1.0 |
| *0.7578* | *random* |

## Legend

The system recogizes the following parameters:

- Dataset:
  - arxmliv, 08, 2019, no-problem – The `no_problem` subset (150,701 documents) of [the arXMLiv 08.2019 dataset][arxmliv-08-2019]
  - phrases – Whether phrases are modeled in the corpus
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
  - min-count – minimum term frequency
  - negative – the number of negative samples
  - sample – sampling threshold
  - sg – the skipgram model
  - size – vector dimensions
  - window – window size
  - workers – the number of threads used in HogWild
- Soft Cosine Measure:
  - dominant – whether the term similarity matrix will be strongly diagonally dominant
  - nonzero-limit – the maximum number of non-zero elements outside the diagonal in a single column of the term similarity matrix
  - symmetric – whether the term similarity matrix will be symmetric
  - exponent – parameter `o` in the [term similarity matrix formula][]
  - threshold – parameter `t` in the [term similarity matrix formula][]

 [arxmliv-08-2019]: https://sigmathling.kwarc.info/resources/arxmliv-dataset-082019/
 [term similarity matrix formula]: https://arxiv.org/pdf/2003.05019.pdf#page=4
