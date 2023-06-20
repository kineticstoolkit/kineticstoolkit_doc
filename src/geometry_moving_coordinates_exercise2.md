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

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Exercise: Moving a trajectory

The trajectory of a point in global coordinates is:

$$
\vec{p}(t_0) = (3, 4, 5) \\
\vec{p}(t_1) = (4, 5, 5) \\
\vec{p}(t_2) = (5, 6, 5) \\
\vec{p}(t_3) = (6, 7, 5) \\
\vec{p}(t_4) = (7, 8, 5) \\
$$

Using Kinetics Toolkit's geometry module, rotate this whole trajectory anti-clockwise on the z axis by 20° then translate it by one unit to the left.

a) Do this exercise by creating the corresponding homogeneous transform using [ktk.geometry.create_transforms](api/ktk.geometry.create_transforms.rst), then by multiplying this transform by the point coordinates using [ktk.geometry.matmul](api/ktk.geometry.matmul.rst).

```{code-cell} ipython3
:tags: [hide-cell]

import kineticstoolkit.lab as ktk
import numpy as np


p = np.array(
    [
        [3.0, 4.0, 5.0, 1.0],
        [4.0, 5.0, 5.0, 1.0],
        [5.0, 6.0, 5.0, 1.0],
        [6.0, 7.0, 5.0, 1.0],
        [7.0, 8.0, 5.0, 1.0],
    ]
)

T = ktk.geometry.create_transforms(
    angles=[np.deg2rad(20)], seq="z", translations=[[-1.0, 0.0, 0.0]]
)

ktk.geometry.matmul(T, p)
```

b) Do this exercise using the [ktk.geometry.rotate](api/ktk.geometry.rotate.rst) and [ktk.geometry.translate](api/ktk.geometry.translate.rst) function.

```{code-cell} ipython3
:tags: [hide-cell]

p = np.array(
    [
        [3.0, 4.0, 5.0, 1.0],
        [4.0, 5.0, 5.0, 1.0],
        [5.0, 6.0, 5.0, 1.0],
        [6.0, 7.0, 5.0, 1.0],
        [7.0, 8.0, 5.0, 1.0],
    ]
)

rotated_p = ktk.geometry.rotate(p, angles=[np.deg2rad(20)], seq="z")
final_p = ktk.geometry.translate(rotated_p, translations=[[-1.0, 0.0, 0.0]])

final_p
```
