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


# Conditional filtering

In section [](numpy_arithmetics.md), we learned how to generate arrays of bool by comparing an array to a number using comparison operators such as `==`, `<`, `>=`, etc. These comparisons make a powerful way to filter an array. For example, to keep every data of an array that is positive:

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt


to_keep = data >= 0  # Create a boolean mask of the values to keep

plt.plot(time, data, "s-", label="Original data")
plt.plot(time[to_keep], data[to_keep], "o-", label="Filtered data")
plt.legend()
plt.show()
```

Or, as another example, to replace any negative value by 0:

```{code-cell} ipython3
new_data = data.copy()

# Assign 0 to every index of new_data where data is zero
new_data[data < 0] = 0  

plt.plot(time, data, "s-", label="Original data")
plt.plot(time, new_data, "o-", label="New data")
plt.legend()
plt.show()
```
