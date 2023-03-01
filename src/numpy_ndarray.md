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

# 📖 Arrays

:::{card} Summary
This section presents the NumPy {{ndarray}} and its differences and similarities to the list. It also show how to create arrays of different shapes using:

- {{np_array}}
- {{np_zeros}}
- {{np_ones}}
- {{np_linspace}}
- {{np_arange}}
:::

Most NumPy operations are performed on arrays. An array is similar to a list but has fundamental differences:

| Lists                                                                                                                                             | Arrays                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Can be a sequence of different types, which makes them very versatile.                                                                            | Only hold element of the same type, which provides homogeneity.                                         |
| Have a dynamic size: it can be modified using `append`, `expand` and `pop`.                                                                       | We can't "grow" an array as we do with lists.                                                           |
| Only hold data, they don't provide methods to compute data.                                                                                       | Can be used directly for calculations such as linear algebra, filtering, etc.                           |
| Are only unidimensional. We can use nested lists to simulate multiple dimensions, but these values are harder to access, calculate, reshape, etc. | Can have any number of dimensions. It can represent and calculate matrices, or even series of matrices. | 

Lists and arrays are both useful and they can be converted one to the other.

## 📄 Dimensions

### One dimension

A simple way to create an array from a list is to use the {{np_array}} function:

```{code-cell} ipython3
import numpy as np

array_1d = np.array([0.1, 0.2, 0.3])

array_1d
```

It is also possible to convert back an array to a list, using its {{ndarray_tolist}} method:

```{code-cell} ipython3
array_1d.tolist()
```

Since a list is unidimensional, the resulting array is also unidimensional. We get the size (shape) of an array using its {{ndarray_shape}} property:

```{code-cell} ipython3
array_1d.shape
```

This tuple has only **1** value and this value is **3**, which means the array has a length of **3** on **1** axis. For unidimensional arrays, both {{ndarray_shape}} and Python's `len` keyword have very similar meanings:

```{code-cell} ipython3
len(array_1d)
```

:::{note}
NumPy's documentation usually refer to **axis** to denote a **dimension**. Both terms refer to the same thing.
:::

### More dimensions

We can create a 2d array using nested lists:

```{code-cell} ipython3
array_2d = np.array(
    [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
    ]
)

array_2d
```

Its shape is:

```{code-cell} ipython3
array_2d.shape
```

which means it has a length of 2 on its first axis, and 3 on its second axis. In other words, this is a 2x3 matrix.

We can even create arrays with more axes:

```{code-cell} ipython3
array_3d = np.array(
    [
        [
            [0.1, 0.2, 0.3],
            [0.4, 0.5, 0.6],
        ],
        [
            [0.7, 0.8, 0.9],
            [1.1, 1.2, 1.3],
        ],
    ]
)

array_3d
```

Its shape is:

```{code-cell} ipython3
array_3d.shape
```

which means it is a series of two 2x3 matrices.

## 📄 Creating an array

We just learned how to create unidimensional arrays using lists, and multidimensional arrays using nested lists. We can also create arrays using common NumPy functions.

### Zeros and ones

To create arrays filled with zeros or ones, we use the {{np_zeros}} and {{np_ones}} functions, which both take the shape of the array to create:

```{code-cell} ipython3
np.zeros((2, 5))
```

```{code-cell} ipython3
np.ones((3, 4))
```

:::{tip}
Note the double parenthesis. The argument to {{np_zeros}} and {{np_ones}} is a shape, which is a tuple. Writing `np.zeros(2, 5)` would generate an error, since this is not one tuple argument, but two integer arguments.
:::

### Linear spacing: `np.arange`

It is very common to generate unidimensional arrays of equally spaced values, such as `[0, 1, 2, 3, 4]` or `[0, 0.1, 0.2, 0.3]`. We could do it using:

```{code-cell} ipython3
np.array(range(5))
```

which creates a range from 0 (incl.) to 5 (excl.), then converts this range to an array. NumPy provides a shortcut for it: {{np_arange}}

```{code-cell} ipython3
np.arange(5)
```

This function takes the same arguments as the Python's [range](python_for_range.md) function.

:::{good-practice} np.arange
While `range` only takes integers as arguments, `np.arange` also accepts floats. For example:

```
np.arange(0, 0.5, 0.1)
```

generates:

```
array([0. , 0.1, 0.2, 0.3, 0.4])
```

However, this practice is not recommended due to potential floating point problems that can generate surprising results. Without going further into these issues, just remind that in most cases, `np.arange` should be used only with integers. For the example above:

```
np.arange(5) / 10
```

is safer and gives the same result:

```
array([0. , 0.1, 0.2, 0.3, 0.4])
```
:::

### Linear spacing: `np.linspace`

Another function to create equally spaced series of float is {{np_linspace}}, which takes as arguments the initial value, the final value, and the number of points in the new array. By default, `np.linspace` includes both the initial and final values. For example, to create an array that goes from 5.0 (included) to 10.0 (included) and that contains 11 elements:

```{code-cell} ipython3
np.linspace(5.0, 10.0, 11)
```

To exclude the final value, we set the `endpoint` argument to False.

```{code-cell} ipython3
np.linspace(5.0, 10.0, 10, endpoint=False)
```

## 💪 Exercise 1

We recorded the force measured by a dynamometer at a sampling frequency of 100 Hz, during 2.5 seconds. Using one line of code (excluding the `import` line), create a NumPy array named `time`, that represents the time at which every measurement was recorded. The first element of this array will be 0 s., the second will be 0.01 s., etc.

```{code-cell} ipython3
:tags: [hide-cell]

# The initial time is 0 s
# The final time corresponds to 2.5 seconds
# The number of points is 2.5 * 100Hz = 250.

time = np.linspace(0, 2.5, 250, endpoint=False)

# Note that if we understand the question as if the final time should be included,
# then we need to increase the number of points by 1 to include this new points:
# >> time = np.linspace(0, 2.5, 251)

time
```

## 💪 Exercise 2

Unfortunately, during the experiment of exercise 1, the dynamometer was not plugged in, and you only recorded a series of zero. Using one line of code, create a NumPy array named `force` that is the same shape as `time`, but that only contains zeros.

```{code-cell} ipython3
:tags: [hide-cell]

# We use the shape of `time` to create an array filled with zeros.

force = np.zeros(time.shape)

force
```

## 💪 Exercise 3

With one line of code, create a 15x3 matrix that contains only ones.

```{code-cell} ipython3
:tags: [hide-cell]

np.ones((15, 3))
```
