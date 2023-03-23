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

# Boolean operators

We can construct complex comparisons by combining the results of many comparisons, using the logical operators `not`, `and` and `or`. These operators are specifically aimed to compare booleans.

The `not` operator inverts the value of a `bool`:
```{code-cell}
not True
```

```{code-cell}
not False
```

The `or` operator yields `True` as long as one of the two operands is True:

```{code-cell}
True or False
```

```{code-cell}
False or False
```

The `and` operator yields `True` if both operands are True:

```{code-cell}
True and False
```

```{code-cell}
True and True
```

Using these operators, we can construct more complex comparisons and program flows, such as this example:

```{code-cell}
def is_between(a, lower, upper):
    """Returns True if a is strictly between lower and upper."""
    return (a > lower) and (a < upper)


# Test the function
print(is_between(3, 2, 5))
print(is_between(10, 2, 5))
print(is_between(2, 2, 5))
```

:::{good-practice} Naming functions that return bools
For clarity, functions that return booleans often start with `is_`, `has_`, `contains_`, etc.
:::
