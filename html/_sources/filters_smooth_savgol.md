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

# Moving average and Savitsky-Golay

This section presents the following functions:
- [ktk.filters.smooth](api/ktk.filters.smooth.rst)
- [ktk.filters.savgol](api/ktk.filters.savgol.rst).

## Smoothing using a moving average

The moving average is an excellent filter to remove noise that is related to a specific time pattern. A classic example is the day-to-day evaluation of a process that is sensible to week-ends (for example, the number of workers who enter a building). A moving average with a window length of 7 days is ideal to evaluate the generic trend of this signal without considering intra-week fluctuations. Let's first load some noisy data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("filters_types_of_noise.ktk.zip"))

ts.plot(["clean", "periodic_noise"], '.-')
```

This signal contains periodic noise with a period of five seconds. Using a 5-second moving average filter:

```{code-cell} ipython3
filtered = ktk.filters.smooth(ts, window_length=5)
```

gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("periodic_noise", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "periodic_noise", "filtered"], '.-')
```

As expected, the 5-sample period noise was completely removed. The signal was however also averaged and we therefore lost some dynamics in the signal.


## Smoothing using a Savitzky-Golay filter

The Savitzky-Golay filter is a generalization of the moving average. Instead of taking the mean of the n points of a moving window, the Savitzky-Golay filter fits a polynomial of a given order over each window. A moving average is therefore a particular case of Savitzky-Golay filter with a polynomial of order 0.

It is a powerful filter for data that is heavily quantized, particularly if we want to derivate these data. Let's plot some heavily quantized data:

```{code-cell} ipython3
ts.plot(["clean", "quantized"], ".-")
```

To smooth this signal using a second-order Savitzky-Golay filter with a window length of 7:

```{code-cell} ipython3
filtered = ktk.filters.savgol(ts, poly_order=2, window_length=7)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("quantized", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "quantized", "filtered"], '.-')
```

## Deriving using a Savitzky-Golay filter

Heavily quantized signals are often difficult to derivate because they contain lors of plateaus that, once derived, are transformed to series of spikes. For instance, let's see how deriving a quantized signal works withouth filtering, using [ktk.filters.deriv](api/ktk.filters.deriv.rst):

```{code-cell} ipython3
derived = ktk.filters.deriv(ts)

derived.plot(["clean", "quantized"], ".-")
```

Deriving using a Savitzky-Golay filter consists in deriving the polynomial that is fitted over the moving window. Using a 2nd-order Savitzky-Golay filter with a window length of 7:

```{code-cell} ipython3
derived_savgol = ktk.filters.savgol(
    ts, poly_order=2, window_length=7, deriv=1
)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
derived.rename_data("clean", "derivative of the clean signal", in_place=True)
derived.rename_data("quantized", "derived from quantized signal, without filtering", in_place=True)
derived_savgol.rename_data("quantized", "derived from quantized signal, using savgol", in_place=True)
derived_savgol.resample(derived.time, fill_value="extrap", in_place=True)
derived.merge(derived_savgol).plot(
    [
        "derivative of the clean signal",
        "derived from quantized signal, without filtering",
        "derived from quantized signal, using savgol",
    ],
    '.-'
)
```

As observed, the derivative of the highly-quantized signal is similar to the derivative of the clean signal.
