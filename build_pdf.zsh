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
--resource-path=.:./assets/img:./guides
