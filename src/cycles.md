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

# 📖 Working with cycles

:::{card} Summary
This section shows the [](api/ktk.cycles.rst) module, which detects cycles in TimeSeries, time-normalizes these cycles, finds the most repeatable ones, and stack/ unstack them.
:::

Since many movements are cyclic (e.g., gait), it is often useful to identify these cycles and work on a per-cycle basis instead of long acquisitions. The [](api/ktk.cycles.rst) module provides some functions to detect, time-normalize and stack cycles, and to find the most repeatable cycles among a set of stacked cycles.

This section showcases this module, using kinetics data from wheelchair propulsion.


```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the instrumented wheel data

ts = ktk.load(ktk.doc.download("wheelchair_kinetics.ktk.zip"))
```

At this point, we have a TimeSeries that contains several signals, including forces and moments.

```{code-cell} ipython3
plt.subplot(2, 1, 1)
ts.plot("Forces")
plt.subplot(2, 1, 2)
ts.plot("Moments")
```

## 📄 Detecting cycles

The [](api/ktk.cycles.detect_cycles.rst) function detects biphasic cycles in a TimeSeries, and add the transitions as events. Each cycle has three events:
- The start of the first phase, named using the `event_names` parameters;
- The start of the second phase, also named using the `event_names` parameters;
- The end of the cycle, always named `_`.

The function does not modify the TimeSeries data, only the events. It uses two thresholds applied to one, unidimensional signal from this TimeSeries. In this example, this signal will be the total force $F_{tot}$. This could also apply to gait, or one could also use only the vertical ground reaction force, depending on the lab's convention or methods.

Let's calculate $F_{tot}$ based on the three force components, and add it as a new data of the TimeSeries.

```{code-cell} ipython3
# Calculate Ftot
ts.data["Ftot"] = np.sqrt(np.sum(ts.data["Forces"] ** 2, axis=1))

# Plot it
ts.plot(["Forces", "Ftot"])
```

We then define threshold values for $F_\text{tot}$. While we could use a single threshold value (e.g., everything above 12 N corresponds to a push, everything below 12 N corresponds to a recovery), it is generally more robust to use two thresholds: one (higher) that registers the beginning of a push, and another (lower) that registers the beginning of a recovery. This method is more robust to noise: it won't register a cycle simply because the signal moves around the threshold during the transitions.

```{code-cell} ipython3
test = ktk.cycles.detect_cycles(
    ts, "Ftot", event_names=["push", "recovery"], thresholds=[10, 5]
)
test.plot(["Forces", "Ftot"])
```

We observe that most cycles are well identified, but a short spike at the beginning was wrongly identified as a cycle. In reality, this is a synchronization spike used to sync data between many instruments. We can reject detected cycles that are deemed to short by specifying minimal durations for both phases.

```{code-cell} ipython3
test = ktk.cycles.detect_cycles(
    ts,
    "Ftot",
    event_names=["push", "recovery"],
    thresholds=[10, 5],
    min_durations=[0.2, 0.2],
)
test.plot(["Forces", "Ftot"])
```

There are other arguments available to filter out more cycles, such as max durations, and minimal/maximal peak height. The [API](api/ktk.cycles.detect_cycles.rst) describes these arguments thoughtfully.

For example, in this signal, the next to last cycle corresponds to a braking phase and we may want to remove it. For this very signal, this can be done using a minimal peak height requirement:

```{code-cell} ipython3
ts_with_events = ktk.cycles.detect_cycles(
    ts,
    "Ftot",
    event_names=["push", "recovery"],
    thresholds=[10, 5],
    min_durations=[0.2, 0.2],
    min_peak_heights=[50, -np.Inf],
)
ts_with_events.plot(["Forces", "Ftot"])
plt.tight_layout()
```

