---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# 📖 Arithmetics and comparisons

:::{card} Summary
This section shows how to perform arithmetic operations and comparisons between arrays, or between arrays and numbers. It also introduces:

- Special constants:
    - {{np_pi}}
    - {{np_inf}}
    - {{np_nan}}
- Trigonometric functions:
    - {{np_sin}}, {{np_cos}}, {{np_tan}}
    - {{np_arcsin}}, {{np_arccos}}, {{np_arctan}}, {{np_arctan2}}
    - {{np_deg2rad}}, {{np_rad2deg}}
    - {{np_abs}}
    - {{np_sqrt}}
- Statistical functions:
    - {{np_sum}}, {{np_nansum}}
    - {{np_mean}}, {{np_nanmean}}
    - {{np_std}}, {{np_nanstd}}
    - {{np_min}}, {{np_nanmin}}
    - {{np_max}}, {{np_nanmax}}
    - {{np_median}}, {{np_nanmedian}}
    - {{np_quantile}}, {{np_nanquantile}}
:::

## 📄 Basic arithmetics

All Python operators (`+`, `-`, `*`, `/`, `**`) work on NumPy arrays, assuming both arrays have the same shape. The operation is performed between every element of a same position. For example:

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

a = np.array(
    [
        [1.0, 2.0, 3.0],
        [1.0, 2.0, 3.0],
    ]
)

b = np.array(
    [
        [1.0, 1.0, 1.0],
        [2.0, 2.0, 2.0],
    ]
)
```

Addition:

```{code-cell} ipython3
a + b
```

Subtraction:

```{code-cell} ipython3
a - b
```

Multiplication:

```{code-cell} ipython3
a * b
```

Division:

```{code-cell} ipython3
a / b
```

Exponent:

```{code-cell} ipython3
a**b
```

It is also possible to perform operations between an array and a float or an integer.

Addition:

```{code-cell} ipython3
a + 1
```

Subtraction:

```{code-cell} ipython3
a - 1
```

etc.

:::{note}
It is also possible to perform arithmetic operations between arrays that do not completely match shape using {{np_broadcasting}} (not seen in this tutorial).
:::

## 💪 Exercise 1

A ball is released from a point in air. Knowing that it was immobile when it was released, and that it gains negative speed at a rate of 9.81 m/s², plot a curve of its velocity during one second from release time.

![Exercise 1 -height:short](_static/images/ball_vertical_speed.png)

::::{tip}
:::{toggle}
Start by creating a time array using {{np_arange}} or {{np_linspace}}. Then, use this time array to create a velocity array.
:::
::::

```{code-cell} ipython3
:tags: [hide-cell]

# First, let's define a time array
t = np.linspace(0, 1, 100, endpoint=False)

# Calculate the velocity as -9.81 * t
v = -9.81 * t

# Show it
plt.plot(t, v)
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.show()
```

## 📄 Matrix multiplication

Numpy also provides an operator `@` that calculates the matrix dot product. For instance, to perform this operation:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\begin{bmatrix}
1 \\ 2 \\ 3
\end{bmatrix}
$$

which is:

$$
\begin{bmatrix}
(1 * 1) + (2 * 2) + (3 * 3)\\
(4 * 1) + (5 * 2) + (6 * 3)\\
(7 * 1) + (8 * 2) + (9 * 3)
\end{bmatrix}
=
\begin{bmatrix}
14 \\ 32 \\ 50
\end{bmatrix}
$$

we simply write:

```{code-cell} ipython3
a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
    ]
)

b = np.array([1.0, 2.0, 3.0])

a @ b
```

## 📄 Comparisons

Comparison operators also work natively on NumPy arrays. For example:

```{code-cell} ipython3
a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
    ]
)

a > 5.0
```

```{code-cell} ipython3
a == 5.0
```

```{code-cell} ipython3
a >= 5.0
```

## 📄 Infinity and Not-A-Number (nan)

Some arithmetic operations such as division by zero lead to infinity of undertermined numbers, which normally result in an error:

```{code-cell} ipython3
:tags: [raises-exception]

1 / 0
```

Since an operation on arrays performs many operations at once, it would be inconvenient to get an error each time only a few calculations failed. For this matter, instead of generating errors, NumPy only warns and provides special constants to express infinity {{np_inf}} and undetermined numbers {{np_nan}} (not-a-number):

```{code-cell} ipython3
a = np.array([0.0, 1.0, -1.0, 1.0])
b = np.array([0.0, 0.0, 0.0, 1.0])

c = a / b

