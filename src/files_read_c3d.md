---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
tags: [remove-cell]
---
%matplotlib inline
```

# Reading C3D files

Let's first download a sample C3D file:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

filename = ktk.doc.download("c3d_sample.c3d")
```

We read it using [ktk.read_c3d](api/ktk.read_c3d.rst):

```{code-cell} ipython3
c3d_contents = ktk.read_c3d(filename)

c3d_contents
```

:::{caution}
As indicated in the warning above, the points in this file are expressed in millimeters; however Kinetics Toolkit uses SI units and therefore meters by default. The point positions have been converted to meters by default, and therefore you can ignore this warning, or suppress it all the way using:

```
c3d_contents = ktk.read_c3d(filename, convert_point_unit=True)
```

You can generally ignore this warning if you read unprocessed marker positions and analog signals.

You should not ignore this warning if you are reading a c3d file that has been processed by some software or pipeline to calculate joint kinetics, powers, etc., and if these values are expressed as "points" in the c3d. Consult the help of [ktk.read_c3d](api/ktk.read_c3d.rst) for more details.
:::

The content of the file is expressed as a dictionary with two keys:
- `Points`: A TimeSeries that contains the point data (markers)
- `Analogs` (only when applicable): A TimeSeries that contains the raw analog data from force platforms, EMG or other analog signals recorded into the c3d file.
- `ForcePlateforms` (only when applicable): A TimeSeries that contains the forces, moments, centres of pressure and force platform positions.

## Points

Each data key of the Points TimeSeries corresponds to one point (marker):

```{code-cell} ipython3
c3d_contents["Points"].data
```

We will learn how to visualize these markers using an interactive player in [](player). For now, let's plot some of them:

```{code-cell} ipython3
c3d_contents["Points"].plot(["c7", "r should"])
```

## Analogs

Each data key of the Analogs TimeSeries corresponds to one analog signal:

```{code-cell} ipython3
c3d_contents["Analogs"].data
```

Let's plot some of them:

```{code-cell} ipython3
c3d_contents["Analogs"].plot(["Left Rectus femoris", "Left Semimembranosus"])
```

## Force platforms

The `ForcePlatforms` TimeSeries contains information regarding all force platforms in the file. In this particular file, there are 6 force platforms, represented as FP0 to FP5:
- The position of the force platforms is given by `FPx_Corner1` to `FPx_Corner4`.
- Their local coordinate systems are given by the `FPx_LCS` transform series.
- Ground reaction forces are given by `Forces`.
- Moments are reported both around the force platform geometrical centre (`FPx_MomentAtCentre`) and at the point of pressure (`FPx_MomentAtCOP`).
- The centre of pressure is reported in `FPx_COP`.

```{code-cell} ipython3
c3d_contents["ForcePlatforms"].data
```

Let's plot the COP on force plates 0:

```{code-cell} ipython3
c3d_contents["ForcePlatforms"].plot('FP0_COP')
```

## Quick visualization

Although visualizing data using the interactive 3D [Player](api/ktk.Player.rst) is explained in section [](player.md), here is how we can quickly visualize the kinematic and kinetic data in this file. Note that every TimeSeries provided to the Player must have the same sampling rate, which means we need to downsample the force platform data to the points sampling rate:

```{code-cell} ipython3
:tags: [skip-execution]

ktk.Player(
    c3d_contents["Points"],
    c3d_contents["ForcePlatforms"].resample(c3d_contents["Points"].time)
)
```

```{code-cell} ipython3
:tags: [remove-input]

%matplotlib qt5

points = c3d_contents["Points"].get_ts_between_times(3, 5)
ktk.Player(
    points,
    c3d_contents["ForcePlatforms"].resample(points.time)
)._to_animation()
```
