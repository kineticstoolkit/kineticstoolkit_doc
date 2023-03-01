# Main points to remember

We will see in the next tutorial that Kinetics Toolkit's geometry module has several functions to ease the expression of coordinates from one coordinate system to another, to create frames and homogeneous transforms, etc. However, I believe it is important to remember these concepts, to understand how geometric data is represented and calculated.

- A point expresses a position in a given coordinate system, and is written as the 4x1 vector:

$$
\begin{bmatrix}
x \\ y \\ z \\ 1
\end{bmatrix}
$$

- A vector expresses a displacement, velocity, acceleration, force, etc., in a given coordinate system, and is written as the 4x1 vector:

$$
\begin{bmatrix}
x \\ y \\ z \\ 0
\end{bmatrix}
$$

- A frame expresses the orientation $R$ and position $P$ of a local coordinate system into a reference coordinate system, and is written as the 4x4 matrix:

$$
\begin{bmatrix}
R_{11} & R_{12} & R_{13} & P_x \\
R_{21} & R_{22} & R_{23} & P_y \\
R_{31} & R_{32} & R_{33} & P_z \\
0      & 0      & 0      & 1
\end{bmatrix}
$$

- An homogeneous transform expresses a rotation $R$ and translation $P$ from a given frame to another, and is written as the same 4x4 matrix:

$$
\begin{bmatrix}
R_{11} & R_{12} & R_{13} & P_x \\
R_{21} & R_{22} & R_{23} & P_y \\
R_{31} & R_{32} & R_{33} & P_z \\
0      & 0      & 0      & 1
\end{bmatrix}
$$
