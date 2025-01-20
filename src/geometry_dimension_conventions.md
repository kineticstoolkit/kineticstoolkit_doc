---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Expressing series of numbers, points, vectors and transforms in Kinetics Toolkit

In Kinetics Toolkit, numbers, points, vectors and transforms are expressed as series, where the first dimension of any series corresponds to time. This is emphasized in the following examples:

## Series of numbers (float, int)

Since a float or an integer has a no dimension, then a **series** of N floats of integers has one dimension of length N:

    [x(t0), x(t1), x(t2), ...]

For example:

```{code-cell} ipython3
series_of_floats = [1.0, 1.1, 1.2, 1.3]
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

## Series of points

Since a point has four coordinates (x, y, z, 1), then a **series** of N points has a shape of (N, 4):

    [
        [x(t0), y(t0), z(t0), 1.0],
        [x(t1), y(t1), z(t1), 1.0],
        [x(t2), y(t2), z(t2), 1.0],
        [ ... ,  ... ,  ... , ...],
    ]

The function [ktk.geometry.create_point_series](api/ktk.geometry.create_point_series.rst) creates such points series:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ktk.geometry.create_point_series(
    x=[1.0, 2.0, 3.0], y=[4.0, 5.0, 6.0], z=[7.0, 8.0, 9.0]
)
```

## Series of vectors

Since a vector has four coordinates (x, y, z, 0), then a **series** of N vectors has a shape of (N, 4):

    [
        [x(t0), y(t0), z(t0), 0.0],
        [x(t1), y(t1), z(t1), 0.0],
        [x(t2), y(t2), z(t2), 0.0],
        [ ... ,  ... ,  ... , ...],
    ]

The function [ktk.geometry.create_vector_series](api/ktk.geometry.create_vector_series.rst) creates such vector series:

```{code-cell} ipython3
ktk.geometry.create_vector_series(
    x=[1.0, 2.0, 3.0], y=[4.0, 5.0, 6.0], z=[7.0, 8.0, 9.0]
)
```

## Series of transforms

Since a transform has a shape of (4, 4), then a **series** of N frames has a shape of (N, 4, 4):

    [
        [
            [R00(t0), R01(t0), R02(t0), px(t0)],
            [R10(t0), R11(t0), R12(t0), py(t0)],
            [R20(t0), R21(t0), R22(t0), pz(t0)],
            [    0.0,     0.0,     0.0,    1.0],
        ],
        [
            [R00(t1), R01(t1), R02(t1), px(t1)],
            [R10(t1), R11(t1), R12(t1), py(t1)],
            [R20(t1), R21(t1), R22(t1), pz(t1)],
            [    0.0,     0.0,     0.0,    1.0],
        ],
        ...
    ]

The function [ktk.geometry.create_transform_series](api/ktk.geometry.create_transform_series.rst) can create transforms using multiple input forms. Although we will explore this function in more details later, here is how to express a series of transforms based on rotation angles:

```{code-cell} ipython3
# Create a series of 2 transforms that represent a rotation
# of 0°, then 1°, around z, and a position of (2, 3, 4), then
# (2, 3.1, 4).
ktk.geometry.create_transform_series(
    angles=[0, 1], seq="z", degrees=True, positions=[[2, 3, 4], [2, 3.1, 4]]
)
```

## Series of point clouds

We can express M points together as an array of shape (4, M):

$$
\begin{bmatrix}
x_0 & x_1 & x_2 & ... \\
y_0 & y_1 & y_2 & ... \\
z_0 & z_1 & z_2 & ... \\
1 & 1 & 1 & ...
\end{bmatrix}
$$

Therefore, a **series** of N point clouds has a shape of (N, 4, M):

    [
        [
            [x0(t0), x1(t0), x2(t0), ...],
            [y0(t0), y1(t0), y2(t0), ...],
            [z0(t0), z1(t0), z2(t0), ...],
            [   1.0,    1.0,    1.0, ...],
        ],
        [
            [x0(t1), x1(t1), x2(t1), ...],
            [y0(t1), y1(t1), y2(t1), ...],
            [z0(t1), z1(t1), z2(t1), ...],
            [   1.0,    1.0,    1.0, ...],
        ],
        ...
    }

The same applies for series of vector clouds.

## Time-invariant coordinates

Always ensure that the first dimension of any array is reserved to time, even for coordinates that do not vary in time. For example, the vector $[1, 2, 3, 0]$ must be expressed as `[[1.0, 2.0, 3.0, 0.0]]` (note the double brackets). Expressing it as `[1.0, 2.0, 3.0, 0.0]` (single brackets) would mean a series of 4 floats instead of one time-invariant vector.

A quick way to convert a constant array to a series is to use {{np_newaxis}}:

    one_vector = np.array([1.0, 2.0, 3.0, 0.0])
    series_of_one_vector = one_vector[np.newaxis]
:::
