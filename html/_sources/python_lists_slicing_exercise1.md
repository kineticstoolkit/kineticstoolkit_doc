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

# Exercise: Slicing lists 1

Here is a list:

```{code-cell} ipython3
list_of_strings = ["zero", "one", "two", "three", "four", "five"]
```

What would be the code to transform `list_of_strings` into:

```
["five", "four", "three", "two", "one", "zero"]
```

:::{tip}
You may want to review [negative indexing](python_lists_indexing.md) again.
:::

```{code-cell} ipython3
:tags: [hide-cell]

# We start at the last element of list_of_strings.
# We can use negative indexing to get this element: -1
# Therefore, the first number of the slice (start index) is -1.

# We will go backward through the list.
# Therefore, the third number of the slice (increment) is -1.

# We go through the entire list. There is no ending point.
# Therefore, there is no second number in the slice.

list_of_strings[-1::-1]
```
