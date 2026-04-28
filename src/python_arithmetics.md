---
kernelspec:
  name: python3
---

# Arithmetic operations

Any arithmetic operation is performed simply by writing its equation. For example, the most common arithmetic operators are `+`, `-`, `*`, `/` and `**`. We use parentheses `()` to indicate operation priority.

:::::{grid} 1 2 2 2

::::{card} Addition
```python
4 + 3
```
::::

::::{card} Subtraction
```python
4 - 3
```
::::

::::{card} Multiplication
```python
4 * 3
```
::::

::::{card} Division
```python
4 / 3
```
::::

::::{card} Exponent
To raise a value to a power (e.g., to calculate $4^2$), we would write:

```python
4 ** 2
```
::::

::::{grid-item-card} Root
For roots, we can exponentiate to the inverse. For example, to calculate $\sqrt{4}$, we would write:

```python
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
