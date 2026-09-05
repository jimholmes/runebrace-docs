#!/bin/zsh

export PATH="/Library/TeX/texbin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

cd ~/workspaces/runebrace-docs

pandoc Index.md \
  guides/Overview.md \
  guides/GettingStarted.md \
  guides/SupportingModels.md \
  guides/WorkingWithMeshes.md \
  guides/Hollowing.md \
  guides/PrintingAndSlicing.md \
  guides/Glossary.md \
-H header.tex \
-o output/RuneBraceManual.pdf \
--pdf-engine=/Library/TeX/texbin/pdflatex \
--resource-path=.:./assets/img:./guides


# -f markdown-implicit_figures \
