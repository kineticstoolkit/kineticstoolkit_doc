---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Numbers

From the beginning, we referred to numbers simply as "numbers". In reality, numbers belong to different sets. In Python, we have three sets:

- Integer numbers: `int`
- Real numbers: `float`
- Complex numbers: `complex`

![number sets -height:shorter](_static/images/number_sets.png)

Through this tutorial, we will focus on integers and floats.

## Integers and floats

Usually, the role of a float is different to the role of an integer. Think of a float as a real, physical value (e.g., a force in newtons, a distance in meters, a power in watts); and an int as a position in a series, an index, a number of repetition (e.g., the 3rd data of a series, the 5th repetition of a total of 10).

Integers and floats are stored differently in memory, and it is sometimes important to make sure a number is stored in the correct type. The type of a variable can be known with the function `type()`.

A variable is defined as an `int` if its assigned value does not contain a decimal point:

```{code-cell} ipython3
a = 3

print(a)
print(type(a))
```

A variable is defined as a `float` if its assigned value contains a decimal point:

```{code-cell} ipython3
b = 1.7

print(b)
print(type(b))
```

A variable can be converted from an `int` to a `float` using the `float()` function:

```{code-cell} ipython3
c = float(a)

print(c)
print(type(c))
```

A variable can be converted from a `float` to an `int` using the `int()` function. Please note, however, that the decimal component of the number is lost:

```{code-cell} ipython3
d = int(b)

print(d)
print(type(d))
```


## Exercise 1

We want to create a variable named `mass` that will contain the mass of a person in kg. This person as a mass of 68 kg. Since this is a physical value that could take any decimal value, but that just happens to be rounded to the unit, we therefore want to create a float:

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

## Arithmetic operations between numbers of different type

When we perform operation between different types, Python may convert the types by itself to be sure that the result has the correct type. For example, adding an int and a float results in a float:

```{code-cell} ipython3
a = 2 + 4.5

type(a)
```

However, adding an int and another int results in an int:

```{code-cell} ipython3
b = 2 + 4

type(b)
```

A particular case is the division, which always results in a float, even if we divide two integers, and even if the result is round:

```{code-cell} ipython3
c = 4 / 2

type(c)
```

Therefore, to be sure that the result of a division is an int, we can cast the result as an int:

```{code-cell} ipython3
d = int(4 / 2)

type(d)
```

## Exponentiation

A last arithmetical operation is the exponentiation. Raising a value to a power is done using the `**` operator. For example, to calculate $4^2$, we would write:

```{code-cell} ipython3
4**2
```

For roots, we can exponententiate to the inverse. For example, to calculate $\sqrt{4}$, we would write:

```{code-cell} ipython3
4 ** (1 / 2)
```

:::{note}
Later in these tutorials, when we will start using [numpy](numpy.md), we will see the function `np.sqrt()` that performs the square root directly.
:::

Exponentiation follows the same type convention as the multiplication: using only integers will results in an integer, and as soon as one of the operands is a float, the result is a float.

```{code-cell} ipython3
type(4**2)
```

```{code-cell} ipython3
type(4.0**2)
```


## Exercise 2

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
