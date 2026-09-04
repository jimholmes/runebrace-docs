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

![Polygon Fill button](../assets/img/LPanel-PolygonFill.png){height="200"}


Polygon Fill takes three or more selected supports as the corners of a polygon and fills the area inside it with supports.


![Poly fill](../assets/img/RoundBase-3Supports-PolyFill.png)


#### Perimeter and Fill

Perimeter & Fill does the same but also lays supports along the outline itself, which is the difference the highlighted border in the icon is showing.


![Poly fill with border](../assets/img/RoundBase-3Supports-PolyFillBorder.png)


#### Circle Fill


Circle Fill takes exactly three supports, builds the circle that passes through their contact points, and fills that.

![Circle fill](../assets/img/RoundBase-3Supports-CircleFill.png)


## Triangle Painting

[Rim](guides/Glossary.md#rim)

## Presets