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

# Electromyography

This dataset contains the raw electromyographic signal for the right biceps brachii during cyclic contraction/relaxing movements, recorded at the [Mobility and Adaptive Sports Research Lab](https://felixchenier.uqam.ca) using a surface electrode (Delsys Trigno).

## Files

- `emg_biceps_brachii.csv`: CSV file with two columns: time and data in volts.

```{code-cell}
import kineticstoolkit.lab as ktk
import pandas as pd

filename = ktk.doc.download("emg_biceps_brachii.csv")
dataframe = pd.read_csv(filename, index_col="Time")

dataframe.plot();
```

- `emg_biceps_brachii.ktk.zip`: The same data as a TimeSeries, interpolated on a constant sample rate.

```{code-cell}
filename = ktk.doc.download("emg_biceps_brachii.ktk.zip")
ts = ktk.load(filename)

ts
```

