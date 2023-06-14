
# Rotating and translating coordinates

In the previous section, we learned how to construct a frame: a 4x4 matrix that represents the position and orientation of a local coordinate system in respect to a reference coordinate system.

We learned that a frame always has this form:

$$
\begin{bmatrix}
R_{11} & R_{12} & R_{13} & P_x \\
R_{21} & R_{22} & R_{23} & P_y \\
R_{31} & R_{32} & R_{33} & P_z \\
0      & 0      & 0      & 1
\end{bmatrix}
$$

where:

- the $R$ sub-matrix is a function of three rotation angles and represents the orientation of the local coordinate system;
- the $P$ vector is the position of the local coordinate system's origin.

In addition to represent positions and orientations, the same matrix can also be represent rigid transformations such as translations and rotations. In this case, this matrix is called a **homogeneous transform**, and:

- the $R$ sub-matrix represents a rotation;
- the $P$ vector is a translation.

Any coordinate (point, vector or frame) that is multiplied by the homogeneous transform will be rotated by $R$ and translated by $P$:

$$
^\text{global} p_{\text{tranformed}} ~~~ = ~~~ T ~~~ ^\text{global} p_\text{initial}
$$

The following examples show how a same homogeneous transform can move either points, vectors or frames.
