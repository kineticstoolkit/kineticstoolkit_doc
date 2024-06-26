---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Boolean and comparisons

Comparisons are performed using the operators `==`, `!=`, `>=`, `>`, `<=` and `<`, and always result in a variable of type boolean. We already know the following types of variable: `string`, `int`, `float` and `complex`. Boolean variables, `bool`, are the simplest: they can be either `True` or `False`.

::::{grid}
:::{grid-item-card} Equal
:columns: 6
```
10 == 5
```

+++

False
:::
:::{grid-item-card} Unequal
:columns: 6
```
10 != 5
```

+++

True
:::
::::
::::{grid}
:::{grid-item-card} Lower or equal
:columns: 6
```
10 <= 5
```

+++

False
:::
:::{grid-item-card} Greater or equal
:columns: 6
```
10 >= 5
```

+++

True
:::
::::
::::{grid}
:::{grid-item-card} Strictly lower
:columns: 6
```
10 < 5
```

+++

False
:::
:::{grid-item-card} Strictly greater
:columns: 6
```
10 > 5
```

+++

True
:::
::::

Obviously, comparing a constant with another constant has little sense. However, comparing variables with constants, or variables with other variables, is very common:

```{code-cell} ipython3
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
my_score > WORLD_RECORD
```

:::{important}
You may note that the equality comparison is a double-equal `==` instead of a single one `=`. This is to avoid confusion between a comparison:

```
a == 5
```
which returns `True` or `False`

and an assignment:

```
a = 5
```
which assigns the value of 5 to variable `a`.
:::

:::{tip}
Boolean values can be used in arithmetical operations: their numerical value is 0 for False, and 1 for True. For instance:

```
14 * True + 2 * False
```

14
:::
