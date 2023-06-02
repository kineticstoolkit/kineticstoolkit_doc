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

# Exercise: Statistics

We recorded this series of forces using a gait force platform, where the first axis corresponds to time and the second axis corresponds to $F_x$, $F_y$ and $F_z$.

```{code-cell} ipython3
import numpy as np

forces = np.array(
    [
        [0.17619048, 0.82380952, 17.61904762],
        [0.21428571, 0.78571429, 21.42857143],
        [0.17619048, 0.82380952, 17.61904762],
        [0.17619048, 0.82380952, 17.61904762],
        [0.17619048, 0.82380952, 17.61904762],
        [0.32857143, 0.67142857, 32.85714286],
        [0.25238095, 0.74761905, 25.23809524],
        [0.17619048, 0.82380952, 17.61904762],
        [0.29047619, 0.70952381, 29.04761905],
        [0.32857143, 0.67142857, 32.85714286],
        [0.25238095, 0.74761905, 25.23809524],
        [0.21428571, 0.78571429, 21.42857143],
        [0.67142857, 0.32857143, 67.14285714],
        [8.1, -7.1, 810.0],
        [8.70952381, -7.70952381, 870.95238095],
        [8.02380952, -7.02380952, 802.38095238],
        [7.26190476, -6.26190476, 726.19047619],
        [7.75714286, -6.75714286, 775.71428571],
        [9.47142857, -8.47142857, 947.14285714],
        [9.85238095, -8.85238095, 985.23809524],
        [9.54761905, -8.54761905, 954.76190476],
        [8.63333333, -7.63333333, 863.33333333],
        [7.83333333, -6.83333333, 783.33333333],
        [6.76666667, -5.76666667, 676.66666667],
        [5.2047619, -4.2047619, 520.47619048],
        [2.95714286, -1.95714286, 295.71428571],
        [1.50952381, -0.50952381, 150.95238095],
        [0.48095238, 0.51904762, 48.0952381],
        [-0.01428571, 1.01428571, -1.42857143],
        [0.02380952, 0.97619048, 2.38095238],
        [0.17619048, 0.82380952, 17.61904762],
        [0.02380952, 0.97619048, 2.38095238],
        [0.06190476, 0.93809524, 6.19047619],
        [0.06190476, 0.93809524, 6.19047619],
        [0.06190476, 0.93809524, 6.19047619],
        [0.02380952, 0.97619048, 2.38095238],
        [0.06190476, 0.93809524, 6.19047619],
        [0.13809524, 0.86190476, 13.80952381],
    ]
)
```

```{code-cell} ipython3
:tags: [remove-input]

import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

plt.plot(forces)
plt.xlabel("# sample")
plt.ylabel("Force (N)")
plt.legend(["Fx", "Fy", "Fz"])
plt.show()
```

1. Write one code line that calculates the three mean forces $\overline{F_x}$, $\overline{F_y}$ and $\overline{F_z}$ over the whole time span.
2. Write one code line that calculates the series of resulting force ($F_\text{tot} = \sqrt{F_x^2 + F_y^2 + F_z^2}$) at each time.
3. Write one code line that calculates the mean resulting force $\overline{F_\text{tot}}$ over the whole time span.

```{code-cell} ipython3
:tags: [hide-cell]

# 1.
print("== 1 ==")
print(
    np.mean(forces, axis=0),
)

# 2.
print("== 2 ==")
print(
    np.sqrt(np.sum(forces**2, axis=1)),
)

# 3.
print("== 3 ==")
print(
    np.mean(np.sqrt(np.sum(forces**2, axis=1)), axis=0),
)
```
