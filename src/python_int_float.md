---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Difference between integers and floats

Usually, floats and integers fulfil different roles:

::::{grid}
:::{grid-item-card}
**Floats** are used to represent real, physical values:
- A force in newtons
- A distance in meters
- A power in watts
- An angle in radians
- etc.
:::
:::{grid-item-card}
**Integers** are used to represent ranks, indexes, counts, etc:
- An index in a list (e.g, 5th value of a list)
- A number of repetitions
- A number of events
- The size of a matrix
- etc.
:::
::::

When we create a new numeric variable, the variable is defined:
- as a `float` if its literal value contains a decimal point
- as an `int` if its literal value contains a decimal point

```{code-cell} ipython3
an_int = 3
a_float = 3.1
```

The type of an existing variable can be known with the function `type`:

```{code-cell}
print(type(an_int))
print(type(a_float))
```

or `isinstance`:

```{code-cell}
print(isinstance(an_int, int))  # Is it an integer?
print(isinstance(an_int, float))  # Is it a float?
```

A variable can be converted from an `int` to a `float` using the `float()` function:

```{code-cell} ipython3
float(an_int)
```

A variable can be converted from a `float` to an `int` using the `int()` function. Please note, however, that the decimal component of the number is lost:

```{code-cell} ipython3
int(a_float)
```
