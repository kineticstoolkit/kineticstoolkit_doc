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

# Integers and floats

Usually, floats and integers fulfil different roles:

::::{grid}
:::{grid-item-card}
**Floats** are used to represent real, physical values:
- Force in newtons
- Distance in meters
- Power in watts
- Angle in radians
- etc.
:::
:::{grid-item-card}
**Integers** are used to represents:
- An index in a list (e.g, 5th value of a list)
- A number of repetitions
- A number of events
- The size of a matrix
- etc.
:::
::::

When we create a new numeric variable, the variable is defined:
- as a `float` if its literal value contains a decimal point
- as an `int` if its literal value contain a decimal point

```{code-cell} ipython3
an_int = 3
a_float = 3.0
```

The type of an existing variable can be known with the functions `type`, or `isinstance`:

```{code-cell}
print(type(an_int))
print(type(a_float))
```

```{code-cell}
print(isinstance(an_int, int))  # Is it an integer?
print(isinstance(an_int, float))  # Is it a float?
```

A variable can be converted from an `int` to a `float` using the `float()` function:

```{code-cell} ipython3
new_variable = float(an_int)

print(new_variable)
print(type(new_variable))
```

A variable can be converted from a `float` to an `int` using the `int()` function. Please note, however, that the decimal component of the number is lost:

```{code-cell} ipython3
new_variable = int(a_float)

print(new_variable)
print(type(new_variable))
```
