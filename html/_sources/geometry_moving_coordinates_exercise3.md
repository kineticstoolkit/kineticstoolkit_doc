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

# Exercise: A fixed point in a moving coordinate system

In {numref}`fig_geometry_basics_exercise`, the position of the elbow in the arm coordinate system is $(0, -0.5, 0)$.

Using Kinetics Toolkit's geometry module, express the position of the elbow in global coordinates for a movement of shoulder flexion of 0°, 5°, 10° and 15°.

a) Do this exercise by creating the corresponding homogeneous transform using [ktk.geometry.create_transforms](api/ktk.geometry.create_transforms.rst), then by multiplying this transform by the point coordinates using [ktk.geometry.matmul](api/ktk.geometry.matmul.rst).

```{code-cell} ipython3
:tags: [hide-cell]

import kineticstoolkit.lab as ktk
import numpy as np


p_elbow_ref_arm = np.array([[0.0, -0.5, 0.0, 1.0]])

T_arm = ktk.geometry.create_transforms(
    angles=[
        np.deg2rad(0.0),
        np.deg2rad(5.0),
        np.deg2rad(10.0),
        np.deg2rad(15.0),
    ],
    seq="z",
)

ktk.geometry.matmul(T_arm, p_elbow_ref_arm)
```

b) Do this exercise using the [ktk.geometry.rotate](api/ktk.geometry.rotate.rst) and [ktk.geometry.translate](api/ktk.geometry.translate.rst) function.

```{code-cell} ipython3
:tags: [hide-cell]
p_elbow_ref_arm = np.array([[0.0, -0.5, 0.0, 1.0]])

ktk.geometry.rotate(
    p_elbow_ref_arm,
    angles=[
        np.deg2rad(0.0),
        np.deg2rad(5.0),
        np.deg2rad(10.0),
        np.deg2rad(15.0),
    ],
    seq="z",
)
```
