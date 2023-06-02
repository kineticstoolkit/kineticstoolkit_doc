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

# Reading C3D files

Let's first download a sample C3D file. This file is provided by https://www.c3d.org as a test suite for C3D software development:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

filename = ktk.doc.download("c3d_test_suite_sample.c3d")
```

We now read it using [ktk.read_c3d](api/ktk.read_c3d.rst):

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

+++

## Points

Each data key of the Points TimeSeries corresponds to one point (marker):

```{code-cell} ipython3
c3d_contents["Points"].data
```

We will learn how to visualize these markers using an interactive player in [](player). For now, let's plot some of them:

```{code-cell} ipython3
c3d_contents["Points"].plot(["LFT1", "RFT1"])
```

## Analogs

Each data key of the Analogs TimeSeries corresponds to one analog signal:

```{code-cell} ipython3
c3d_contents["Analogs"].data
```

Let's plot some of them:

```{code-cell} ipython3
c3d_contents["Analogs"].plot(["FZ1", "FZ2"])
```
