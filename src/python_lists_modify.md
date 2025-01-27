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

# Modifying lists

This section shows how to modify one or many elements of a list (using indexing and slicing), how to `extend` lists or `append` data to lists, and how to remove an element from a list using `pop`.

:::{important}
Since tuples are immutable, this page does not apply to tuples.
:::

## Modifying an element

We already know how to read one element of a list using [indexing](python_lists_indexing.md) and multiple elements using [slicing](python_lists_slicing.md):

```{code-cell} ipython3
a = [1, 2, 3]

# Read the first element (indexing)
print(a[0])

# Read the first and second elements (slicing)
print(a[0:2])
```

We can also use indexing and slicing to write elements of a list.

To modify a single element using indexing:

```{code-cell} ipython3
a = [1, 2, 3]
a[0] = 10

a
```

To modify multiple elements using slicing:

```{code-cell} ipython3
a = [1, 2, 3]

# Assign 20 and 30 from `b` in place of 1 and 2 in `a`
a[0:2] = [10, 20]

a
```

## Appending an element to a list

To append a new element to a list, we use the list's `append` method, which takes the new element as an argument.

:::{admonition} Function vs method
A [function](python_functions.md) is a subprogram that can process arguments and return a result.

```
output = function(variable)
```

A **method** is a special type of function that is only available for a given variable type. It is called using the variable itself, using the dot `.` operator:

```
output = variable.method()
```

Methods sometimes modify the variable itself, which is the case with `append` and `extend`.

:::

```{code-cell} ipython3
a = [1, 2, 3]
print("a before =", a)

a.append(4)

print("a after =", a)
```

## Extending a list

To append multiple elements at once, we instead use the lists' `extend` method, which takes a list of new elements as an argument.

```{code-cell} ipython3
a = [1, 2, 3]
print("a before =", a)

a.extend([4, 5])

print("a after =", a)
```

## Deleting an element from a list

To remove an element at a given index, we use the list's `pop` method, which returns the element being deleted and removes it from the list.

```{code-cell} ipython3
a = [1, 2, 3]

print(a.pop(0))  # Remove the first element
print(a)
```
