# Mapping local coordinates to global coordinates

Let's start with this example, where we want to express the yellow point in global coordinates.

```{figure-md} fig_geometry_change_coordinate_system
:width: 4in
![](_static/images/fig_geometry_change_coordinate_system.png)

Expressing a local point in global coordinates.
```

The unknown is the yellow point's coordinates in respect to the global frame:

$$
^\text{global}p = \text{?}
$$

Instead of considering point $p$ as a point in its own local coordinate system, let's imagine that it was first expressed in the global reference frame ($^\text{global} p_\text{initial}$). Then, it was rotated by 30 degrees around the origin, then translated by (7, 5, 0) to reach its final position ($^\text{global} p_\text{transformed}$):


```{figure-md} fig_geometry_transformation_sequence
:width: 8in
![](_static/images/fig_geometry_transformation_sequence.png)

Transformation sequence from local coordinates to global coordinates.
```

This operation is expressed by:

$$
^\text{global} p_\text{transformed}
~~~ =
~~~ T
~~~ ^\text{global}p_\text{initial}
$$

These two ways of seing this problem are completely equivalent:

| Local point in global coordinates (Fig. 1)                                  | Rotating/translating a point (Fig. 2)                                            |
| :-------------------------------------------------------------------------: | :------------------------------------------------------------------------------: |
| $^\text{global}p ~~~ = ~~~ ^\text{global}_\text{local}T ~~~ ^\text{local}p$ | $^\text{global} p_\text{transformed} = ~~~ T ~~~ ^\text{global}p_\text{initial}$ |
| $^\text{global}p$                                                           | $^\text{global} p_\text{transformed}$                                            |
| $^\text{global}_\text{local}T$                                              | $T$                                                                              |
| $^\text{local}p$                                                            | $^\text{global}p_\text{initial}$                                                 |


See how the left equation allows passing from local coordinates to global coordinates!

We know the yellow point's coordinate (2, 1, 0) in respect to the local frame:

$$
^\text{local}p = \begin{bmatrix}
2 \\ 1 \\ 0 \\ 1
\end{bmatrix}
$$

We also know how to express the local frame:

$$
~^\text{global}_\text{local}T = \begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 7 \\
\sin(30) & \cos(30) & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Therefore:

$$
^\text{global}p
=
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 7 \\
\sin(30) & \cos(30) & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\ 1 \\ 0 \\ 1
\end{bmatrix}
\\ =
\begin{bmatrix}
0.866 & -0.5 & 0 & 7 \\
0.5 & 0.866 & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\ 1 \\ 0 \\ 1
\end{bmatrix}
=
\begin{bmatrix}
8.232 \\ 6.866 \\ 0 \\ 1
\end{bmatrix}
$$

The position of the yellow points, in global coordinates, is (8.232, 6.866, 0).
