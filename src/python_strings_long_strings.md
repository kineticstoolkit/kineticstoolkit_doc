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

# Creating long strings

Normally, we want our code to fit in a given width and avoid lines that are too long. Many code style conventions limit the width of a code line to 80 characters. Following this advice may be difficult when creating long strings. There is however a way to express a continuous string on multiple lines, by enclosing multiple strings in parentheses.

```{code-cell} ipython3
long_string = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
    "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim "
    "ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
    "aliquip ex ea commodo consequat."
)

print(long_string)
```
