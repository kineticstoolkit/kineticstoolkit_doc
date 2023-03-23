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

# Arithmetic operations between integers and floats

When we perform operation between different types, python may convert the types to ensure that the result holds the correct value. For example, adding a float to an integer results in a float:

```{code-cell} ipython3
a = 2 + 4.5

type(a)
```

However, adding an integer to another integer results in an integer:

```{code-cell} ipython3
b = 2 + 4

type(b)
```

A special case is the division, which always results in a float, even if we divide two integers, and even if the result is round:

```{code-cell} ipython3
c = 4 / 2

type(c)
```
