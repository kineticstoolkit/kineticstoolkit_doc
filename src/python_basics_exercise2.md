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

# Exercise: Python basics 2

A sprinter runs a given distance $x$ to the East, then a given distance $y$ to the North (in km), as picture in {numref}`fig_exercise_pythagore`. Use the Pythagorean theorem to complete the following program so that it prints the distance $d$ between her starting point and her final destination.

```{figure-md} fig_exercise_pythagore
:width: 4in
![](_static/images/fig_exercise_pythagore.png)

Distance between the starting point and final destination.
```

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
