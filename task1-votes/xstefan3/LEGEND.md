Sentence-BERT (or in short **sbert**) system able to minimize the distances of two joint representations of associated pieces of text. It is trained with an objective to align the given distances of two texts with the predicted distances.

**CompuBert** is an IR system that **minimises a distance of a question to its relevant answers**. In the scope of ARQMath CLEF '20 Task 1, we consider a ground-truth relevance score of the answers for the question to be the answers' relative number of **upvotes**.

CompuBert further introduces the customization encoded in the results names. A categorized list of customizations is listed here.
Each of the parameters in the experiment name results mean that the listed change has been applied to the default implementation. In case where the parameter occurs only one, the objective of the experiment was to measure the respective change in accuracy as compared to the same configuration without the parameter.

- Math
  - nopreproc: formulae in posts are kept in LaTEX format
  - html-removal: all <*> tags have been removed from post body
  - prefix: formulae have been replaced with their respective prefix notation equivalent. The type identifiers have been extended. (V->var, O->function, ...)
  - infix: the same, with infix notation equivalent. Extension included.
  - datav: version of the data and formulaes used for the experiment. In case of datav0.2, furmulae v0.1 has been used
  - vit: Vit's preprocessing, this was to evaluate the sanity of the implemented CompuBert preprocessing
  
- Data
  - (no-)token-type: whether an identification mask of the math input has been added to BERT input.
  
- Other
  - exid: ordinal identifier of the experiment. The experiments have been made chronologically in increasing order.
