# Transforms

We are now ready to introduce the **homogeneous transform**, a 4x4 matrix that expresses both the position and the orientation of a coordinate system, in reference to another coordinate system.

The fourth (easiest) column of a transform is the position of the local coordinate system's origin expressed in the reference coordinate system. In the example of Figure 4, this is:

$$
~^\text{global}p_\text{upper arm} = \begin{bmatrix}
x_\text{upper arm} \\
y_\text{upper arm} \\
z_\text{upper arm} \\
1
\end{bmatrix}
$$

The first three columns of a transform express the orientation of the coordinate system into the reference coordinate system. They are, in the reference coordinate system, the coordinates of three unit vectors that are respectively oriented toward the x, y and z axes of the local coordinate system.

```{figure-md} fig_geometry_frame
:width: 4in
![](_static/images/fig_geometry_frame.png)

Orientation of the upper arm coordinate system (bold lines) in reference to the global coordinate system (thin lines).
```

Based on {numref}`fig_geometry_frame`, which illustrates this concept for the pose of {numref}`fig_geometry_local_coordinates_rotated`, here is how we would express these three unit vectors in both coordinate systems:

|                  |        In the upper arm coordinate system        |                     In the global coordinate system                     |
| ----------------:|:------------------------------------------------:|:-----------------------------------------------------------------------:|
| Upper arm x axis | $\begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}$ | $\begin{bmatrix} \cos(\theta) \\ \sin(\theta) \\ 0 \\ 0 \end{bmatrix}$  |
| Upper arm y axis | $\begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}$ | $\begin{bmatrix} -\sin(\theta) \\ \cos(\theta) \\ 0 \\ 0 \end{bmatrix}$ |
| Upper arm z axis | $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}$ |            $\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}$             |

Combining these four vectors into a single 4x4 matrix gives the transform $~^\text{global}_\text{upper arm}T$:

$$
~^\text{global}_\text{upper arm}T = \begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 & x_\text{upper arm} \\
\sin(\theta) & \cos(\theta) & 0 & y_\text{upper arm} \\
0 & 0 & 1 & z_\text{upper arm} \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

where the expression $~^\text{global}_\text{upper arm}T$ is read as: Position and orientation of the upper arm coordinate system, expressed in the global coordinate system.

For example, if the shoulder is located 15 cm forward and 70 cm upward to the global origin, and the upper arm is inclined at 30 degrees of the vertical, then the position and orientation of the upper arm coordinate system is expressed by the transform:

$$
~^\text{global}_\text{upper arm}T = \begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 0.15 \\
\sin(30) & \cos(30) & 0 & 0.7 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix} \\=
\begin{bmatrix}
0.866 & -0.5 & 0 & 0.15 \\
0.5 & 0.866 & 0 & 0.7 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

:::{important}
Independently of the position and orientation of the studied body, a transform always has this form:

$$
\begin{bmatrix}
R_{11} & R_{12} & R_{13} & p_x \\
R_{21} & R_{22} & R_{23} & p_y \\
R_{31} & R_{32} & R_{33} & p_z \\
0      & 0      & 0      & 1
\end{bmatrix}
$$

where:

- $R$ is a function of three rotation angles and represents the orientation of the local coordinate system;
- $p$ is the position of the local coordinate system's origin.
:::
