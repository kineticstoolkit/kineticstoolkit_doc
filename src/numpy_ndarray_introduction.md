# Introduction to arrays

While a NumPy array could be seen as an extension of the [Python lists](python_lists.md) list to multiple dimensions, it has fundamental differences which make both types powerful in its own way. The main differences between both types are:

| Lists                                                                                                                                        | Arrays                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Are unidimensional. We can use nested lists to simulate multiple dimensions, but these values are harder to access, calculate, reshape, etc. | Can have any number of dimensions; they can represent matrices, or even series of matrices. | 
| Can be a sequence of different types, which makes them very versatile.                                                                       | Only hold elements of the same type, which provides homogeneity.                            |
| Have a dynamic size that can be modified using `append`, `expand` and `pop`.                                                                 | Cannot "grow" as we do with lists.                                                          |
| Only hold data, they don't provide methods to compute data.                                                                                  | Can be used directly for calculations such as linear algebra, filtering, etc.               |

They can however be converted one to the other, as seen later in [](numpy_ndarray_creating_from_lists.md).

Each dimension of a NumPy array has a corresponding axis, which allows addressing any value in the array:

::::{grid}
:::{grid-item-card} One-dimension
:columns: 3

![](_static/images/fig_array_1d.png)
+++
Every value is accessed exactly like a list:

- 1st value: `the_array[0]`
- 2nd value: `the_array[1]`
- etc.

:::
:::{grid-item-card} Two dimensions
:columns: 4
![](_static/images/fig_array_2d.png)
+++
Every value is accessed using two coordinates. For a matrix, these coordinates are:

1. the line
2. the column

For example: 

- 1st line, 1st column: `the_array[0, 0]`
- 2nd line, 3rd column: `the_array[1, 2]`
- etc.
:::
:::{grid-item-card} Three dimensions
:columns: 5
![](_static/images/array_3d.png)
+++
Every value is accessed using three coordinates. For a series of matrices, these coordinates are:

1. the matrix
1. the line
2. the column

For example: 

- 1st matrix, 1st line, 1st column: `the_array[0, 0, 0]`
- 1st matrix, 2nd line, 3rd column: `the_array[0, 1, 2]`
- etc.
:::
::::

The **shape** of an array is its size on each of its dimensions. We get this information using its {{ndarray_shape}} property. For instance, the shape of these arrays would be:

::::{grid}
:::{grid-item-card} shape = `(4,)`
:columns: 3
![](_static/images/fig_array_1d.png)

:::
:::{grid-item-card} shape = `(3, 4)`
:columns: 4
![](_static/images/fig_array_2d.png)

:::
:::{grid-item-card} shape = `(3, 3, 4)`
:columns: 5
![](_static/images/array_3d.png)

:::
::::


:::{note}
Note the trailing comma after the 4 in the notation `(4,)` above. It is required to avoid confusing the tuple delimiter `()` with standard parentheses `()`. Writing `(4)` without a comma is an integer in parentheses, while writing `(4,)` with a comma is a tuple of 1 value. The `shape` property of an array is always a tuple.
:::
