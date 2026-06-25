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



# Numbers

Until now, we referred to numbers simply as "numbers". In reality, numbers belong to different sets, each fulfilling a different role. Python provides three sets of numbers:

- Integer numbers: `int`
- Real numbers: `float`
- Complex numbers: `complex`

```{figure}
:label: fig_number_sets
:width: 6in
![](_static/images/fig_number_sets.png)

The three sets of numbers in Python.
```

However, we will focus only on integers (`int`) and real numbers (`float`).


## Integers and floats

Usually, floats and integers fulfil different roles:

**Floats** are used to represent real, physical values:

- A force in newtons
- A distance in meters
- A power in watts
- An angle in radians
- etc.

**Integers** are used to represent ranks, indexes, counts, etc:

- An index in a list (e.g, 5th value of a list)
- A number of repetitions
- A number of events
- The size of a matrix
- etc.


When we create a new numeric variable, the variable is defined:
- as a `float` if its literal value contains a decimal point
- as an `int` if its literal value contains a decimal point

```{code-cell} ipython3
an_int = 3
a_float = 3.1
```

The type of an existing variable can be known with the function `type`:

```{code-cell}
print(type(an_int))
print(type(a_float))
```

or `isinstance`:

```{code-cell}
print(isinstance(an_int, int))  # Is it an integer?
print(isinstance(an_int, float))  # Is it a float?
```

A variable can be converted from an `int` to a `float` using the `float()` function:

```{code-cell} ipython3
float(an_int)
```

A variable can be converted from a `float` to an `int` using the `int()` function. Please note, however, that the decimal component of the number is lost:

```{code-cell} ipython3
int(a_float)
```



## Arithmetic operations between integers and floats

When we perform operations between different types, Python may automatically convert integers to floats to ensure that the result holds the correct value. For example, adding an integer to another integer results in an integer:

```{code-cell} ipython3
a = 2 + 4

type(a)
```

However, adding a float to an integer results in a float:

```{code-cell} ipython3
b = 2 + 4.5

type(b)
```

A special case is the division, which always results in a float, even if we divide two integers, and even if the result is round:

```{code-cell} ipython3
c = 4 / 2

type(c)
```


## 💪 Exercise

We want to create a variable named `mass` that will contain the mass of a person in kg. This person has a mass of 68 kg. Since this is a physical value, it should be a float, hence the decimal point:

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
