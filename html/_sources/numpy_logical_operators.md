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

In section [](python_conditions_logical_operators.md), we learned the logical operators `not`, `or` and `and`. Unfortunately, these operators work only on bool, not on arrays of bool. However, NumPy provides equivalents:

| Python's operator on `bool` | NumPy's equivalent operator for arrays of `bool` |
|:---------------------------:|:------------------------------------------------:|
|            `not`            |                       `~`                        |
|            `or`             |                       `\|`                       |
|            `and`            |                       `&`                        |

{numref}`fig_numpy_boolean_operators` illustrates the behaviour of each operator.

```{figure-md} fig_numpy_boolean_operators
![Logical operators on Python and Numpy](_static/images/fig_numpy_boolean_operators.png)

Correspondence between logical operations on bool and ndarray.
```
