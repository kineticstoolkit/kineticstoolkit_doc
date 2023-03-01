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

# 📖 Butterworth filter

:::{card} Summary
This section shows how to remove specific ranges of frequencies from a TimeSeries using [ktk.filters.butter](api/ktk.filters.butter.rst).
:::

The Butterworth filter may be the most used filter in biomechanics. It removes ranges of frequencies from the signal's frequency spectrum. Normally, we first identify the frequency range of our data, so that we can remove any signal outside this range. This removes noise, without removing information from the data.

The following section will show different use cases for the [ktk.filters.butter](api/ktk.filters.butter.rst) function. Let's start by loading some noisy data.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts_noisy = ktk.load(ktk.doc.download("filters_noisy_signals.ktk.zip"))

ts_noisy.plot()
plt.title("Noisy signals")
plt.tight_layout()
```

## ⚙️ Example 1: Low-pass, no-lag filter

Here is what we get if we filter out higher frequencies using a no-lag Butterworth filter of order 2:

```{code-cell} ipython3
plt.subplot(1, 3, 1)
ts_noisy.plot()
plt.title("Before filtering")

plt.subplot(1, 3, 2)
temp = ktk.filters.butter(ts_noisy, fc=20)
temp.plot()
plt.title("Low-pass 2nd order at 20 Hz")
plt.tight_layout()

plt.subplot(1, 3, 3)
temp = ktk.filters.butter(ts_noisy, fc=4)
temp.plot()
plt.title("Low-pass 2nd order at 4 Hz")
plt.tight_layout()
```

As expected, when filtering lower frequencies, the signal is clearer but transitions are less sharp and the most dynamic information may be lost.

## ⚙️ Example 2: High-pass, no-lag filter

Here is what we get if we filter out lower frequencies using a no-lag Butterworth filter of order 2.

```{code-cell} ipython3
plt.subplot(1, 2, 1)
ts_noisy.plot()
plt.title("Before filtering")

plt.subplot(1, 2, 2)
temp = ktk.filters.butter(ts_noisy, btype="highpass", fc=60)
temp.plot()
plt.title("High-pass 2nd order at 60 Hz")
plt.tight_layout()
```

Only the transitions are kept, all the stable parts of the signal were removed.