We observe an `_` event at about 27 seconds. There are in fact such `_` events at the end of each cycle (look how each next push's 'p' letter seems underlined). As explained above, the `detect_cycles` function adds an `_` event at the end of each cycle; the one at 27 seconds just happens to not correspond to the begin of a new cycle.

## 📄 Time-normalizing cycles

Once the cycles have been detected, we can time-normalize them using [](api/ktk.cycles.time_normalize.rst) to get them on the same time scale (a percentage of the cycle).

Here, every 12 complete cycles will be time-normalized from 0 to 100%, with a new cycle starting at every multiple of 100%:

```{code-cell} ipython3
ts_normalized_on_cycle = ktk.cycles.time_normalize(
    ts_with_events, event_name1="push", event_name2="_"
)

plt.subplot(2, 1, 1)
ts_normalized_on_cycle.plot(["Forces", "Ftot"])
plt.subplot(2, 1, 2)
ts_normalized_on_cycle.plot("Moments")
plt.tight_layout()
```

To time-normalize only during the push phase, we would define `event_name2` as "recovery" instead of " _ ". Note in the original data that we had a total of 12 complete transitions from "push" to " _ ". The end of the last cycle could not be identified since no new push started after.

If we are only interested in transitions from "push" to "recovery", then we have a total of **13** complete pushes:

```{code-cell} ipython3
ts_normalized_on_push = ktk.cycles.time_normalize(
    ts_with_events, "push", "recovery"
)

plt.subplot(2, 1, 1)
ts_normalized_on_push.plot(["Forces", "Ftot"])
plt.subplot(2, 1, 2)
ts_normalized_on_push.plot("Moments")
plt.tight_layout()
```

It is also possible to include data before 0% and after 100% using the `span` parameter. For example, to include pre-push (-25% to 0%) and post-recovery (100% to 125%):

```{code-cell} ipython3
ts_normalized_on_push_with_span = ktk.cycles.time_normalize(
    ts_with_events, "push", "recovery", span=[-20, 125]
)
plt.subplot(2, 1, 1)
ts_normalized_on_push_with_span.plot(["Forces", "Ftot"])
plt.subplot(2, 1, 2)
ts_normalized_on_push_with_span.plot("Moments")
plt.tight_layout()
```

In this case, each time point still represents 1% of a cycle, but the TimeSeries wrap every 145 points (0 to 19 is the pre-push for the first cycle, 20 to 119 is the first push, 120 to 144 is the post-release for the first cycle, etc.).

## 📄 Combining the cycles

Cycles are often analyzed together, and it makes sense to construct a numpy array of higher dimension, where instead of having a first dimension that represents both the cycle and percentage of cycle, we would have a first dimension that represents the cycle, and second that represents the percentage of cycle. This is done using the [](api/ktk.cycles.stack.rst) function.

Let's stack the data from the last computed TimeSeries (without pre-push and post-recovery).

```{code-cell} ipython3
data = ktk.cycles.stack(ts_normalized_on_push)

data
```

The first dimension of each dictionary's entry corresponds to the cycles. It now becomes easier to perform operations on cycles. For example, to plot the propulsive moment `Mz` (`Moments[2]`) in each cycle one of top of the other:

```{code-cell} ipython3
# Plot every cycles
for i_cycle in range(13):
    plt.plot(data["Ftot"][i_cycle], label=f"Cycle {i_cycle}")

# Plot the average cycle
plt.plot(np.mean(data["Ftot"], axis=0), "k:", linewidth=4, label="Average")

plt.legend()
```

## 📄 Finding the most repeatable cycles

In the previous step, we calculated an average cycle. However, this average cycle was calculated on cycles that were very different between each other. We can use the [](api/ktk.cycles.most_repeatable_cycles.rst) function to obtain an ordered list from the most repeatable cycles to the most different one. The algorithm is explained in the [API](api/ktk.cycles.most_repeatable_cycles.rst). Here, we will base this analysis on the `Ftot` signal.

```{code-cell} ipython3
index = ktk.cycles.most_repeatable_cycles(data["Ftot"])

index
```

We see that cycles 12 (last) and 0 (first) were expectedly found as the least repeatable pushes since they are respectively a last push and an acceleration push. Now let's make the same plot of `Mz`, but based only on the five most repeatable cycles.

```{code-cell} ipython3
# Plot every cycles
for i_cycle in index[0:5]:
    plt.plot(data["Ftot"][i_cycle], label=f"Cycle {i_cycle}")

# Plot the average cycle
plt.plot(
    np.mean(data["Ftot"][index[0:5]], axis=0),
    "k:",
    linewidth=4,
    label="Average",
)

plt.legend()
```

For more information on cycles, please check the [API Reference for the cycles module](api/ktk.cycles.rst).
