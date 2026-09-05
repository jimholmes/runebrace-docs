# Glossary

Here are common terms and phrases used in Runebrace.

<!--
Keep this list manually organized alphabetically.

This is **PANDOC SPECIFIC**

Use 
   [Term]{#ID}
   : Definition...

IDs must be unique as they're all collapsed into one doc before rendering into the PDF.

Reference a term here the first time it's used in the docs:
   [Rim](#Rim)

-->


[Path]{#path}
: Path applies to Line, Arc, and Circle. For two selected supports, Runebrace builds a path using a raycast between two points. For three selected supports, Runebrace will build a path by creating a curve that passes through all three supports' contact points.

[Raycast]{#raycast}
: A virtual ray is cast through the model from a source to a target. This ray can be traced to determine intersection points with the model. For example, when adding line supports, a raycast is made from the tip of the first support to the tip of the second. The ray is examined for where the model is on, above, or below the ray which then determines support placement.

[Rim]{#rim}

: In triangle mode, "Rim" denotes the border of a painted triangle selection. It is determined from the mesh edges, and can have both an outer border *plus* the borders of any holes inside that particular selection. See also: "Outer Rim Only" and "All boundaries" options in the Triangle Paint panel.

