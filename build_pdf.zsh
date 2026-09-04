#!/bin/zsh

cd ~/workspaces/runebrace-docs

pandoc Index.md \
  guides/Overview.md \
  guides/GettingStarted.md \
  guides/SupportingModels.md \
  guides/WorkingWithMeshes.md \
  guides/Hollowing.md \
  guides/PrintingAndSlicing.md \
  guides/Glossary.md \
-f markdown-implicit_figures \
-H header.tex \
-o output/RuneBraceManual.pdf \
--pdf-engine=/Library/TeX/texbin/pdflatex \
--resource-path=.:./assets/img:./guides
