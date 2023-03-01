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
This section presents the array and its differences and similarities to the list. It also show how to create arrays of different shapes.
:::

Most NumPy operations are performed on arrays. An array is different from a Python list, and each has its advantages:

| List                                                                                                                                              | Array                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Can be a sequence of different types, which makes it very versatile.                                                                              | Have element that are of the same type, which provides homogeneity.                                                           |
| Have a dynamic size: it can be modified using `append`, `expand` and `pop`.                                                                       | Are continuous blocks with a fixed size. While we can merge two arrays, we usually don't "grow" an array as we do with lists. |
| Only hold data, they don't provide methods to compute data other than by using `for` loops.                                                       | Can be used directly for calculations such as linear algebra, filtering, etc.                                                 |
| Are only unidimensional. We can use nested lists to simulate multiple dimensions, but these values are harder to access, calculate, reshape, etc. | Can be multidimensional. Therefore, it can represent and calculate matrices, or even series of matrices.                      |

While lists and arrays are different, they are both useful and they can be converted one to the other.

## 📄 Creating an array

### From a list

Creating an array from a list is done using the `np.array` function:

```{code-cell} ipython3
import numpy as np

one_array = np.array([1.0, 2.0, 3.0, 2.5, 2.75, 1.5])

one_array
```

:::{note}
It is also possible to convert back an array to a list, using the `tolist` method:

```
one_array.tolist()
```

:::

### Zeros and ones

To create arrays filled with zeros or ones, we use the `np.zeros` and `np.ones` functions:

```{code-cell} ipython3
print(np.zeros(10))  # 10 is the length of the array to create
print(np.ones(10))   # 10 is the length of the array to create
```

### Linear spacing

To create equally distributed series of float, we can use `np.linspace`, which takes as arguments the initial value, the final value, and the number of points in the new array. For example, to create an array that goes from 5.0 (included) to 10.0 (included) and that contains 11 elements:

```{code-cell} ipython3
np.linspace(5.0, 10.0, 11)
```

Or we can use `np.arange`, which is very similar to the `range` function seen in section [](python_for_range.md), but which also accepts floats in addition to integers.

Its different forms are:

- `np.arange(final_value)`
- `np.arange(initial_value, final_value)`
- `np.arange(initial_value, final_value, step)`

where the initial value is inclusive and the final value is exclusive. Here are some examples:

Range from 0 (included) to 10 (excluded):
```{code-cell} ipython3
print(np.arange(10.0))
```

Range from 5 (included) to 10 (excluded):
```{code-cell} ipython3
print(np.arange(5.0, 10.0))
```

Range from 5 (included) to 10 (excluded), by steps of 0.5:
```{code-cell} ipython3
print(np.arange(5.0, 10.0, 0.5))
```


## 💪 Exercise 1

We recorded the force measured by a dynamometer at a sampling frequency of 100 Hz, during 2.5 seconds. Using one line of code (excluding the `import` line), create a NumPy array named `time`, that represents the time at which every measurement was recorded. For example, the first element of this array will be 0 s., the second will be 0.01 s., etc.

```{code-cell} ipython3
:tags: [hide-cell]

# The initial time is 0 s
# The final time corresponds to 2.5 seconds
# The step is the sampling period, which is 1/(100 Hz).

time = np.arange(0, 2.5, 0.01)

time
```

## 📄 Multiple dimensions

The ability to create arrays of any numbers of dimensions may be one of the most useful aspects of NumPy. We will start with two dimensions, and expand to more dimensions later in other sections.

### Creating a multidimensional array from a list

While we can create a unidimensional array using a list:

```{code-cell} ipython3
array_1d = np.array([1.0, 2.0, 3.0])

array_1d
```

We can create a multidimensional array using a list of nested lists:

```{code-cell} ipython3
array_2d = np.array(
    [
        [1.0, 2.0],
        [3.0, 4.0],
        [5.0, 6.0],
    ]
)

array_2d
```

### Shape of an array

We are now used to use the function `len` on lists, to know how big a list is. While this function also works on an array, it only returns the length of the array on its first dimension. To get the complete size (shape) of an array, we use the array's `shape` property:

```{code-cell} ipython3
print(array_1d.shape)
print(array_2d.shape)
```

For a 2d array, the first dimension corresponds to the lines, and the second dimension corresponds to the columns. Since the `shape` property always returns a tuple, we extract the number of lines and columns by indexing this tuple:

```{code-cell} ipython3
print(
    f"This array has {array_2d.shape[0]} lines and {array_2d.shape[1]} columns."
)
```

### Creating a multidimensional array of zeros or ones

Let's have a look at the [docstring of `np.zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html).

![np.zeros -width:wider -border](_static/images/np.zeros.png)

Look at the first argument, which is a shape or an integer. In our first example, we used an integer to define the length of the new unidimensional array. If we use a shape instead, it creates an array of this shape.

```{code-cell} ipython3
np.zeros((3, 2))  # A 3x2 matrix filled with zeros
```

:::{tip}
Although the `shape` property of an array is a tuple, we can also use lists to define shapes. This code is equivalent to the code above:
```
np.zeros([3, 2])
```
:::

In the same idea:

```{code-cell} ipython3
np.ones([3, 2])  # A 3x2 matrix filled with ones
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
