# 3D angles

Single rotations such as the previous example are generally easy to understand. However, in 3d space, there are 3 rotation angles. It is helpful to consider rotations around orthogonal axes (e.g., x, y, z). We already know how to express a pure rotation of $\theta_z$ degrees around the z axis:

$$
T_z = \begin{bmatrix}
\cos(\theta_z) & -\sin(\theta_z) & 0 & 0 \\
\sin(\theta_z) & \cos(\theta_z) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Following the definition of a frame in section [](geometry_basics.md), we can also generate the two other rotation matrices:

$$
T_y = \begin{bmatrix}
\cos(\theta_y) & 0 & \sin(\theta_y) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta_y) & 0 & \cos(\theta_y) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

$$
T_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta_x) & -\sin(\theta_x) & 0 \\
0 & \sin(\theta_x) & \cos(\theta_x) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Now, let's say we want to rotate a point $p_\text{initial}$ by $\theta_x$ around the x axis, and by $\theta_y$ around the y axis. We may start by rotating the point around the x axis, then around the y axis. In this case, its final, rotated position, would be:

$$
p_\text{rotated} = T_y (T_x p_\text{initial}) = T_y T_x p_\text{initial}
$$

However, if we start by rotating the point around the y axis, then around the x axis, then we would get this final position instead:

$$
p_\text{rotated} = T_x (T_y p_\text{initial}) = T_x T_y p_\text{initial}
$$

Matrix multiplication is not commutative, which means $T_y T_x$ is not equal to $T_x T_y$. Therefore, **both rotation sequences do not perform the same total rotation.**

There are 24 different ways to express 3d rotations using series of 3 angles, with 12 being independent:

- 6 combinations of cardan angle sequences of intrinsic rotations
- 6 combinations of cardan angle sequences of extrinsic rotations
- 6 combinations of Euler angle sequences of intrinsic rotations
- 6 combinations of Euler angle sequences of extrinsic rotations


## Cardan angles

Also called Tait-Bryan angles, nautical angles, Heading/elevation/bank, or Yaw/pitch/roll, cardan angles express series of rotations around successive orthogonal axes: XYZ, XZY, YZX, YXZ, ZXY, and ZYX. Rotations can be either intrinsic or extrinsic.

**Intrinsic rotations** means that the coordinate system moves with the object being rotated. For instance, for a sequence of XYZ intrinsic rotations, the object is:

1. rotated around its x axis;
2. then around its new y axis that rotated with it during rotation 1;
3. then around its new z axis that rotated with it during rotations 1 and 2.

The animated figure below shows the six possible rotations using intrinsic cardan angles. In every case, the cube is rotated by 30 degrees around all axes: $\theta_x = \theta_y = \theta_z = 30^\circ$. The different final poses are only due to the different sequences of rotations.

<video autoplay controls muted loop>
<source src="_static/images/rotation_sequence_cardan_intrinsic.mp4" type="video/mp4">
</video>

*The six sequences of intrinsic cardan rotations (intrinsic = moving coordinate system)*

**Extrinsic rotations** means that the rotations are all performed around the initial coordinate system. For a sequence of XYZ intrinsic rotations, the object is:

1. rotated around its x axis;
2. then around the initial, unrotated y axis;
3. then around the initial, unrotated z axis.

The animated figure below shows the six possible rotations using extrinsic cardan angles. Again, the cube is rotated by 30 degrees around all axes.

<video autoplay controls muted loop>
<source src="_static/images/rotation_sequence_cardan_extrinsic.mp4" type="video/mp4">
</video>

*The six sequences of extrinsic Cardan rotations (extrinsic = fixed coordinate system)*


## Euler angles

Also called proper Euler angles, of classic Euler angles, Euler angles are different than cardan angles in that the first and third axes are the same. Again, rotations can be either intrinsic or extrinsic, as shown in the two figures below. As for both previous figures, every rotation is a rotation of 30 degrees around a given axis.

<video autoplay controls muted loop>
<source src="_static/images/rotation_sequence_euler_intrinsic.mp4" type="video/mp4">
</video>

*The six sequences of intrinsic Euler rotations (intrinsic = moving coordinate system)*

<video autoplay controls muted loop>
<source src="_static/images/rotation_sequence_euler_extrinsic.mp4" type="video/mp4">
</video>

*The six sequences of extrinsic Euler rotations (extrinsic = fixed coordinate system)*


:::{note}
Whereas we viewed 24 possibilities of rotation sequences, each intrinsic rotation as an equivalent extrinsic rotation: $\text{intrinsic}(\theta_1, \theta_2, \theta_3)$ = $\text{extrinsic}(\theta_3, \theta_2, \theta_1)$, which means that there is a total of 6 independent cardan angle sequences, and 6 independent Euler angle sequences.
:::
