---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]
%matplotlib inline
```

# Dimension conventions

In the [](api/ktk.geometry.rst) module and in most of Kinetics Toolkit's module:

- Every point, vector or matrix, and in many case even scalar, is considered as a **series**.
- The first dimension of any series corresponds to **time**.

This is emphasized in the following examples:

## Series of scalars

```
[x(t0), x(t1), x(t2), ...]
```


## Series of points

```
[
    [x(t0), y(t0), z(t0), 1.0],
    [x(t1), y(t1), z(t1), 1.0],
    [x(t2), y(t2), z(t2), 1.0],
    [ ... ,  ... ,  ... , ...],
] 
```

## Series of vectors

```
[
    [x(t0), y(t0), z(t0), 0.0],
    [x(t1), y(t1), z(t1), 0.0],
    [x(t2), y(t2), z(t2), 0.0],
    [ ... ,  ... ,  ... , ...],
] 
```

## Series of point clouds

```
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
```

## Series of frames or homogeneous transforms

```
[
    [
        [R00(t0), R01(t0), R02(t0), Tx(t0)],
        [R10(t0), R11(t0), R12(t0), Ty(t0)],
        [R20(t0), R21(t0), R22(t0), Tz(t0)],
        [    0.0,     0.0,     0.0,    1.0],
    ],
    [
        [R00(t1), R01(t1), R02(t1), Tx(t1)],
        [R10(t1), R11(t1), R12(t1), Ty(t1)],
        [R20(t1), R21(t1), R22(t1), Tz(t1)],
        [    0.0,     0.0,     0.0,    1.0],
    ],
    ...
}
```



## Working with constants

Since most signals in Kinetics Toolkit as considered as a series, always ensure that the first dimension of any array is reserved to time. For example, the vector (x = 1, y = 2, z = 3) must be expressed as `np.array([[1.0, 2.0, 3.0, 0.0]])` (note the double brackets). A common error would be to express it as `np.array([1.0, 2.0, 3.0, 0.0])` (single brackets), which would mean a series of 4 floats instead of one constant vector.

A quick way to convert a constant array to a series is to use numpy's `newaxis`:

```{code-cell} ipython3
import numpy as np

one_matrix = np.eye(4)
one_matrix
```

```{code-cell} ipython3
series_of_one_matrix = one_matrix[np.newaxis]
series_of_one_matrix
```

## First example with the geometry module

Now that we presented the conventions for expressing coordinates and transforms as series, we are ready to redo the last example from the last section, this time using Kinetics Toolkit.

![humerus_frame -height:normal](_static/images/humerus_frame.png)
Figure 1. Position and orientation of the humerus.

We know the lenght of the arm is 38 cm, and we want to express the position of the elbow in the global coordinate system. The shoulder is located 15 cm forward and 70 cm upward to the global origin and the humerus is inclined at 30 degrees of the vertical.

First, let's express the elbow position in the humerus coordinate system.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

local_elbow_position = np.array([[0, -0.38, 0, 1]])

local_elbow_position
```

Now, we create the frame representing the position and orientation of the humerus coordinate system. Since we know these position and orientation, then we will create this frame as an homogeneous transform from the global to the humerus coordinate system, using the [](api/ktk.geometry.create_transforms.rst) function:

```{code-cell} ipython3
humerus_frame = ktk.geometry.create_transforms(
    seq="z", angles=[np.deg2rad(30)], translations=[[0.15, 0.70, 0]]
)

humerus_frame
```

Now we can express the local elbow position in the global coordinate system:

```{code-cell} ipython3
ktk.geometry.get_global_coordinates(local_elbow_position, humerus_frame)
```
