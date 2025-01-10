---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Moving frames (transforms)

The orientation and position of a frame (defined as a coordinate system attached to a segment) is expressed by a [homogeneous transform](geometry_transforms.md). We remind that the first three columns are three vectors (the direction of three axes), and the fourth column is a point (the position of the origin). Therefore, since an homogeneous transform can move both points and vectors, then it can also move complete frames.

```{figure-md} fig_geometry_moving_frames
:width: 5in
![](_static/images/fig_geometry_moving_frames.png)

Rotating and translating a local frame in respect to the global reference frame.
```

Let's use the same homogeneous transform to rotate and translate the frame  $^\text{global} _\text{local-initial} F$ (which reads as *Frame 'local' in its initial pose, expressed in global coordinates*) as shown in {numref}`fig_geometry_moving_frames`.

$$
^\text{global} _\text{local-tranformed} F ~~~ = ~~~ T ~~~ ^\text{global} _\text{local-initial} F
$$

We first express the unrotated frame $^\text{global} _\text{local-initial} F$:

$$
^\text{global} _\text{local-initial} F
=
\begin{bmatrix}
\cos(0) & -\sin(0) & 0 & 10 \\
\sin(0) & \cos(0) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 & 10 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The transformed frame is calculated using:

$$
^\text{global} _\text{local-transformed} F
=
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 10 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\\=
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 10.66 \\
\sin(30) & \cos(30) & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$


## Application in Kinetics Toolkit

The transform $T$ is created using:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

T = ktk.geometry.create_transform_series(
    angles=[30],
    degrees=True,
    seq="z",  # Which means a rotation around the z axis
    positions=[[2.0, 0.0, 0.0, 1.0]],
)

T
```

The initial local frame is expressed as:

```{code-cell} ipython3
initial_frame = np.array(
    [
        [
            [1.0, 0.0, 0.0, 10.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
    ]
)
```

The rotated frame is:

```{code-cell} ipython3
ktk.geometry.matmul(T, initial_frame)
```

## Direct transformation in Kinetics Toolkit

We can also rotate and translate the initial frame using [ktk.geometry.rotate](api/ktk.geometry.rotate.rst) and [ktk.geometry.translate](api/ktk.geometry.translate.rst):

```{code-cell} ipython3
rotated_frame = ktk.geometry.rotate(
    initial_frame, seq="z", angles=[30], degrees=True
)
final_frame = ktk.geometry.translate(rotated_frame, [[2.0, 0.0, 0.0]])

final_frame
```
