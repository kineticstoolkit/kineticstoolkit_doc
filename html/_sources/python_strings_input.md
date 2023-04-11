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

To conclude this section, we can also create strings using user input:

```
the_string = input()
```

This allows the user to type some text right in the console, until they press Enter. It is usually a good idea to provide some text to the user:

```
the_string = input("Please enter your name: ")
```

Note that the input function always create a string. If you want the user to input a float, then you need to convert the string to a float. For example:

```
str_height = input("What is the participant's height in meters? ")
```

User enters "1.45"

```{code-cell}
:tags: ["remove-cell"]
str_height = "1.45"
str_cycle = "4"
```

```{code-cell}
height = float(str_height)

print(height)
print(type(height))
```

The same thing applies if we need the user to enter an integer:

```
str_cycle = input("Which gait cycle do we keep? ")
```

User enters "4"

```{code-cell}
i_cycle = int(str_cycle)

print(i_cycle)
print(type(i_cycle))
```
