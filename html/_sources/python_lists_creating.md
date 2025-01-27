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


# Creating lists and tuples

As implied by its name, a list is an ordered collection of values. A tuple is also an ordered collection of values, but it cannot be modified after being created while a list can. Choosing between a list or a tuple is often philosophical:
- We normally use a tuple to express a constant using a group of variables. The coordinates of a 2D point (x, y) is a good example. Once a 2D point is defined by its two coordinates (x, y), there is no use to append a third value to it.
- We normally use a list to express an expandable list of values. A series of measurements \[x0, x1, x1, x2, x3\] is a good example. We may add or remove measurements from a list.

:::{important}
We usually use lists more often than tuples in data processing because they are more flexible. Therefore, from now on, we will focus on lists. This being said, **everything on this page also applies to tuples**.
:::

A tuple is created using parentheses `()`:

```{code-cell} ipython3
coordinates = (1.0, 5.2)
```

A list is created using square brackets `[]`:

```{code-cell} ipython3
empty_list = []
list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Lists can contain any kind of variable, even other lists or any other container type such as dictionaries:

```{code-cell} ipython3
list_of_anything = [
    "hello",            # string
    0,                  # int
    4.5,                # float
    (2 + 3j),           # complex
    False,              # bool
    [1, 2, 3],          # list
    {"key": "value"},   # dict
]
```

:::{note}
The `{"key": "value"}` syntax is a dictionary, that will be seen in section [](python_dicts.md).
:::

We can get the length of a list (i.e., the number of elements it contains) using the `len` function:

```{code-cell} ipython3
len(list_of_anything)
```
