# Supporting Models

## Supporting Overview

<!--Don't write a tutorial. Point users elsewhere.-->

## Basic Workflow



## Features

### Support Basics

* Horizontal line of layers

#### Manual Supports


### Symmetry


### Path Supports

[Path](#path) supports 

#### Line

"What happens when you draw support lines or arcs is that it simulates a mouse clicking on various points along this line (depending on the set distance) and performs a mouse raycast on the model. If the raycast hits the geometry and the face is not parallel to the build plate or tilted upwards, a support is placed. It is likely that there are some raycast misses, so the support cannot be placed and is skipped.  It's not a matter of whether the surface is flat... the geometry must be under the ray cast by the mouse and be a valid point for a support."

#### Arc

#### Circle


### Fill Basics

We'll start with a basic example, then show a more complex, practical example after. Triangle Fills will be covered in a separate section below.

All examples start from this point.

![Round Base with Three Supports](../assets/img/RoundBase-3Supports.png)


#### Polygon Fill

Fill an area defined by three or more supports. Select three or more supports using F3 + LMB.

**Where:** ![Polygon Fill button](../assets/img/LPanel-PolygonFill.png){height="200"}

Also the Fill Space button from the right menu (see below).

The image below shows the result.

![Poly fill](../assets/img/RoundBase-3Supports-PolyFill.png)

**Why:** EDIT: ADD USE CASE

**Controlling:** Adjust the spacing of the fill under Right Menu => Advanced Placement => Line and Fill => Fill Space

![Menu for adjusting Polygon Fill spacing](RMenu-AdvancedPlacement-LineAndFill-FillSpace.png){height="200"}

#### Perimeter and Fill

![Polygon Fill button](../assets/img/LPanel-PerimiterAndFill.png){height="200"}


Perimeter & Fill does the same but also lays supports along the outline itself, which is the difference the highlighted border in the icon is showing.


![Poly fill with border](../assets/img/RoundBase-3Supports-PolyFillBorder.png)


#### Circle Fill

![Polygon Fill button](../assets/img/LPanel-CircleFill.png){height="200"}


Circle Fill takes exactly three supports, builds the circle that passes through their contact points, and fills that.

![Circle fill](../assets/img/RoundBase-3Supports-CircleFill.png)


## Triangle Painting

[Rim](guides/Glossary.md#rim)

## Presets