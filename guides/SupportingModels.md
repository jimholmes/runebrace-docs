# Supporting Models

## Supporting Overview

<!--Don't write a tutorial. Point users elsewhere.-->

## Basic Workflow

**CONTENT NEEDED**

## Features

### Support Basics

**CONTENT NEEDED**

* Horizontal line of layers



#### Manual Supports

**CONTENT NEEDED**

#### Left Menu (REWORD)

The left icon panel controls many support options.

![Left panel icons](../assets/img/LPanel.png){#fig:LPanel}

### Symmetry

**CONTENT NEEDED**

### Path Supports

[Path](#path) supports are created on a line between two or more supports. A path is drawn from the tip of each support in the order they were selected. (Use F3 + LMB when selecting multiple supports.)

![Round Base with Three Supports](../assets/img/RoundBase-3Supports.png){#fig:InitialBaseExample}

Settings controlling spacing of supports for the following features are located in the right menu under Advanced Placement => Line and Fill.

![Right menu with line and fill highlighted](../assets/img/RMenu-AdvancedPlacement-TopLevel.png){height="400"}

> **Important Considerations**

> Settings in this section are not distances in millimeters; they are multipliers of the support diameter. Runebrace determines how many supports fit in the space between the selected supports, then spreads generated supports evenly along the segment.

> Very small values stop having an effect at some point, and are ignored.

> A segment too short to fit anything gets no supports.

#### Line

Adds support along a line between two and only two supports. 

Line placement is available through the right menu and the left button menu ([@fig:LPanel]).

Spacing for supports along the line is controlled by the right menu under Advanced Placement => Line & Fill => Line.

![Menu for adjusting Polygon Fill spacing](../assets/img/RMenu-AdvancedPlacement-LineAndFill-Line.png)

Selecting support #1, then #2, then creating Line supports results in this:

![Supports created via line](../assets/img/RoundBase-2Supports-CreateLine.png)


#### Arc

Using Arc adds supports along three selected supports&mdash;no more, no fewer.

Arc placement is available through the right menu and the left button menu ([@fig:LPanel]).

Configure using the settings in the right menu Advanced Placement => Line & Fill => Arc.

![Settings for Arcs](../assets/img/RMenu-AdvancedPlacement-LineAndFill-Arc.png){#fig:ArcSettings}

Selecting support #1, then #2, then #3, then creating Arc supports results in this:

![Supports created via Arc](../assets/img/RoundBase-3Supports-CreateArc.png)

Note the double supports appearing at callout #2. This is due to the spacing along the arc, with one added support being in close proximity to the original #2.


#### Circle

Using Circle adds supports along a circle path drawn through three supports&mdash;no more, no fewer.

Circle placement is available **only** through the left button menu ([@fig:LPanel]).
 
Configure using the settings in the right menu Advanced Placement => Line & Fill => Arc as shown above in [@fig:ArcSettings].

Selecting support #1, then #2, then #3, then creating Circle supports results in this:

![Supports created via Circle](../assets/img/RoundBase-3Supports-CreateCircle.png)

Again, note the doubled supports, this time at #2 and #3.


### Fill Basics

Runebrace also provides area fill capabilities.

We'll start with a basic example, then show a more complex, practical example after. Triangle Painting and fills are covered separately below.

Each feature below will show results starting from the above figure [@fig:InitialBaseExample], a round base with three supports selected in the order they're labeled.

#### Polygon Fill

Polygon Fill, commonly referred to as Poly Fill, fills an area defined by three or more supports. No rim support is created.

Poly Fill is available through the Fill Space option in the right menu and the corresponding button on the left button menu ([@fig:LPanel]).

You can also use the Fill Space button from the right menu (see below).

Using Poly Fill/Fill Space from our starting point results in this:

![Poly fill](../assets/img/RoundBase-3Supports-PolyFill.png)

**Why:** EDIT: ADD USE CASE

Adjust the spacing of the filled supports under Right Menu => Advanced Placement => Line and Fill => Fill Space

![Menu for adjusting Polygon Fill spacing](RMenu-AdvancedPlacement-LineAndFill-FillSpace.png){height="200"}

#### Perimeter and Fill

Perimeter & Fill does the same as Poly Fill but also lays supports along the area's bordering path itself. Note the menu button's icon shows this via the yellow outline.

Poly Fill is available **only** through the corresponding button on the left button menu ([@fig:LPanel]).

Select three or more supports, then press the Perimeter and Fill button (there's no alternative from the right menu). One action creates the perimeter and inside area supports.

Using Perimeter and Fill from our starting point results in this:

![Poly fill with Perimeter](../assets/img/RoundBase-3Supports-PolyFillPerimeter.png)

Perimeter and Fill has two separate adjustments:

* **Line:** Spacing between supports on the lines of the outer perimeter
* **Fill Space:** Spacing between supports in the grid that fills the area

![Menu for adjusting both Polygon Fill and Line spacing](RMenu-AdvancedPlacement-LineAndFill-LineAndFillBoth.png){height="200"}

These settings are demonstrated in the example below. The perimeter supports are denoted by the red hash lines and were configured with a spacing of 5.0. The inside area was configured with a spacing of 1.5.

![Poly fill with perimeter as seen from underneath](../assets/img/RoundBase-3Supports-PolyFillPerimeter-Below.png)

#### Circle Fill
Circle Fill takes exactly three supports, builds a circular path that passes through their contact points, and fills that. No path supports are created.

Circle Fill is available **only** through the corresponding button on the left button menu ([@fig:LPanel]).


Using Circle Fill from our starting point results in this:

![Circle fill](../assets/img/RoundBase-3Supports-CircleFill.png)

From below, the result looks like:

![Circle fill viewed from below](../assets/img/RoundBase-3Supports-CircleFill-Below.png)

## Triangle Painting

[Rim](guides/Glossary.md#rim)

## Deeper Dive on Placement

**lines**
"What happens when you draw support lines or arcs is that it simulates a mouse clicking on various points along this line (depending on the set distance) and performs a mouse raycast on the model. If the raycast hits the geometry and the face is not parallel to the build plate or tilted upwards, a support is placed. It is likely that there are some raycast misses, so the support cannot be placed and is skipped.  It's not a matter of whether the surface is flat... the geometry must be under the ray cast by the mouse and be a valid point for a support."

**details**

" Five details worth having in the docs. The perimeter walks the supports in selection order and closes the loop back to the first one, so the last segment is support N to support 1. The fill plane is defined by the first three supports only, not by all of them: any support beyond the third is flattened onto that plane, so a selection that is not roughly planar will not fill the way it looks. The grid covers the bounding box of the polygon in that plane and keeps the points that fall inside it, with one axis along support 1 to support 2 and the other perpendicular to it. Each grid point is then projected onto the model along the average tip direction of the selected supports, so the fill follows the surface, and where that ray misses the mesh no support appears, which is why gaps show up over holes or steep overhangs. Finally, Line and Fill Space are multipliers, not distances, and they multiply different reference diameters: Line multiplies the Base diameter, Fill Space multiplies the Top diameter. The same number on both sliders does not give the same spacing on the outline and on the fill. One more practical note: the operation records two undo steps, the perimeter and the fill, so undoing it takes two presses."

"very small values stop having an effect below a certain point, and a segment too short to fit anything simply gets no supports in between. Happy to give you the exact arithmetic if you want a footnote."


**Math on Determining Placement**
"step = Base diameter × Line (or Top diameter × Fill Space). Gaps = segment length ÷ step, rounded down. Supports added = gaps − 1, spread evenly, so the real spacing is segment length ÷ gaps. Because the count rounds down, the spacing is always at least the step and can reach almost double it. Yours: 26.73 mm ÷ 4 gaps = 6.68 mm, the 6.64 you measured."


## More Complex Examples

You should now understand the basics of creating supports with the various tools. The example above is very simplistic, so let's use more complex 


## Presets