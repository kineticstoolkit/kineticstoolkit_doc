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

# Exercise: Segmenting TimeSeries

Using this dataset of [kinetic data during wheelchair propulsion](dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

Write a code that generates a list of three floats named `peak_Mz`, that includes the peak moment (`Moments[:, 2]`) during each of the three first pushes.

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np

# Init the list
peak_Mz = []

# Fill the list
for i_push in range(3):
    # Extract a new TimeSeries that only spans this push
    sub_ts = ts.get_ts_between_events("push", "recovery", i_push, i_push)

    # Calculate the peak moment on this new TimeSeries and happen it to
    # the list
    peak_Mz.append(np.max(sub_ts.data["Moments"][:, 2]))

# Print it!
print(peak_Mz)
```