---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# 2D angles

At the end of the example of section [](geometry_kinematic_chains.md), we had calculated the frames that express the orientation of both the upper arm ($^\text{global}_\text{upper arm} T$) and forearm ($^\text{global}_\text{forearm} T$) in global coordinates.

Let's see how we could extract the elbow flexion angle from those two frames.

The first step is to calculate the homogeneous transform from the upper arm to the forearm. This is the same as expressing the forearm frame in reference to the upper arm frame.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

# Upper arm and forearm frames, expressed in global coordinates
# (calculated in last example):
global_T_upperarm = np.array(
    [
        [
            [0.8660254, -0.5, 0.0, 0.15],
            [0.5, 0.8660254, 0.0, 0.7],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
    ]
)

global_T_forearm = np.array(
    [
        [
            [0.64278761, -0.76604444, 0.0, 0.34],
            [0.76604444, 0.64278761, 0.0, 0.37091035],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
    ]
)

# Express the forearm frame in local upper arm coordinates
upperarm_T_forearm = ktk.geometry.get_local_coordinates(
    global_T_forearm, global_T_upperarm
)

upperarm_T_forearm
```

In section [](geometry_basics.md), we expressed the generic form of a 2d frame in the xy plane:

$$
~^\text{upper arm}_\text{forearm}T = \begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 & x \\
\sin(\theta) & \cos(\theta) & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Here, $\theta$ corresponds to the flexion angle of the elbow. To extract θ from the resulting $^\text{upper arm}_\text{forearm}T$ matrix, we use simple trigonometric relations:

$$
\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)} = \frac{T_{21}}{T_{11}} = \frac{0.34202}{0.93970}
$$

$$
\theta = \text{atan2}(y=0.93970, x=0.36396) \\= 20^\circ
$$

We could also use Kinetics Toolkit's function [ktk.geometry.get_angles](api/ktk.geometry.get_angles.rst) to extract this angle automatically:

```{code-cell} ipython3
elbow_angles = ktk.geometry.get_angles(
    upperarm_T_forearm, seq="xyz", degrees=True
)

elbow_angles
```
