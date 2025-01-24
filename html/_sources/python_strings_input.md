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

# User input

We can create strings interactively from user input:

```
the_string = input()
```

This allows the user to type some text right in the console. It is usually a good idea to provide some text to the user:

```
the_string = input("Please enter your name: ")
```

Note that the input function always creates a string. If you want the user to input a float, then you need to convert the string to a float:

```
height = float(input("What is the participant's height in meters? "))
```

Or if we need the user to enter an integer:

```
i_cycle = int(input("Which gait cycle do we keep? "))
```
