#!/bin/zsh

export PATH="/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

cd ~/workspaces/runebrace-docs

# Build PDF
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


# Build HTML
for f in guides/*.md; do
  pandoc "$f" -o "site/${f:t:r}.html" \
    --standalone --lua-filter=md-links.lua
done
# -f markdown-implicit_figures \
