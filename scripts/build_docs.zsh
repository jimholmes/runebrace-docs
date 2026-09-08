#!/bin/zsh

export PATH="/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

# Project root
ROOT=${0:A:h:h}

##### Build PDF
# pandoc Index.md \
#   guides/Overview.md \
#   guides/GettingStarted.md \
#   guides/SupportingModels.md \
#   guides/WorkingWithMeshes.md \
#   guides/Hollowing.md \
#   guides/PrintingAndSlicing.md \
#   guides/Glossary.md \
# -F pandoc-crossref \
# -H header.tex \
# -o output/RuneBraceManual.pdf \
# --pdf-engine=/Library/TeX/texbin/pdflatex \
# --resource-path=.:./assets/img:./guides


##### Build HTML

# purge existing to ensure clean build
rm -rf $ROOT/docs/guides/*

# copy assets to docs folder
rsync -a $ROOT/content/assets $ROOT/docs

# copy CSS
cp $ROOT/css/* $ROOT/docs/css/

# create HTML, use lua filters for fixing links

print "$ROOT/css/nav.css "

## Root index file
pandoc $ROOT/content/Index.md -o $ROOT/docs/index.html \
    --include-before-body=$ROOT/docs/nav.html \
    --include-after-body=$ROOT/snippets/after.html \
    --css=css/nav.css \
    --css=css/docs.css \
    --standalone --lua-filter=$ROOT/scripts/md-links.lua \
    --filter pandoc-crossref

## MD files to process
list=$ROOT/scripts/ORDERED_FILE_LIST.txt

# Read the file into an array, one path per line.
# Empty lines and lines starting with # are skipped.
files=()
while IFS= read -r line || [[ -n $line ]]; do
  line=${line%%$'\r'}          # strip CR if the list is CRLF
  [[ -z $line || $line == \#* ]] && continue
  files+=("$ROOT/$line")
done < "$list"


for f in $files; do
  # trim CR, leading/trailing whitespace
  f=${f%%$'\r'}
  f=${f##[[:space:]]#}
  f=${f%%[[:space:]]#}

  if [[ ! -f $f ]]; then
    print -u2 "skipping missing file: $f"
    continue
  fi

  pandoc "$f" -o "$ROOT/docs/guides/${f:t:r}.html" \
    --include-before-body=$ROOT/docs/nav.html \
    --include-after-body=$ROOT/snippets/after.html \
    --standalone --lua-filter=$ROOT/scripts/md-links.lua \
    --css=../css/nav.css \
    --css=../css/docs.css \
    --filter pandoc-crossref

done
