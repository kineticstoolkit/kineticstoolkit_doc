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

# 🚧 Indexing and slicing

{{ stub }}

:::{card} Summary
This section shows how to index and slice unidimensional and multidimensional arrays, to extract specific information from an array, or to assign new values to it.
:::

:::{admonition} Reminder
Indexing and slicing arrays if very similar to indexing and slicing lists.

- Indexing a list means accessing a specific element of a list, using an index (an integer). For example: `a_list[2]`
- Slicing a list means accessing several elements of a list, using a slice (a combination of integers and columns `:`).  For example: `a_list[0:3]`

Please go back to sections [](python_lists_indexing.md) and [](python_lists_slicing.md) for a refresh on indexing and slicing lists.
:::

## 📄 Unidimensional array

Indexing and slicing a unidimensional array is exactly the same as for a list. For example, here is a list an its equivalent array:

```{code-cell} ipython3
import numpy as np

a_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
an_array = np.array(a_list)

print(a_list)
print(an_array)
```

### Indexing

To read one element of a list/array:

```{code-cell} ipython3
print(a_list[3])  # Read the fourth element
print(an_array[3])  # Read the fourth element
```

To write one element of a list/array:

```{code-cell} ipython3
a_list[3] = 0.35  # Assign 0.35 to fourth element
an_array[3] = 0.35  # Assign 0.35 to fourth element

print(a_list)
print(an_array)
```

### Slicing

To read several elements of a list/array:

```{code-cell} ipython3
# Read each other value from 2nd (incl.) up to 7th (excl.)
print(a_list[1:6:2])
print(an_array[1:6:2])
```

To write several elements of a list/array:

```{code-cell} ipython3
# Write 0.15, 0.35 and 0.55 to 2nd, 4th and 6th elements
a_list[1:6:2] = [0.15, 0.35, 0.55]
an_array[1:6:2] = np.array([0.15, 0.35, 0.55])

print(a_list)
print(an_array)
```

:::{tip}
Note that in the example above, we could also write to the array using a list:

```
an_array[1:6:2] = [0.15, 0.35, 0.55]
```

NumPy is very forgiving in the use of types. In its documentation, argument types are often defined as "array-like", which means that any variable that NumPy can transform to an array is a valid argument. Therefore, lists and lists of lists are very often accepted as arguments, as if they were proper arrays.
:::

## 📄 Multidimensional array

Note that this section only applies to arrays, since a list can only have one dimension. Multidimensional indexes/slices are expressed as unidimensional indexes/slices separated by commas. Let's see this in action with a 3x2 matrix.

```{code-cell} ipython3
an_array = np.array(
    [
        [0.1, 0.2, 0.3],
        [0.4, 0.5, 0.6],
        [0.7, 0.8, 0.9],
        [1.0, 1.1, 1.2],
    ]
)

an_array
```

### Indexing

To read one element of a multidimensional array:

```{code-cell} ipython3
an_array[2, 1]  # Read 3rd line, 2nd column
```

To write one element of a multidimensional array:

```{code-cell} ipython3
an_array[2, 1] = 0.65  # Assign 0.65 to 3rd line, 2nd column

print(an_array)
```

### Slicing

To read multiple elements of an array:

```{code-cell} ipython3
# Read the first and second column of the second line
print(an_array[1, 0:2])  # We index dim 0 (line), and we slice dim 1 (column).
```

```{code-cell} ipython3
# Read the whole second line
print(an_array[1, :])  # We index dim 0, and we take a whole slice of dim 1.
```

```{code-cell} ipython3
# Read the whole second column
print(an_array[:, 1])
```

:::{tip}
Note the lone column operator `:`, which simply means "all data on this dimension".
:::


To write multiple elements to an array:

```{code-cell} ipython3
# Assign [0.35, 0.45, 0.55] to the second line
an_array[1, :] = [0.35, 0.45, 0.55]

an_array
```

```{code-cell} ipython3
# Assign [0.25, 0.5, 0.6, 0.65] to the second column
an_array[:, 1] = [0.25, 0.5, 0.6, 0.65]

an_array
```

We can also assign a single float to multiple elements in a single instruction:

```{code-cell} ipython3
# Assign 1.0 to the whole first column
an_array[:, 0] = 1.0

an_array
```

## 📄 Negative indexing

Negative indexing also works exactly as for lists:

```{code-cell} ipython3
# Assign 2.0 to the whole last line
an_array[-1, :] = 2.0

an_array
```

#todo 🚧 To be continued
