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

# Exercise: Filtering EMG data

Using this [dataset](dataset_emg.md) with one surface EMG electrode on the biceps brachii:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

filename = ktk.doc.download("emg_biceps_brachii.ktk.zip")
emg = ktk.load(filename)
emg.plot()
```

Write a code that generates a new data named "Envelope" in the TimeSeries, that corresponds to the envelope of this signal. Follow these three steps:
1. Filter the TimeSeries with a band-pass butterworth filter from 20 Hz to 500 Hz to reject high frequency noise and body movement artifacts.

```{code-cell} ipython3
:tags: [hide-cell]

filtered_emg = ktk.filters.butter(emg, btype="bandpass", fc=[20, 500])
filtered_emg.plot()
```

2. Rectify the filtered TimeSeries, by replacing every data by its absolute value. You may use {{np_abs}}.

```{code-cell} ipython3
:tags: [hide-cell]

filtered_emg.data["BicepsBrachiiR"] = np.abs(filtered_emg.data["BicepsBrachiiR"])
filtered_emg.plot()
```

3. Filter the rectified TimeSeries with a low-pass butterworth filter with a cut-off frequency of 10 Hz.

```{code-cell} ipython3
:tags: [hide-cell]

filtered_emg = ktk.filters.butter(filtered_emg, fc=10)

# Add the filtered signal as Envelope in the original TimeSeries
# There are many ways to do this, here is a robust one:
filtered_emg = filtered_emg.rename_data("BicepsBrachiiR", "Envelope")
emg = emg.merge(filtered_emg)

# Plot the result
emg.plot()
```
