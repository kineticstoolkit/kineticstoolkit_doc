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

# Butterworth filter

The Butterworth filter may be the most used filter in biomechanics. It removes ranges of frequencies from the signal's frequency spectrum. Normally, we first identify the frequency range of our data, so that we can remove any signal frequencies outside this range.

Let's start by loading some noisy data.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts_noisy = ktk.load(ktk.doc.download("filters_noisy_signals.ktk.zip"))

ts_noisy.plot();
```

## Low-pass filter

The default setting for [ktk.filters.butter](api/ktk.filters.butter.rst) is to apply a low-pass, no-lag filter of order 2. To filter with a cut-off frequency of 20 Hz:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, fc=20)
ts_filtered.plot()
```

You are encouraged to experiment with different cut-off frequencies to observe its effect on the results. In the figure above, we observed that while 20 Hz was probably correct for the sine wave, it still filtered out the most dynamic components, most notably in the square and pulse signals.

## High-pass filter

The inverse operation is the high-pass filter. Let's observe what we removed from the original signal in the figure above:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, btype="highpass", fc=20)
ts_filtered.plot()
```

Only the transitions were kept; all the stable parts of the signal were removed.

## Band-pass filter

We can combine both low-pass and high-pass in a band-pass filter. This type of filter is commonly used in processing of electromyography, to filter both high-frequency noise and low-frequency movement artifact.

To remove frequencies between 10 and 80 Hz:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, btype="bandpass", fc=[10, 80])
ts_filtered.plot()
```
