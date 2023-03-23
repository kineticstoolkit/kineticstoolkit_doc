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

# Arrays

:::{card} Summary
This section presents the NumPy {{ndarray}} and its differences and similarities to the list. It also show how to create arrays of different shapes using:

- {{np_array}}
- {{np_zeros}}
- {{np_ones}}
- {{np_linspace}}
- {{np_arange}}
:::

Most NumPy operations are performed on arrays. An array is similar to a list but has fundamental differences:

| Lists                                                                                                                                        | Arrays                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Can be a sequence of different types, which makes them very versatile.                                                                       | Only hold elements of the same type, which provides homogeneity.                            |
| Have a dynamic size that can be modified using `append`, `expand` and `pop`.                                                                 | Cannot "grow" as we do with lists.                                                          |
| Only hold data, they don't provide methods to compute data.                                                                                  | Can be used directly for calculations such as linear algebra, filtering, etc.               |
| Are unidimensional. We can use nested lists to simulate multiple dimensions, but these values are harder to access, calculate, reshape, etc. | Can have any number of dimensions; they can represent matrices, or even series of matrices. | 

Lists and arrays are both useful and they can be converted one to the other.

```{tableofcontents}
```
