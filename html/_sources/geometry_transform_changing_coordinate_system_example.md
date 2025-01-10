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

# Local to global coordinates example

This ability of switching between coordinate systems is very powerful. Let's get back to {numref}`fig_geometry_local_coordinates_rotated`.

Using this information:
1. the length of the upper arm is 38 cm;
2. the shoulder is located 15 cm forward and 70 cm upward to the global origin;
3. the upper arm is inclined at 30 degrees of the vertical.

We want to know the position of the elbow in global coordinates.

**Solution:**

The first information allows us to express the position of the elbow in the local upper arm coordinate system:

$$
~^\text{upper arm}p_\text{elbow} = \begin{bmatrix}
0 \\ -0.38 \\ 0 \\ 1
\end{bmatrix}
$$

The second and third informations allow us to express the upper arm frame:

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

Therefore, the position of the elbow in the global coordinate system is:

$$
^\text{global}p_\text{elbow}
~~~=
~~~^\text{global}_\text{upper arm}T
~~~^\text{upper arm}p_\text{elbow}
$$

$$
^\text{global}p_\text{elbow}
\\=
\begin{bmatrix}
0.866 & -0.5 & 0 & 0.15 \\
0.5 & 0.866 & 0 & 0.7 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
0 \\ -0.38 \\ 0 \\ 1
\end{bmatrix} \\=
\begin{bmatrix}
0.34 \\ 0.371 \\ 0 \\ 1
\end{bmatrix}
$$

Its global coordinates are $(0.34, 0.371, 0)$.

## Changing coordinate systems using Kinetics Toolkit

Using the [ktk.geometry.create_transform_series](api/ktk.geometry.create_transform_series.rst) and [ktk.geometry.matmul](api/ktk.geometry.matmul.rst) functions introduced in the previous section, we can solve this problem following:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

T_upperarm = ktk.geometry.create_transform_series(
    angles=[30], degrees=True, seq="z", positions=[[0.15, 0.7, 0]], 
)

local_p_elbow = [[0, -0.38, 0, 1]]

global_p_elbow = ktk.geometry.matmul(T_upperarm, local_p_elbow)

global_p_elbow
```

However, since changing coordinates from between reference frames is so common, Kinetics Toolkit also provides the functions [ktk.geometry.get_global_coordinates](api/ktk.geometry.get_global_coordinates.rst) and [ktk.geometry.get_local_coordinates](api/ktk.geometry.get_local_coordinates.rst). These functions are simple shortcuts but are easier to remember:

```{code-cell} ipython3
global_p_elbow = ktk.geometry.get_global_coordinates(
    local_coordinates=local_p_elbow, reference_frames=T_upperarm
)

global_p_elbow
```

```{code-cell} ipython3
local_p_elbow = ktk.geometry.get_local_coordinates(
    global_coordinates=global_p_elbow, reference_frames=T_upperarm
)

local_p_elbow
```
