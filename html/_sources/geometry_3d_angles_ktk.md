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


# Extracting 3D angles using Kinetics Toolkit

We already used the [ktk.geometry.get_angles](api/ktk.geometry.get_angles.rst) function to extract [a 2D angle](geometry_2d_angles.md). This function can also accommodate any of these 24 variations of 3D rotation sequences, using the `seq` parameter which is 3 characters belonging to the set {'X', 'Y', 'Z'} for intrinsic rotations (moving axes), or {'x', 'y', 'z'} for extrinsic rotations (fixed axes).

For instance, lets create a 3d rotation defined by an extrinsic cardan sequence of 20° about the x axis, then -10° about the y axis, then 15° about the z axis:

$$
T = T_{15^\circ \text{around} z}
~~~ T_{-10^\circ \text{around} y}
~~~ T_{20^\circ \text{around} x}
$$

```{code-cell} ipython3
import kineticstoolkit.lab as ktk


total_rotation = ktk.geometry.matmul(
    ktk.geometry.create_transforms(angles=[15], seq="z", degrees=True),
    ktk.geometry.matmul(
        ktk.geometry.create_transforms(angles=[-10], seq="y", degrees=True),
        ktk.geometry.create_transforms(angles=[20], seq="x", degrees=True),
    ),
)

total_rotation
```

To extract these three angles back from this matrix, we would use a sequence of "xyz", in lower case to denote extrinsic rotations:

```{code-cell} ipython3
angles = ktk.geometry.get_angles(total_rotation, seq="xyz", degrees=True)

angles
```

Note that other combinations would give different and wrong angles:

```{code-cell} ipython3
print(ktk.geometry.get_angles(total_rotation, seq="XYZ", degrees=True))
print(ktk.geometry.get_angles(total_rotation, seq="xzy", degrees=True))
print(ktk.geometry.get_angles(total_rotation, seq="zyx", degrees=True))
print(ktk.geometry.get_angles(total_rotation, seq="ZXY", degrees=True))
```

