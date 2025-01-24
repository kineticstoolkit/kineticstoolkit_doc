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


# Trigonometry

In addition to arithmetic operators, NumPy provides lots of essential functions and constants to perform trigonometrical operations:

- {{np_pi}}: π
- {{np_sin}}: Sine
- {{np_cos}}: Cosine
- {{np_tan}}: Tangent
- {{np_arcsin}}: Arcsine
- {{np_arccos}}: Arccosine
- {{np_arctan}}: Arctangent
- {{np_arctan2}}: Arctangent in the full plane, unlike {{np_arctan}} that only returns values from -π/2 (-90°) to +π (+90°)
- {{np_deg2rad}}: Convert degrees to radians
- {{np_rad2deg}}: Convert radians to degrees
- {{np_abs}}: Absolute value
- {{np_sqrt}}: Square root

In all trigonometric functions, angles are in radians by default. You can either convert to/from degrees by multiplying or dividing by $\pi/180$ manually, or use {{np_deg2rad}} and {{np_rad2deg}}.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

angle = np.linspace(0, 2 * np.pi, 100)

plt.plot(angle, np.sin(angle));
```
