# Points and vectors

Using the global coordinate system of {numref}`fig_geometry_global_coordinates`, we can express the position of any point in space using its three components (x, y, z). For example, the position of the shoulder in global coordinates is:

$$
~^\text{global}p_\text{shoulder} = \begin{bmatrix}
x_\text{shoulder} \\
y_\text{shoulder} \\
z_\text{shoulder}
\end{bmatrix}
$$

where $~^\text{global}p_\text{shoulder}$ is read as: Position ($p$) of the shoulder expressed in the global coordinate system.

While three components are sufficient to express points and vectors in three dimensions, we normally use four components instead, the fourth being 1 for points and 0 for vectors. Therefore, while we express the **position** (a point) of the shoulder in global coordinates as:

$$
~^\text{global}p_\text{shoulder} = \begin{bmatrix}
x_\text{shoulder} \\
y_\text{shoulder} \\
z_\text{shoulder} \\ 1
\end{bmatrix}
$$

we would express its **velocity** (a vector) as:

$$
~^\text{global}\vec{v}_\text{shoulder} = \begin{bmatrix}
v_\text{x shoulder} \\
v_\text{y shoulder} \\
v_\text{z shoulder} \\ 0
\end{bmatrix}
$$