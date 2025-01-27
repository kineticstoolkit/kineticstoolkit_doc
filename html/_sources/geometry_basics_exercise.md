# Exercise: Transform

{numref}`fig_geometry_basics_exercise` shows inclined local coordinate systems for both the upper arm and forearm. Knowing that the position of the elbow in global coordinates is $(0.34, 0.371, 0)$, and that the forearm is inclined by $50^\circ$ compared to the global reference frame, construct this 4x4 matrix: $^\text{global} _\text{forearm} T$.

```{figure-md} fig_geometry_basics_exercise
:width: 3in
![](_static/images/fig_geometry_basics_exercise.png)

Local coordinates for both the upper arm and the forearm.
```


:::{toggle}

$$
~^\text{global}_\text{forearm}T = \begin{bmatrix}
\cos(50) & -\sin(50) & 0 & 0.34 \\
\sin(50) & \cos(50) & 0 & 0.371 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix} \\=
\begin{bmatrix}
0.643 & -0.766 & 0 & 0.34 \\
0.766 & 0.643 & 0 & 0.371 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

:::
