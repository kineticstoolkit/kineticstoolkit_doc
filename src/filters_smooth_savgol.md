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

# 📖 Moving average and Savitsky-Golay

:::{card} Summary
This section shows how to smooth a noisy signal using [ktk.filters.smooth](api/ktk.filters.smooth.rst), or how to smooth and derivate a noisy signal using the more generic [ktk.filters.savgol](api/ktk.filters.savgol.rst) function.
:::


## ⚙️ Example 1: Smoothing using a moving average

The moving average is an excellent filter to remove noise that is related to a specific time pattern. A classic example is the day-to-day evaluation of a process that is sensible to week-ends (for example, the number of workers who enter a building). A moving average with a window length of 7 days is ideal to evaluate the generic trend of this signal without considering intra-week fluctuations. Although its use in biomechanics is less obvious, this filter may be useful in some situation. Let's first load some noisy data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("filters_types_of_noise.ktk.zip"))

# Plot it
ts.plot(["clean", "periodic_noise"], marker=".")
plt.grid(True)
plt.tight_layout()
```

In this signal, we observe that appart from random noise, there seems to be a periodic signal with a period of five seconds, that we may consider as noise. Since it has a constant period, the moving average is a nice candidate for filtering out this noise.

```{code-cell} ipython3
filtered = ktk.filters.smooth(ts, window_length=5)

ts.plot(["clean", "periodic_noise"], marker=".")

filtered.plot("periodic_noise", marker=".", color="k")

plt.title("Removing the fast, constant rate variation (black curve)")
plt.grid(True)
plt.tight_layout()
```

As expected, the 5-sample period noise was completely removed. The signal was however also averaged and we therefore lost some dynamics in the signal.


## ⚙️ Example 2: Smoothing using a Savitzky-Golay filter

The Savitzky-Golay filter is a generalization of the moving average. Instead of taking the mean of the n points of a moving window, the Savitzky-Golay filter fits a polynomial of a given order over each window (a moving average is therefore a Savitzky-Golay filter with a polynomial of order 0).

It is a powerful filter for data that is heavily quantized, particularly if we want to derivate these data. Let's plot some heavily quantized data:

```{code-cell} ipython3
ts = ktk.load(ktk.doc.download("filters_types_of_noise.ktk.zip"))

# Plot it
ts.plot(["clean", "quantized"], marker=".")
plt.grid(True)
plt.tight_layout()
```

Smoothing this signal using a second-order Savitzky-Golay filter with a window length of 7:

```{code-cell} ipython3
filtered = ktk.filters.savgol(ts, poly_order=2, window_length=7)

ts.plot(["clean", "quantized"], marker=".", linestyle="--")
filtered.plot(["quantized"], marker=".", color="k")

plt.title(
    "Smoothed signal using a Savitzky-Golay filter of order=2 and window_length=7"
)
plt.grid(True)
plt.tight_layout()
```

## ⚙️ Example 3: Deriving using a Savitzky-Golay filter

This sort of signal that suffers from bad resolution is very difficult to derivate because it is filled with fast-changing plateaus that, once derived, are transformed to series of spikes. Let's see the result with a bare derivation without filtering, using [ktk.filters.deriv](api/ktk.filters.deriv.rst):

```{code-cell} ipython3
# Try to derivate
derivate = ktk.filters.deriv(ts)

# Plot it
derivate.plot(["clean", "quantized"], marker=".")
plt.grid(True)
plt.tight_layout()
```

Since the Savitzky-Golay filter fits a polynomial instead of just smoothing the signal, then the derivative of the filtered signal is automatically given by deriving the polynomial instead of the signal. Let's see how deriving the quantized signal using a 2nd-order Savitzky-Golay filter with a window length of 7 compares to deriving the original, clean signal:

```{code-cell} ipython3
# Filter and derivate the noisy signal
derivate_savgol = ktk.filters.savgol(
    ts, poly_order=2, window_length=7, deriv=1
)

# Plot the derivative of the clean signal
derivate.plot(["clean", "quantized"], marker=".", linestyle="--")

# Plot the filtered derivative of the quantized signal
derivate_savgol.plot("quantized", marker=".", color="k")

plt.title(
    "Derived signal using a Savitzky-Golay filter of order=2 and window_length=7 (black)"
)
plt.grid(True)
plt.tight_layout()
```

As observed, the derivative of the highly-quantized signal is very similar to the derivative of the clean signal.
