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
