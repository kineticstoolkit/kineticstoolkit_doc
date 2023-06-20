---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Exercise: Indexing and slicing unidimensional arrays

You used an accelerometer to detect a small movement. The acceleration returned by the instrument is expressed by this list, at a sampling frequency of 100 Hz.

```{code-cell} ipython3
acc = [0.01, 0.01, 0.00, 0.00, 0.02, 0.77, 0.82, 0.86, 0.81, 0.74, 0.07, 0.02]
```

```{code-cell} ipython3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

acc = np.array(acc)
time = np.arange(acc.shape[0]) / 100

plt.plot(time, acc, "o-r")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration")
plt.grid(True);
```

However, by carefully inspecting your signal, you realize that the data is late by 40 milliseconds. You want to fix this delay, but you also want to keep the same number of samples in your signal.

- Using NumPy slicing, write a code that moves forward every data by 40 ms.
- Fill the missing data at the end with zeros.

In summary, you want to produce the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]

new_acc = acc.copy()
new_acc[0:-4] = acc[4:]
new_acc[-5:] = 0

time = np.arange(acc.shape[0]) / 100
fig = plt.figure()
plt.plot(time, acc, "o-r")
plt.plot(time, new_acc, "o--b")
plt.plot(
    np.array([5, 2, 3, 2, 3, 2, 5]) / 100,
    [0.4, 0.4, 0.5, 0.4, 0.3, 0.4, 0.4],
    "k",
    linewidth=5,
)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration")
plt.grid(True);
```

::::{tip}

:::{toggle}
Do not forget to convert the list to an array.
:::

:::{toggle}
Separate the problem in two separate steps. First shift the signal, then fill the rest of the signal with zeroes. It is suggested to plot the intermediary result between both steps.
:::

:::{toggle}
Shifting the signal is equivalent to reading a certain portion of the signal, and then assign this portion to another portion of the signal.
:::

::::

```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np
import matplotlib.pyplot as plt


# Convert acc to an array
acc = np.array(acc)

# We will plot intermediary steps, to better visualize what we do.
plt.subplot(1, 3, 1)
plt.plot(acc, "o-")
plt.title("Original signal")

# STEP 1 - Shift the signal.
#
# At 100 Hz, the sampling period is 1/100 = 0.01. Therefore, 40 ms is 4 samples.
# We need to shift the acceleration by -4 samples. In other words, we need to
# assign acc[from sample 4 to the end] to acc[from sample 0 to the end-4]
acc[:-4] = acc[4:]

# Plot the new signal
plt.subplot(1, 3, 2)
plt.plot(acc, "o-")
plt.title("Shifted signal")

# STEP 2 - Fill the rest with zeros
acc[-4:] = 0

# Let's see the result
plt.subplot(1, 3, 3)
plt.plot(acc, "o-")
plt.title("End result")

plt.tight_layout();
```
