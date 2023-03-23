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
