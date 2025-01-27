# Analyzing time-varying data

In biomechanics, we often process data that is a function of time, e.g., electromyography, marker trajectories, force series, etc. When we analyze only a few data points and the sampling frequency is constant, using NumPy is usually sufficient. This is what we did in the last section in the different [NumPy exercises](numpy_exercises.md).

However, things can get more complicated when:
- data are of different natures, such as marker trajectories, EMG, measured forces, calculated forces, etc.;
- data were recorded by unsynchronized instruments at different sampling frequencies;
- data were recorded with inconstant sample frequencies;
- data are missing (e.g., occluded markers);
- data are noisy;
- etc.

For these reasons, Kinetics Toolkit provides a new type of variable: the [TimeSeries](api/ktk.TimeSeries.rst).

**Chapter Contents**

```{tableofcontents}
```
