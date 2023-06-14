---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell}
:tags: [remove-cell]

%matplotlib inline
```

# Exercise: Expressing a series of frames

In {numref}`fig_geometry_basics_exercise`, the position of the elbow in global coordinates is $(0.34, 0.371, 0)$. Therefore, the frame the expresses the position and incline of the forearm is:

$$
~^\text{global}_\text{forearm}T = \begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 & 0.34 \\
\sin(\theta) & \cos(\theta) & 0 & 0.371 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Using [Kinetics Toolkit's conventions](geometry_dimension_conventions.md), create a NumPy array that expresses the series of frames for a movement consisting of three inclines: 0°, 15° and 25°.

```{code-cell}
:tags: [hide-cell]

import numpy as np


frames = np.array(
    [
        [
            [np.cos(0.0), -np.sin(0.0), 0.0, 0.34],
            [np.sin(0.0), np.cos(0.0), 0.0, 0.371],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        [
            [np.cos(np.deg2rad(15.0)), -np.sin(np.deg2rad(15.0)), 0.0, 0.34],
            [np.sin(np.deg2rad(15.0)), np.cos(np.deg2rad(15.0)), 0.0, 0.371],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        [
            [np.cos(np.deg2rad(25.0)), -np.sin(np.deg2rad(25.0)), 0.0, 0.34],
            [np.sin(np.deg2rad(25.0)), np.cos(np.deg2rad(25.0)), 0.0, 0.371],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
    ]
)

frames
```
