---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib qt5
```

# Visualizing forces and other vectors

In addition to points and frames (local coordinate systems), The [Player](api/ktk.Player.rst) can represent forces or other vectors using its `vectors` property.

We start by loading a gait c3d file.

```{code-cell} ipython3
:tags: [remove-output]

import kineticstoolkit.lab as ktk
import numpy as np

contents = ktk.read_c3d(
    ktk.doc.download("c3d_sample.c3d"), convert_point_unit=True
)

p = ktk.Player(contents["Points"])
```

```{code-cell} ipython3
:tags: [remove-input]

points = contents["Points"].get_ts_between_times(3, 5.5)
# force_platforms = force_platforms.get_ts_between_times(3, 5.5)
p = ktk.Player(points)
p.zoom = 1.628894626777442
p.azimuth = 0.688
p.elevation = 0.26
p.pan = (-0.4663898987149148, -0.3352733755899471)
p._to_animation()
```


Let's add a vector at the right shoulder, that could for example represent the joint reaction force. For now, we will simply create a dummy sinusoidal vector:

```{code-cell} ipython3
forces = ktk.TimeSeries(time=contents["Points"].time)
forces.data["ShoulderForce"] = 500 * ktk.geometry.create_vector_series(
    y=np.sin(3 * forces.time)
)
```


Now we create a new Player that shows both points and forces:

```{code-cell} ipython3
:tags: [skip-execution]

p = ktk.Player(contents["Points"], forces)
```

```{code-cell} ipython3
:tags: [remove-input]

points = contents["Points"].get_ts_between_times(3, 5.5)
forces = forces.get_ts_between_times(3, 5.5)
p = ktk.Player(points, forces)
p.zoom = 1.628894626777442
p.azimuth = 0.688
p.elevation = 0.26
p.pan = (-0.4663898987149148, -0.3352733755899471)
p._to_animation()
```

The force is not shown yet, because the Player does not know how to represent the vector "ShoulderForce". This is configured by the Player's `vectors` property, which is a dict where:
- The key is the name of the force. Here, "ShoulderForce".
- The value is a dict with:
    - "Origin": The name of the point the vector origins from. Here, "r should", as read from the C3D file.
    - "Scale": Optional, the scale of the vector in meters per vector unit. It is 1 by default, but here we will set 0.001, which means in this case that the line will be one millimeter per newton.
    - "Color": Optional, an RGB color tuple.

To show the shoulder force:

```{code-cell} ipython3
p.vectors["ShoulderForce"] = {"Origin": "r should", "Scale": 0.001}
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```


## Force platforms

The previous section was a dummy example to show how to represent vectors in the Player. In this same file, we also have force platform contents. For visualization, we need to downsample it so that everything is on the same sampling rate:

```{code-cell} ipython3
points = contents["Points"]
force_platforms = contents["ForcePlatforms"].resample(points.time)
```


We can now visualize the points and force platform data in the Player:

```{code-cell} ipython3
:tags: [skip-execution]

p = ktk.Player(points, force_platforms)
```

```{code-cell} ipython3
:tags: [remove-input]

points = contents["Points"].get_ts_between_times(3, 5.5)
force_platforms = (
    contents["ForcePlatforms"]
    .resample(points.time)
    .get_ts_between_times(3, 5.5)
)
p = ktk.Player(points, force_platforms)
p.zoom = 1.628894626777442
p.azimuth = 0.688
p.elevation = 0.26
p.pan = (-0.4663898987149148, -0.3352733755899471)
p._to_animation()
```

As we see, the Player draws the platforms and the ground reaction forces by default, based on the default value of its `interconnections` and `vector` properties

```{code-cell} ipython3
p.interconnections
```

```{code-cell} ipython3
p.vectors
```


In these values, wildcards `*` are used to mean:
- Any point ending with `_Corner1` is connected to a matching point ending with `_Corner2`;
- Any point ending with `_Corner2` is connected to a matching point ending with `_Corner3`;
- etc.
- Any vector ending with `Force` is connected to a matching point ending with `COP`.