c
```

To know which operations resulted in `nan` or `inf`, we use {{np_isnan}} and {{np_isinf}}:

```{code-cell} ipython3
np.isnan(c)
```

```{code-cell} ipython3
np.isinf(c)
```

:::{note}
It is common in data analysis to use `np.nan` to indicate missing data. For instance, we could record the (x, y, z) trajectory of a reflective marker and use (`nan`, `nan`, `nan`) when the marker is not seen by the cameras.
:::

## 📄 Trigonometry

In addition to arithmetical operators, NumPy provides lots of essential functions and constants to perform trigonometrical operations:

- {{np_pi}}: π
- {{np_sin}}: Sinus
- {{np_cos}}: Cosinus
- {{np_tan}}: Tangent
- {{np_arcsin}}: Arc-sinus
- {{np_arccos}}: Arc-cosinus
- {{np_arctan}}: Arc-tangent
- {{np_arctan2}}: Art-tangent in the full plane, contrarily to {{np_arctan}} that only returns values from -π/2 (-90°) to +π (+90°)
- {{np_deg2rad}}: Convert degrees to radians
- {{np_rad2deg}}: Convert radians to degrees
- {{np_abs}}: Absolute value
- {{np_sqrt}}: Square root

In all trigonometric functions, angles are in radians by default. You can either convert to/from degrees by multiplying or dividing by $\pi/180$ manually, or use {{np_deg2rad}} and {{np_rad2deg}}.

```{code-cell} ipython3
angle = np.linspace(0, 2 * np.pi, 100)

plt.plot(angle, np.sin(angle))
plt.show()
```


## 💪 Exercise 2

A ball is threw horizontally with a constant horizontal velocity of 10 m/s, and with no initial vertical velocity at release time. Once released, its horizontal velocity stays constant while its vertical velocity increases negatively at a rate of 9.81 m/s². Plot a curve of its total speed during one second from release time. The total speed is the norm of the vector created by the horizontal velocity and the vertical velocity:

![Exercise 2 -height:short](_static/images/ball_total_speed.png)

::::{tip}
:::{toggle}
You already calculated the vertical velocity `v_y` in the previous exercise. Now use the Pythagorean theorem using arithmetic operations on arrays to calculate the total speed `v_total` based on `v_x` and `v_y`.
:::
::::

```{code-cell} ipython3
:tags: [hide-cell]

# First, let's define a time array
t = np.linspace(0, 1, 100, endpoint=False)

# Calculate the vertical velocity as -9.81 * t
v_y = -9.81 * t

# Constant horizontal speed of 10 m/s2
v_x = 10

# Calculate the total speed
v_total = np.sqrt(v_x**2 + v_y**2)

# Plot it
plt.plot(t, v_total)
plt.xlabel("Time (s)")
plt.ylabel("Total speed (m/s)")
plt.grid()
plt.show()
```


## 💪 Exercise 3

When we walk on an inclined treadmill, we must overcome a backward force equal to:

$$
F = m g \sin \theta
$$

where $m$ is the person's mass, $g$ is 9.81 m/s² and $\theta$ is the treadmill angle. Write a function that takes the mass as an argument, and that plots $F$ for $\theta \in [-20, 20]$ degrees. Then, test your function for $m = 65$ kg.

![Exercise 3 -height:short](_static/images/gait_inclined.png)

```{code-cell} ipython3
:tags: [hide-cell]

def plot_force(m: float) -> None:
    """
    Plot the force a persons need to overcome on an inclined treadmill.

    Parameters
    ----------
    m :
        Mass of the person in kilograms

    Returns
    -------
    None

    """
    # First, let's define an angle array
    theta = np.linspace(-30, 30, 100, endpoint=False)

    # Calculate the force
    force = m * 9.81 * np.sin(np.deg2rad(theta))

    # Plot it
    plt.plot(theta, force)
    plt.xlabel("Angle (deg)")
    plt.ylabel("Force (N)")
    plt.show()


# Test the function
plot_force(65)
```

## 📄 Statistical functions

NumPy also provides statistical functions such as {{np_sum}}, {{np_mean}}, {{np_std}}, {{np_min}}, {{np_max}}, {{np_median}}, and {{np_quantile}}. For multidimensional arrays, these functions accept an `axis` parameter that indicates on which axis to perform the operation. For example, for a matrix, an operation on the first axis is performed on the **lines**, so that we get a result for each column.

```{code-cell} ipython3
a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
    ]
)

print(f"Sum on first axis = {np.sum(a, axis=0)}")
print(f"Max on first axis = {np.max(a, axis=0)}")
```

Whereas an operation on the second axis is performed on the **columns**, so that we get a result for each line:

```{code-cell} ipython3
print(f"Sum on second axis = {np.sum(a, axis=1)}")
print(f"Max on second axis = {np.max(a, axis=1)}")
```

If the array contains `nan` values, using these functions can be problematic because any arithmetic operation that includes a `nan` results in a `nan`:

```{code-cell} ipython3
a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, np.nan, 6.0],
    ]
)

print(f"Sum on first axis = {np.sum(a, axis=0)}")
print(f"Max on first axis = {np.max(a, axis=0)}")
```

For these cases, NumPy provides alternate functions: {{np_nansum}}, {{np_nanmean}}, {{np_nanstd}}, {{np_nanmin}}, {{np_nanmax}}, {{np_nanmedian}}, {{np_nanquantile}} that ignore `nan` values from the calculation.

```{code-cell} ipython3
print(f"Sum on first axis = {np.nansum(a, axis=0)}")
print(f"Max on first axis = {np.nanmax(a, axis=0)}")
```
