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

# 📖 NumPy

:::{card} Summary
This section presents the NumPy package, which is one of the most important and powerful packages in data processing. NumPy is a huge package. This section covers the basics to get started with it for biomechanical analysis. To really master it, we recommend NumPy's [learning section](https://numpy.org/learn/).

![NumPy Logo -width:narrower](_static/images/numpy_logo.png)
:::

The main goal of NumPy is to perform mathematical operations not only on floats, but also on vectors and matrices, and to perform these operations very quickly.

As an example, let's say we need to average multiple measurements. We could do this easily using basic Python code, by summing every element of a list, and then by dividing the sum by the number of elements:

```{code-cell} ipython3
list_of_float = [1.0, 2.0, 3.0, 2.5, 2.75, 1.5]

# Calculate the sum of every elements
sum = 0
for one_float in list_of_float:
    sum += one_float
    
# Divide by the number of elements
mean = sum / len(list_of_float)

mean
```

NumPy makes it much easier:

```{code-cell} ipython3
import numpy as np

one_array = np.array([1.0, 2.0, 3.0, 2.5, 2.75, 1.5])
np.mean(one_array)
```

This chapter covers the basics of NumPy for biomechanics.


```{tableofcontents}
```
