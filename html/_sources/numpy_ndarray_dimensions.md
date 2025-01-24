# Array dimensions

Each dimension of a NumPy array has a corresponding axis, which allows addressing any value in the array:



**One dimension**

::::{grid}
:::{grid-item}
:columns: 5

![](_static/images/fig_array_1d.png)
:::
:::{grid-item}
:columns: 7

Every value is accessed exactly like a list:

- 1st value: `the_array[0]`
- 2nd value: `the_array[1]`
- etc.

:::
::::

**Two dimensions**

::::{grid}
:::{grid-item}
:columns: 5
![](_static/images/fig_array_2d.png)
:::

:::{grid-item}
:columns: 7

Every value is accessed using two coordinates. For a matrix, these coordinates are:

1. the row
2. the column

For example: 

- 1st row, 1st column: `the_array[0, 0]`
- 2nd row, 3rd column: `the_array[1, 2]`
- etc.
:::
::::

**Three dimensions**

::::{grid}
:::{grid-item}
:columns: 5
![](_static/images/fig_array_3d.png)
:::
:::{grid-item}
:columns: 7

Every value is accessed using three coordinates. For a series of matrices, these coordinates are:

1. the matrix in the series
1. the row
2. the column

For example: 

- 1st matrix, 1st row, 1st column: `the_array[0, 0, 0]`
- 1st matrix, 2nd row, 3rd column: `the_array[0, 1, 2]`
- etc.
:::
::::

The **shape** of an array is its size on each of its dimensions. We get this information using its {{ndarray_shape}} property. For instance, the shape of these arrays would be:

**One dimension**

::::{grid}
:::{grid-item}
:columns: 5
![](_static/images/fig_array_1d.png)
:::
:::{grid-item}
:columns: 7
shape = `(4,)`
:::
::::

**Two dimensions**

::::{grid}
:::{grid-item}
:columns: 5
![](_static/images/fig_array_2d.png)
:::
:::{grid-item}
:columns: 7
shape = `(3, 4)`
:::
::::

**Three dimensions**

::::{grid}
:::{grid-item}
:columns: 5
![](_static/images/fig_array_3d.png)
:::
:::{grid-item}
:columns: 7
shape = `(3, 3, 4)`
:::
::::


:::{note}
Note the trailing comma after the 4 in the notation `(4,)` above. It is required to avoid confusing the tuple delimiter `()` with standard parentheses `()`. Writing `(4)` without a comma is an integer in parentheses, while writing `(4,)` with a comma is a tuple of 1 value. The `shape` property of an array is always a tuple.
:::
