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

# NumPy

The main goal of {{numpy}} is to perform mathematical operations not only on floats, but also on vectors and matrices, and to perform these operations very quickly.

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

:::{tip}
If you already know Matlab, then this [cheat sheet](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) could be useful.
:::

```{figure-md} fig_numpy_logo
:width: 4in
![NumPy Logo](_static/images/fig_numpy_logo.png)

Numpy logo.
```

**Chapter Contents**

```{tableofcontents}
```
