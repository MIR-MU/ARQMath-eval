#!/bin/bash
set -e
shopt -s nullglob

if [[ ! -e trec_eval ]]
then
  git clone https://github.com/usnistgov/trec_eval
  make -j -C trec_eval
fi

cd task1
# summary task 1 table header
cat > README-head.md << EOT
This table contains the best results for every user.

| User | nDCG | Result name |
|:-----|------|:------------|
EOT
for USER in */
do
  cd $USER
  # per-user task 1 table header
  cat > README-head.md << EOT
This table contains all results for $USER in descending order of task performance.  
Result names are based on the filenames of the results with underscores (\`_\`) replaced with a comma and a space for improved readability.

| nDCG | Result name |
|------|:------------|
EOT
  for RESULT in *.tsv
  do
    NDCG=$(../../trec_eval/trec_eval ../qrel.V0.1.tsv "$RESULT" -m ndcg | awk '{ print $3 }')
    # per-user task 1 table entries
    cat >> README-tail.md << EOT
| $NDCG | $(printf '%s\n' "${RESULT%.tsv}" | sed 's/_/, /g') |
EOT
  done
  (cat README-head.md && LC_ALL=C sort -k 2 -k 4 README-tail.md | tee >(
    # summary task 1 table header
    head -1 | while read LINE
    do
      printf '%s%s\n' "| [${USER%/}]($USER) " "$LINE"
    done >> ../README-tail.md
  )) > README.md
  rm README-head.md README-tail.md
  git add README.md
  cd ..
done
(cat README-head.md && LC_ALL=C sort -k 4 -k 2 -k 6 README-tail.md) > README.md
rm README-head.md README-tail.md
git add README.md
cd ..

if ! git diff --staged
then
  git commit -m 'Update result tables' --quiet
  if ! git push --quiet
  then
    git fetch
    git rebase master
    printf 'Failed to git push\n >&2'
    exit 1
  fi
fi
