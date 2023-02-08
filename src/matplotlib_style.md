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

# 📖 Markers, line style and colours

:::{card} Summary
This section shows how to use markers, line styles and to specify colours when plotting using {{plt_plot}}.
:::

The optional, third argument `fmt` of the `plot` function sets the marker shape, line style and colour. This argument is a string composed of three optional parts:

## Marker

- nothing (no marker)
- `.` dot
- `o` round
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

# Sample data to plot
x = [1.0, 2.0, 3.0, 4.0]
y1 = [1.0, 2.0, 3.0, 1.0]
y2 = [1.0, 3.0, -1.0, 2.0]
y3 = [-1.0, 4.0, -2.0, 2.0]
y4 = [-1.0, -4.0, -3.0, 0.0]
y5 = [2.0, 3.0, -1.0, 1.0]

# Specifying markers
plt.subplot(1, 3, 1)
plt.plot(x, y1, ".")
plt.plot(x, y2, "o")
plt.plot(x, y3, "^")
plt.plot(x, y4, "d")
plt.plot(x, y5, "s")
plt.title("Specifying markers")

# Specifying line styles
plt.subplot(1, 3, 2)
plt.plot(x, y1, "-")
plt.plot(x, y2, "--")
plt.plot(x, y3, "-.")
plt.plot(x, y4, ":")
plt.title("Specifying styles")

# Specifying colours
plt.subplot(1, 3, 3)
plt.plot(x, y1, "r")
plt.plot(x, y2, "g")
plt.plot(x, y3, "b")
plt.plot(x, y4, "c")
plt.plot(x, y4, "m")
plt.title("Specifying colours")

plt.tight_layout()
plt.show()
```

Markers, line styles and colours can be mixed and matched:

```{code-cell} ipython3
plt.plot(x, y1, ".-r")   # dot markers, full line, red
plt.plot(x, y2, "--g")   # no marker, dashed line, green
plt.plot(x, y3, "s-.b")  # square markers, dash-dotted line, blue
plt.plot(x, y4, "oc")    # round markers, no line, cyan

plt.show()
```

## 💪 Exercise

You need to generate the same figure as exercise 2 of section [](matplotlib_plot.md), but it needs to be printed in black and white. To maximize the clarity of the figure, you want to use markers and line styles instead of grey shades.

Here is the data:

```{code-cell} ipython3
# Video camera data
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # meters

# Timing gates data (placed at positions 0m, 25m, 50m, 75m and 100m)
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]  # seconds
```

and here is the original figure:

```{code-cell} ipython3
:tags: [remove-input]

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.show()
```

Generate this figure, but with these style specifications:

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

plt.show()
```
