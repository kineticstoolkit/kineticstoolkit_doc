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

In addition to arithmetical operators, NumPy provides lots of essential functions and constants to perform trigonometrical operations:

- {{np_pi}}: π
- {{np_sin}}: Sinus
- {{np_cos}}: Cosinus
- {{np_tan}}: Tangent
- {{np_arcsin}}: Arc-sinus
- {{np_arccos}}: Arc-cosinus
- {{np_arctan}}: Arc-tangent
- {{np_arctan2}}: Art-tangent in the full plane, contrarily to {{np_arctan}} that only returns values from -π/2 (-90°) to +π (+90°)
- {{np_deg2rad}}: Convert degrees to radians
- {{np_rad2deg}}: Convert radians to degrees
- {{np_abs}}: Absolute value
- {{np_sqrt}}: Square root

In all trigonometric functions, angles are in radians by default. You can either convert to/from degrees by multiplying or dividing by $\pi/180$ manually, or use {{np_deg2rad}} and {{np_rad2deg}}.

```{code-cell} ipython3
import numpy as np
import matplotlib as plt

angle = np.linspace(0, 2 * np.pi, 100)

plt.plot(angle, np.sin(angle))
plt.show()
```
