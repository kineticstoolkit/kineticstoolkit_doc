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

The optional, third argument `fmt` of the {{plt_plot}} function defines optional markers, line styles and line colours. This argument is a string composed of these characters:

::::{grid}
:::{grid-item-card} Marker
:columns: 4

- `.` dot
- `o` round
- `x` cross (x)
- `+` cross (+)
- `^` triangle
- `d` diamond
- `s` square

By default, no marker is plotted.

:::

:::{grid-item-card} Line style
:columns: 4

- `-` full line
- `--` dashed line
- `-.` dash-dotted line
- `:` dotted line

Default is a full line, unless a marker has been set, in which case the default is no line.

:::

:::{grid-item-card} Colour
:columns: 4

- `r` red
- `g` green
- `b` blue
- `c` cyan
- `m` magenta
- `y` dark yellow
- `w` white
- `k` black

Default is the next colour in the current colour cycle.

:::
::::

Here are some examples:

```{code-cell} ipython3
import matplotlib.pyplot as plt

y = [0.0, 1.0, -1.0, 2.0, 0.5, 0.0]

plt.subplot(2, 2, 1)
plt.plot(y, ".-r")
plt.title("dot markers, full line, red")

plt.subplot(2, 2, 2)
plt.plot(y, "--g")
plt.title("no marker, dashed line, green")

plt.subplot(2, 2, 3)
plt.plot(y, "s-.b")
plt.title("square markers, dash-dotted line, blue")

plt.subplot(2, 2, 4)
plt.plot(y, "oc")
plt.title("round markers, no line, cyan")

plt.tight_layout()

plt.show()
```
