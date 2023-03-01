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

# 📖 Numbers

:::{card} Summary
This section explains the difference between classes of numbers (integers, floats and complex numbers), and shows the exponentiation (`**`) arithmetic operation.
:::

Up to now, we referred to numbers simply as "numbers". In reality, numbers belong to different sets. Python provides three sets of numbers:

- Integer numbers: `int`
- Real numbers: `float`
- Complex numbers: `complex`

![number sets -height:shorter](_static/images/number_sets.png)

For now, we will focus only on integers and floats.

## 📄 Integers and floats

Usually, floats and integers fulfil different roles:

- Floats are used to represent real, physical values:
    - Force in newtons
    - Distance in meters
    - Power in watts
    - Angle in radians
    - etc.
- Integers are used to represents:
    - An index in a list (e.g, 5th value of a list)
    - A number of repetitions
    - A number of events
    - The size of a matrix
    - etc.

Integers and floats are stored differently in memory. A variable is defined as a `float` if it contains a decimal point, and as an `int` if doesn't contain one:

```{code-cell} ipython3
an_int = 3
a_float = 3.0
```

The type of an existing variable can be known with the functions `type`, or `isinstance`:

```{code-cell}
print(type(an_int))
print(type(a_float))
```

```{code-cell}
print(isinstance(an_int, int))  # Is it an integer?
print(isinstance(an_int, float))  # Is it a float?
```

A variable can be converted from an `int` to a `float` using the `float()` function:

```{code-cell} ipython3
new_variable = float(an_int)

print(new_variable)
print(type(new_variable))
```

A variable can be converted from a `float` to an `int` using the `int()` function. Please note, however, that the decimal component of the number is lost:

```{code-cell} ipython3
new_variable = int(a_float)

print(new_variable)
print(type(new_variable))
```


## 💪 Exercise 1

We want to create a variable named `mass` that will contain the mass of a person in kg. This person as a mass of 68 kg. Since this is a physical value, we want to create it as a float, using a decimal point:

```
mass = 68.0
```

How would you create the following variables?

- `hip_height`: The height of the hip in standing position, which is 1 m.
- `i_trial`: The trial number where someone reached the highest isometric contraction, which is 3.
- `n_trials`: The total number of trials someone tried to reach the highest isometric contraction, which is 4.
- `emg_max`: The EMG value measured during a maximal isometric contraction, which is 34 μV.

```{code-cell} ipython3
:tags: [hide-cell]

hip_height = 1.0
i_trial = 3
n_trials = 4
emg_max = 34.0
```

## 📄 Arithmetic operations between integers and floats

When we perform operation between different types, python may convert the types to ensure that the result holds the correct value. For example, adding an int and a float results in a float:

```{code-cell} ipython3
a = 2 + 4.5

type(a)
```

However, adding an int and another int results in an int:

```{code-cell} ipython3
b = 2 + 4

type(b)
```

A special case is the division, which always results in a float, even if we divide two integers, and even if the result is round:

```{code-cell} ipython3
c = 4 / 2

type(c)
```

## 📄 Exponentiation

To raise a value to a power, we use the `**` operator. For example, to calculate $4^2$, we would write:

```{code-cell} ipython3
4**2
```

For roots, we can exponentiate to the inverse. For example, to calculate $\sqrt{4}$, we would write:

```{code-cell} ipython3
4 ** (1 / 2)
```

:::{note}
Later in section [](numpy_arithmetics_and_comparisons.md), we will see the function {{np_sqrt}} that performs the square root directly.
:::

Exponentiation follows the same type convention as the multiplication: using only integers will results in an integer, and as soon as one of the operands is a float, the result is a float.

```{code-cell} ipython3
type(4**2)
```

```{code-cell} ipython3
type(4.0**2)
```


## 💪 Exercise 2

A sprinter runs a given distance $x$ to the East, then a given distance $y$ to the North (in km). Use the Pythagorean theorem to complete the following program so that it prints the distance $d$ between her starting point and her final destination.

![exercice_illustration -height:shorter](_static/images/exercice_pythagore.png)

```
x = 2.5  # in meters
y = 0.7  # in meters
```

```{code-cell} ipython3
:tags: [hide-cell]

x = 2.5  # in meters
y = 0.7  # in meters
d = (x**2 + y**2) ** (1 / 2)

print(d)
```
