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

# 📖 Arithmetics and variables

:::{card} Summary
This section covers basic arithmetics (`+`, `-`, `*`, `/`) and variables.
:::

## 📄 Arithmetic operations

Any arithmetical operation is performed simply by writing its equation. For example, the most usual arithmetic operators are `+`, `-`, `*` and `/`:

```{code-cell} ipython3
4 + 3
```

```{code-cell} ipython3
4 - 3
```

```{code-cell} ipython3
4 * 3
```

```{code-cell} ipython3
4 / 3
```

## 📄 Variables

The variable is a fundamental concept in programming. It is a space in memory where we store a value. In python, contrarily to other, static programming languages, there is no need to declare or allocate variables before using them. If we need a variable to store a value, we just define a name and assign a value to it using the `=` operator. For example, we could have two variables, `a` and `b`, that both store a different number:

```{code-cell} ipython3
a = 4
b = 3
```

Now, we can refer to the value of a variable by referring to the variable name:

```{code-cell} ipython3
a + 1
```

```{code-cell} ipython3
a + b
```

We can even assign the result of an operation to a new variable:

```{code-cell} ipython3
c = a + b
print(c)
```

Keep in mind that in the last example, we did not tell to python that `c` must always be equal to `a + b`. This is not how a sequential programming language such as python works. Instead, we ask python, at this very instant, to calculate the result of `a + b` and to store it in a new variable `c`. The sequential nature of python (and many other languages) is illustrated with this example:

```{code-cell} ipython3
c = c + 1
print(c)
```

As with the previous example, we told python to calculate the result of `c + 1` and to store it in the variable `c`.

:::{tip}
The exemple above could be written in a shorter form using the increment `+=` operator. This notation is very common and may help avoid typos in more complex statements. For example, this statement that includes nested [lists](python_lists.md) and [dicts](python_dicts.md):

```
the_list[0]['first_try'][5] = the_list[0]['first_try'][5] + 2
```

would become:

```
the_list[0]['first_try'][5] += 2
```

which is simpler since the complex part of the code is written only once.

These shorthands exist for every arithmetical operation, such as:

```
a += b      # equivalent to a = a + b
a -= b      # equivalent to a = a - b
a *= b      # equivalent to a = a * b
a /= b      # equivalent to a = a / b
```
:::


:::{good-practice} Variable names
It is generally a good idea to use names rather than letters for variables. For example, this code:

```
velocity = distance / duration
```

is clearer than:

```
v = d / t
```

In addition, the [PEP8](https://pep8.org/) recommends to use all lower case for variables, and to generally separate multiple words by underscores (`_`), e.g., `power`, `mean_power`, `peak_power`.

:::

## 💪 Exercise

A sprinter runs through two timing gates spaced by 50 m. Each timing gate records the time (in seconds) at which the sprinter passes through it.

![exercices_illustration -width:normal](_static/images/exercise_timing_gates.png)

Given the following program:

```
time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters
```

Continue this program so that it prints the mean velocity of the sprinter between gates 1 and 2. You can then show a suggested answer by clicking on the plus sign below.

```{code-cell} ipython3
:tags: [hide-cell]

time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters

print(distance_gates12 / (time_gate2 - time_gate1))
```

