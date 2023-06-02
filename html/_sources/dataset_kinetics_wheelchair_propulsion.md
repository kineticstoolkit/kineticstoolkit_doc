---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Wheelchair propulsion kinetics

This dataset was recorded at the [Mobility and Adaptive Sports Research Lab](https://felixchenier.com).

These are the 3D kinetics (3 forces, 3 moments) applied by a wheelchair user on an instrumented pushrim, during wheelchair propulsion from stop. Data are sampled at 240 Hz and are expressed as a TimeSeries.

Coordinate system: x is forward, y is upward, z is lateral, in the wheelchair reference frame.

## TimeSeries contents

| Data key | Definition                                                      |
| -------- | --------------------------------------------------------------- |
| Forces   | Nx4 array consisting where each line is $[F_x, F_y, F_z, 0.0]$. |
| Moments  | Nx4 array consisting where each line is $[M_x, M_y, M_z, 0.0]$. |

## Files

- `kinetics_wheelchair_propulsion.ktk.zip`: TimeSeries with the forces and moments, without events.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

filename = ktk.doc.download("kinetics_wheelchair_propulsion.ktk.zip")
kinetics = ktk.load(filename)
kinetics.plot()
```
