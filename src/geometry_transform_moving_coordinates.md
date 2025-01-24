# Rotating and translating coordinates

We now know how to construct a transform, which is a 4x4 matrix that represents the position and orientation of a local coordinate system in respect to a reference coordinate system.

We learned that a transform always has this form:

$$
T =
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

In addition to representing positions and orientations, the same matrix can also represent rigid transformations such as translations and rotations, thus its name **homogeneous transform**. In this case:

- $R$ represents a rotation;
- $p$ is a translation.

Any coordinate (point, vector, or frame) that is multiplied by the homogeneous transform will be rotated by $R$ and translated by $p$:

$$
^\text{global} p_{\text{tranformed}} ~~~ = ~~~ T ~~~ ^\text{global} p_\text{initial}
$$

The following examples show how the same homogeneous transform can move either points, vectors, or frames.
