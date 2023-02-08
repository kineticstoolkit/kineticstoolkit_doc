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

# 🚧 Numpy arithmetics

{{ stub }}

## Exercise ideas

- Filtered EMG and filtered EMGmax: plot a curve of EMG normalized by MVC.
- Calculate the speed of the COM during a jump, based on the trajectory of the COM, and use the position and speed curve to calculate the impulse time.

---

The rest of this section is just a draft that is out of context for now.

---


## Matrix multiplication

The main goal of Numpy is to perform mathematical operations not only on floats, but on whole arrays. For example, using Numpy, we can realize a complete matrix multiplication in only one instruction, and this single operation is really fast.

Let's compare how we would perform this operation:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\begin{bmatrix}
1 \\ 2 \\ 3
\end{bmatrix}
$$

using both pure Python code, and then using Numpy. Let's first represent both matrices as variables. The second one could be a list of three elements:

```{code-cell}
b = [1.0, 2.0, 3.0]
```

and the first one could be a list of three rows, where each row is a list of three columns:

```{code-cell}
a = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
]
```

## Matrix multiplication using pure python

The matrix multiplication $a b$ is performed by this series of operations:

```
[
    a[0, 0] b[0] + a[0, 1] b[1] + a[0, 2] b[2]
    a[1, 0] b[0] + a[1, 1] b[1] + a[1, 2] b[2]
    a[2, 0] b[0] + a[2, 1] b[1] + a[2, 2] b[2]
]
```

Therefore, one possible code to calculate this multiplication would be:

```{code-cell}
result = []  # Initialize an empty list for the result
for i_row in range(3):
    temp = 0  # Temporary result for this row
    for i_column in range(3):
        temp += a[i_row][i_column] * b[i_column]
    result.append(temp)

# Print the result
result
```

## Matrix multiplication using Numpy

In Numpy, we create multidimensional arrays using Numpy's `array` object. There are several ways to create an array, and one is to simply use a list of lists:

```{code-cell}
# Import the Numpy library to access its contents
import numpy as np

# Convert a and b to Numpy arrays
a_array = np.array(a)
b_array = np.array(b)

# Perform a matrix multiplication, which is the operator @
result = a_array @ b_array

# Print the result
result
```
