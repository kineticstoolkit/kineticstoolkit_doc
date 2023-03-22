---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Kinematic chains

:::{card} Summary
This section introduces the concept of kinematic chains, shows how it relates to homogeneous transforms, and how we can navigate between chain elements in Kinetics Toolkit.
:::

## 📄 Series of homogeneous transforms

Now that we understand how powerful homogeneous transforms are, we will take it one step further, and chain multiple transforms. We will start with the last example from section [](geometry_transform_changing_coordinate_system.md). We still know this information:

- the length of the upper arm is 38 cm;
- the shoulder is located 15 cm forward and 70 cm upward to the global origin;
- the upper arm is inclined at 30 degrees of the vertical.

to which we add:

- the length of the forearm is 34 cm;
- the elbow is flexed 20 degrees.

Based on this information, we want to calculate the position of the wrist in global coordinates.

![forearm_rotated -height:normal](_static/images/geometry_forearm_rotated.png)

*Figure 1. Local coordinates for both the upper arm and the forearm*

**Solution:**

The way to solve this problem is to see it as a chain of parent-child relations between coordinate systems (CS). Before solving this problem, let's consider the previous example in the form of a parent-child chain.

$$
\text{global CS} \rightarrow \text{upper arm CS} \rightarrow \text{elbow}
$$

- The position of the elbow was a child of the upper arm frame;
- The upper arm frame was a child of the global frame;

We solved $^\text{global}p_\text{elbow}$ by expressing:

1. the position of the elbow **in its parent frame**: $^\text{upper arm}p_\text{elbow}$;
2. the upper arm frame **in its parent frame**: $^\text{global}_\text{upper arm}T$.

and by using this equation.

$$
^\text{global}p_\text{elbow}
~~~=
~~~^\text{global}_\text{upper arm}T
~~~^\text{upper arm}p_\text{elbow}
$$


This new problem is similar, with the difference that we now have an additional chain:

$$
\text{global CS} \rightarrow \text{upper arm CS} \rightarrow \text{forearm CS} \rightarrow \text{wrist}
$$

- The position of the wrist is a child of the forearm frame:
- The forearm frame is a child of the upper arm frame;
- The upper arm frame is a child of the global frame;


We solve $^\text{global}p_\text{wrist}$ by expressing:

1. the position of the wrist **in its parent frame**: $^\text{forearm}p_\text{wrist}$;
2. the forearm frame **in its parent frame**: $^\text{upper arm}_\text{frame}T$;
3. the upper arm frame **in its parent frame**: $^\text{global}_\text{upper arm}T$.

This leads to this equation:

$$
^\text{global}p_\text{wrist}
~~~=
~~~^\text{global}_\text{upper arm}T
~~~^\text{upper arm}_\text{forearm}T
~~~^\text{forearm}p_\text{wrist}
$$

:::{tip}
Take a look at how using this notation, the upper and lower indices cancel out to give the final transformation.
:::

## 💪 Exercise

Develop the three terms of the equation above to solve this example. No need to try performing the matrix multiplication itself. Then toggle the solution below to verify your solution.

:::{toggle}

$$
^\text{forearm}p_\text{wrist} =
\begin{bmatrix}
0 \\ -0.34 \\ 0 \\ 1
\end{bmatrix}
$$

$$
^\text{upper arm}_\text{forearm}T =
\begin{bmatrix}
\cos(20) & -\sin(20) & 0 & 0 \\
\sin(20) & \cos(20) & 0 & -0.38 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

$$
^\text{global}_\text{upper arm}T =
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 0.15 \\
\sin(30) & \cos(30) & 0 & 0.7 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

:::

## 📄 Navigating between chain elements using Kinetics Toolkit

We already know enough functions of the [ktk.geometry](api/ktk.geometry.rst) module to solve this example. The first step is to create the known frames and positions:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

# position of the wrist in the forearm coordinate system
forearm_p_wrist = [[0, 0.34, 0, 1]]

# forearm frame in the upper arm coordinate system
upperarm_T_forearm = ktk.geometry.create_transforms(
    seq="z", angles=[20], translations=[[0, -0.38, 0]], degrees=True
)

# upper arm frame in the global coordinate system
global_T_upperarm = ktk.geometry.create_transforms(
    seq="z", angles=[30], translations=[[0.15, 0.7, 0]], degrees=True
)
```

One method to reach the final answer is to simply perform the multiplication using [ktk.geometry.matmul](api/ktk.geometry.matmul.rst):

```{code-cell} ipython3
global_p_wrist = ktk.geometry.matmul(
    global_T_upperarm, ktk.geometry.matmul(upperarm_T_forearm, forearm_p_wrist)
)

global_p_wrist
```

Another, equivalent method, is to iteratively expressing everything in global coordinates using [ktk.geometry.get_global_coordinates](api/ktk.geometry.get_global_coordinates.rst). We already defined the upper arm frame:

```{code-cell} ipython3
global_T_upperarm
```

Then we proceed with the forearm frame:

```{code-cell} ipython3
global_T_forearm = ktk.geometry.get_global_coordinates(
    local_coordinates=upperarm_T_forearm, reference_frames=global_T_upperarm
)

global_T_forearm
```

Then we proceed with the wrist:

```{code-cell} ipython3
global_p_wrist = ktk.geometry.get_global_coordinates(
    forearm_p_wrist, reference_frames=global_T_forearm
)

global_p_wrist
```
