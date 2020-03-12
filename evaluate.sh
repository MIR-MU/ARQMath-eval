#!/bin/bash
set -e
shopt -s nullglob

cd task1
cat > README-head.md << EOT
| User | nDCG | Result name |
|:-----|------|:------------|
EOT
for USER in */
do
  cd $USER
  cat > README-head.md << EOT
| nDCG | Result name |
|------|:------------|
EOT
  for RESULT in *.tsv
  do
    NDCG=$(../../trec_eval/trec_eval ../qrel.V0.1.tsv "$RESULT" -m ndcg | awk '{ print $3 }')
    cat >> ../README-tail.md << EOT
| [${USER%/}](https://gitlab.fi.muni.cz/$USER) | $NDCG | $(printf '%s\n' "${RESULT%.tsv}" | sed 's/_/, /g') |
EOT
    cat >> README-tail.md << EOT
| $NDCG | $(printf '%s\n' "${RESULT%.tsv}" | sed 's/_/, /g') |
EOT
  done
  (cat README-head.md && sort -k 2 -k 4 README-tail.md) > README.md
  rm README-head.md README-tail.md
  git add README.md
  cd ..
done
(cat README-head.md && sort -k 4 -k 2 -k 6 README-tail.md) > README.md
rm README-head.md README-tail.md
git add README.md
cd ..

if ! git diff --quiet
then
  git commit -m 'Update result tables'
  git push
fi
