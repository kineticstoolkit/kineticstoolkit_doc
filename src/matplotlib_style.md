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

# Markers, line style and colours

:::{card} Summary
This section shows how to use markers, line styles and to specify colours when plotting using {{plt_plot}}.
:::

The optional, third argument `fmt` of the {{plt_plot}} function sets markers, line styles and line colours. This argument is a string composed of these characters:

## Marker

- nothing (no marker)
- `.` dot
- `o` round
- `x` cross (x)
- `+` cross (+)
- `^` triangle
- `d` diamond
- `s` square

## Line style

- nothing (full line, or no line if there is no marker)
- `-` full line
- `--` dashed line
- `-.` dash-dotted line
- `:` dotted line

## Colour

- nothing (next colour in the colour cycle)
- `r` red
- `g` green
- `b` blue
- `c` cyan
- `m` magenta
- `y` dark yellow
- `w` white
- `k` black

Here are some examples:

```{code-cell} ipython3
import matplotlib.pyplot as plt

y = [0.0, 1.0, -1.0, 2.0, 0.5, 0.0]

plt.subplot(4, 1, 1)
plt.plot(y, ".-r")  # dot markers, full line, red
plt.subplot(4, 1, 2)
plt.plot(y, "--g")  # no marker, dashed line, green
plt.subplot(4, 1, 3)
plt.plot(y, "s-.b")  # square markers, dash-dotted line, blue
plt.subplot(4, 1, 4)
plt.plot(y, "oc")  # round markers, no line, cyan
plt.tight_layout()

plt.show()
```

## 💪 Exercise

In section [](matplotlib_plot.md), using these data:

```{code-cell} ipython3
# Video camera data
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # meters

# Timing gates data (placed at positions 0m, 25m, 50m, 75m and 100m)
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]  # seconds
```

you generated the following figure:

```{code-cell} ipython3
:tags: [remove-input]

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True)
plt.show()
```

You now need to print it in black and white. To maximize the clarity of the figure, you want to use markers and line styles instead of grey shades.

Generate this figure again, but this time with these specifications:

- The video camera curve must be a full, black line with square markers;
- The timing gates curve must be a dashed, black line with round markers.

```{code-cell} ipython3
:tags: [hide-cell]

plt.plot(t, p, "s-k")
plt.plot(timing_gates_time, [0, 25, 50, 75, 100], "o--k")
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True)

plt.show()
```
