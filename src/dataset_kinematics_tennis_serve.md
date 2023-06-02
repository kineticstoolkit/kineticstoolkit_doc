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

# Tennis serve kinematics

This dataset was kindly provided by Fraje Watson, Steve Taylor and Jin (Derrick) Gaokuang from the [University College London](https://www.ucl.ac.uk/), [Aspire CREATe lab](https://ucl.ac.uk/aspire-create).

These are the bilateral kinematics of four tennis serves, sampled at 50 Hz. The laboratory vertical axis is z.

## Markerset

| Marker       | Definition                          | Marker       | Definition                                    |
| ------------ | ----------------------------------- | ------------ | ----------------------------------- |
| Derrick:LTOE | Left toe                            | Derrick:RTOE | Right toe                            |
| Derrick:LHEE | Left heel                           | Derrick:RHEE | Right heel                           |
| Derrick:LANK | Left ankle                          | Derrick:RANK | Right ankle                          |
| Derrick:LKNE | Left knee                           | Derrick:RKNE | Right knee                           |
| Derrick:LASI | Left anterior-superior iliac spine  | Derrick:RASI | Right anterior-superior iliac spine  |
| Derrick:LPSI | Left posterior-superior iliac spine | Derrick:RPSI | Right posterior-superior iliac spine |
| Derrick:LSHO | Left shoulder                       | Derrick:RSHO | Right shoulder                       |
| Derrick:LELB | Left elbow                          | Derrick:RELB | Right elbow                          |
| Derrick:LWRA | Left wrist (A)                      | Derrick:RWRA | Right wrist (A)                      |
| Derrick:LWRB | Left wrist (B)                      | Derrick:RWRB | Right wrist (B)                      |
| Derrick:LFIN | Left finger                         | Derrick:RFIN | Right finger                         |
| Derrick:LFHD | Left forehead                       | Derrick:RFHD | Right forehead                       |
| Derrick:LBHD | Left backhead                       | Derrick:RBHD | Right backhead                       |
| Derrick:C7   | C7                                  | Derrick:T10  | T10                                 |
| Derrick:STRN | Sternum                             | Derrick:CLAV | Interclavicular space               |

## Files

- `kinematics_tennis_serve.c3d`: Labelled markers, no events, no forces, no analog signals

```{code-cell} ipython3
:tags: [remove_output]

import kineticstoolkit.lab as ktk

filename = ktk.doc.download("kinematics_tennis_serve.c3d")
markers = ktk.read_c3d(filename)["Points"]
player = ktk.Player(markers)
```

```{code-cell} ipython3
:tags: [remove-input]

player = ktk.Player(markers.get_ts_between_times(2, 5), up="z")
player._to_animation()
```

- `kinematics_tennis_serve_nan.c3d`: Same as `kinematics_tennis_serve.c3d`, with simulated missing samples on Derrick:RSHO.

```{code-cell} ipython3
filename = ktk.doc.download("kinematics_tennis_serve_nan.c3d")
markers = ktk.read_c3d(filename)["Points"]
markers.plot("Derrick:RSHO")
```
