---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Arithmetic operations

Any arithmetic operation is performed simply by writing its equation. For example, the most common arithmetic operators are `+`, `-`, `*`, `/` and `**`. We use parentheses `()` to indicate operation priority.

:::::{grid}
:gutter: 2

::::{grid-item-card} Addition
:columns: 6
```
4 + 3
```
::::

::::{grid-item-card} Subtraction
:columns: 6
```
4 - 3
```
::::

::::{grid-item-card} Multiplication
:columns: 6
```
4 * 3
```
::::

::::{grid-item-card} Division
:columns: 6
```
4 / 3
```
::::

::::{grid-item-card} Exponent
:columns: 6
To raise a value to a power (e.g., to calculate $4^2$), we would write:

```
4 ** 2
```
::::

::::{grid-item-card} Root
:columns: 6
For roots, we can exponentiate to the inverse. For example, to calculate $\sqrt{4}$, we would write:

```
4 ** (1 / 2)
```
::::

:::::


As an exercise, type one line in the console that performs this operation:

$$\left( \frac{3+5}{6-4} \right)^2$$

```{code-cell}
:tags: [hide-cell]
((3 + 5) / (6 - 4)) ** 2
```
