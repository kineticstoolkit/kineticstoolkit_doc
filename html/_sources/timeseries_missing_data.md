---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]
%matplotlib inline
```

# Missing data

This section shows how to use these methods:

- [ktk.TimeSeries.isnan](api/ktk.TimeSeries.isnan.rst)
- [ktk.TimeSeries.fill_missing_samples](api/ktk.TimeSeries.fill_missing_samples.rst)

It happens regularly that we record suboptimal data, which may include missing samples. For instance, in [these kinematic data of tennis serve](dataset_kinematics_tennis_serve.md), the marker on the right shoulder dissapears regularly:

```{code-cell}
import kineticstoolkit.lab as ktk
import numpy as np


filename = ktk.doc.download("kinematics_tennis_serve_nan.c3d")
markers = ktk.read_c3d(filename)["Points"]
markers.plot("Derrick:RSHO")
```


## Finding missing samples

Similarly to NumPy's {{np_isnan}} function, TimeSeries provide the [ktk.geometry.isnan](api/ktk.geometry.isnan.rst) method that returns which samples are missing as a list of bool:

```{code-cell}
is_missing = markers.isnan("Derrick:RSHO")
```

Using {{np_nonzero}}, the list of missing indexes is:

```{code-cell}
np.nonzero(is_missing)
```

## Filling missing samples

If the gaps are not too wide, we can fill these gaps using [ktk.TimeSeries.fill_missing_samples](api/ktk.TimeSeries.fill_missing_samples.rst):

```{code-cell}
filled_markers = markers.fill_missing_samples(
    max_missing_samples=20
)

filled_markers.plot("Derrick:RSHO")
```

We see in the figure above that any gap larger than 20 samples has been left untouched. It is always a good idea to set such as maximal gap according to the sampling rate and movement being recorded, so that we do not interpolate too much and create invalid data.

Now, look at the blue curve. The default linear interpolation method was not optimal for these data, as it introduces obvious discontinuities in the signal. We may opt for another method, such as a cubic spline:

```{code-cell}
filled_markers = markers.fill_missing_samples(
    max_missing_samples=20,
    method="cubic",
)

filled_markers.plot("Derrick:RSHO")
```
