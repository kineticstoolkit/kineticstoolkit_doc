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

# Rotating vectors

For this second example, let's apply this same transform to a vector of 10 units toward the x-axis (10, 0, 0) as shown in {numref}`fig_geometry_moving_vectors`.

```{figure-md} fig_geometry_moving_vectors
:width: 4in
![](_static/images/fig_geometry_moving_vectors.png)

Rotating a vector in respect to the global reference frame.
```


The same equation applies:

$$
^\text{global} \vec{v}_{\text{tranformed}} ~~~ = ~~~ T ~~~ ^\text{global} \vec{v}_\text{initial}
$$

Although vector $\vec{v}_\text{initial}$ shares the same coordinates as $p_\text{initial}$ in the previous example, it is written differently (with a 0 instead of a 1 in the fourth coordinate). This is because the fourth element is responsible for translations, and contrary to a point, a vector cannot be translated.

$$
^\text{global} \vec{v}_\text{initial} =
\begin{bmatrix}
10 \\ 0 \\ 0 \\ 0
\end{bmatrix}
$$

We multiply this vector by the transform to obtain the final vector:

$$
^\text{global} \vec{v}_{\text{tranformed}} =
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 10 \\ 0 \\ 0 \\ 0 \end{bmatrix} \\ =
\begin{bmatrix} 10\cos(30) \\ 10\sin(30) \\ 0 \\ 0 \end{bmatrix} =
\begin{bmatrix} 8.66 \\ 5 \\ 0 \\ 0 \end{bmatrix}
$$

The final coordinates of the vector are (8.66, 5, 0).


## Application in Kinetics Toolkit

The transform $T$ can be created using:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

T = ktk.geometry.create_transform_series(
    angles=[30],
    degrees=True,
    seq="z",  # Which means a rotation around the z axis
)

T
```

The rotated vector is:

```{code-cell} ipython3
ktk.geometry.matmul(T, [[10, 0, 0, 1]])
```

## Direct transformation in Kinetics Toolkit

We can also rotate the vector directly using [ktk.geometry.rotate](api/ktk.geometry.rotate.rst):

```{code-cell} ipython3
ktk.geometry.rotate([[10, 0, 0, 0]], seq="z", angles=[30], degrees=True)
```
