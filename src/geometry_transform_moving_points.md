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

# Moving points

Let say we want to rotate the point located at (10, 0, 0) by 30 degrees around the origin's z axis, then translate it 2 units to the right:

```{figure-md} fig_geometry_moving_points
:width: 4in
![](_static/images/fig_geometry_moving_points.png)

Rotating and translating a point in respect to the global reference frame.
```

We first express the original coordinates of the point:

$$
^\text{global} p_\text{initial} =
\begin{bmatrix}
10 \\ 0 \\ 0 \\ 1
\end{bmatrix}
$$

We then express the rotation and translation that we want to apply to this point:

$$
T =
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

We multiply the position to the transform to obtain the final position of the point:

$$
^\text{global} p_{\text{tranformed}} =
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 10 \\ 0 \\ 0 \\ 1 \end{bmatrix} \\ =
\begin{bmatrix} 10\cos(30) + 2 \\ 10\sin(30) \\ 0 \\ 1 \end{bmatrix} =
\begin{bmatrix} 10.66 \\ 5 \\ 0 \\ 1 \end{bmatrix}
$$

The final coordinates of the points are (10.66, 5, 0).


## Application in Kinetics Toolkit

We can do the same in Kinetics Toolkit, using the function [ktk.geometry.create_transforms](api/ktk.geometry.create_transforms.rst) that creates series of homogeneous transforms based on angles and translations. For instance, the transform $T$ used in this section can be created using:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

T = ktk.geometry.create_transforms(
    seq="z",  # Which means a rotation around the z axis
    angles=[30],
    translations=[[2, 0, 0]],
    degrees=True,
)

T
```

:::{caution}
Note that the `angles` and `translations` values are enclosed in bracket. Similarly, the return transformed $T$ is also enclosed in an additional first dimension. This is because all functions in the [](api/ktk.geometry.rst) module work on series of data, and the first dimensions is always reserved to time. Please consult [this section](geometry_dimension_conventions.md) for more information.
:::

The function [ktk.geometry.matmul](api/ktk.geometry.matmul.rst) performs matrix multiplications on data series. It can therefore be used to obtain the solution to the previous examples.

```{code-cell} ipython3
ktk.geometry.matmul(T, [[10, 0, 0, 1]])
```

## Direct movement in Kinetics Toolkit

Kinetics Toolkit's geometry module also provides simpler function to provide basic geometry operations, such as [ktk.geometry.rotate](api/ktk.geometry.rotate.rst), [ktk.geometry.translate](api/ktk.geometry.translate.rst) and [ktk.geometry.scale](api/ktk.geometry.scale.rst). If we don't need to express a full homogeneous transform, then we can use these simpler functions:

```{code-cell} ipython3
point = [[10, 0, 0, 1]]
rotated_point = ktk.geometry.rotate(point, seq="z", angles=[30], degrees=True)
final_point = ktk.geometry.translate(rotated_point, translations=[[2, 0, 0]])

final_point
```
