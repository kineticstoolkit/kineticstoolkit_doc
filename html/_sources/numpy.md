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
This section presents the NumPy package, that is the basis of virtually any data processing operation in the different fields related to numerical analysis and algebra in Python.

NumPy is a huge package. This section covers the basics to get started with Numpy for biomechanical analysis. To really master it, we recommended to consult the [learning section](https://numpy.org/learn/) on their [website](https://numpy.org).

[![NumPy Logo -width:narrower](_static/images/numpy_logo.png)](https://numpy.org)
:::

The main goal of NumPy is to perform mathematical operations not only on floats, but also on vectors and matrices, and to perform these operation very fast.

Let's use the averaging of multiple measurements as an example. We could very well use pure python and apply the mean equation (sum of all measurements divided by the number of measurements) to a list of float, using a `for` loop:

```{code-cell} ipython3
list_of_float = [1.0, 2.0, 3.0, 2.5, 2.75, 1.5]

# Calculate the sum of every elements
result = 0
for one_float in list_of_float:
    result += one_float
    
# Divide by the number of elements
result /= len(list_of_float)

result
```

Using NumPy, this would be much easier:

```{code-cell} ipython3
import numpy as np

# Create a numpy array
one_array = np.array([1.0, 2.0, 3.0, 2.5, 2.75, 1.5])

# Calculate the mean
np.mean(one_array)
```

This chapter shows the basics of NumPy, in an approach directed toward biomechanical analysis.


```{tableofcontents}
```
