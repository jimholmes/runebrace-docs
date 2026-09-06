#!/bin/zsh

export PATH="/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

cd ~/workspaces/runebrace-docs

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
rm -rf site/*

# copy assets to site folder
rsync -a content/assets site

# create HTML, use lua filters for fixing links
## Root index file
pandoc content/Index.md -o site/Index.html \
    --standalone --lua-filter=md-links.lua

## files in guides
for f in content/guides/*.md; do
  pandoc "$f" -o "site/guides/${f:t:r}.html" \
    --standalone --lua-filter=md-links.lua
done
