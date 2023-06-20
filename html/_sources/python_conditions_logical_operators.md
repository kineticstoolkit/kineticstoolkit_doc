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

# Logical operators

In section [](python_conditions_boolean.md), we learned how to generate boolean values (True, False) using comparison operators such as `>` (greater than) or `<=` (less or equal to). We can create more complex comparisons by combining and inverting the results of many comparisons, using the logical operators `not`, `or` and `and` as shown in {numref}`fig_logical_operators`.

```{figure-md} fig_logical_operators
:width: 3.5in
![](_static/images/fig_logical_operators.png)

Truth table of `not`, `or` and `and`.
```


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
