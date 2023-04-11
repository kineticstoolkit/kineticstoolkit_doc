---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```


# 💪 Exercise 3

You recorded a noisy signal:

```
signal = np.array(
    [
        0.436, 0.493, 0.467, 0.467, 0.482, 0.497, 0.474, 0.493, 0.474, 0.467,
        0.470, 0.455, 0.482, 0.501, 0.470, 0.482, 0.467, 0.467, 0.558, 0.413,
        0.463, 0.444, 0.463, 0.417, 0.528, 0.455, 0.486, 0.459, 0.490, 0.459,
    ]
)
```

```{code-cell} ipython3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

signal = np.array(
    [
        0.436,
        0.493,
        0.467,
        0.467,
        0.482,
        0.497,
        0.474,
        0.493,
        0.474,
        0.467,
        0.470,
        0.455,
        0.482,
        0.501,
        0.470,
        0.482,
        0.467,
        0.467,
        0.558,
        0.413,
        0.463,
        0.444,
        0.463,
        0.417,
        0.528,
        0.455,
        0.486,
        0.459,
        0.490,
        0.459,
        0.467,
    ]
)
plt.plot(signal)
plt.show()
```

You want to smooth this signal using a moving average with a window of three samples. This means that you want to create a new array where each value is the average of the three neighbour values of the raw signal:

![Moving average -width:wide](_static/images/moving_average.png)

Using only one line, apply such a filter on the raw, noisy signal. Then, plot both the raw and filtered signal on the same figure to verify your result.

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np
import matplotlib.pyplot as plt


filtered = (signal[0:-2] + signal[1:-1] + signal[2:]) / 3

plt.plot(signal, label="raw")
plt.plot(filtered, label="filtered")
plt.legend()
plt.show()
```

