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

Normally, we want to avoid writing very long code lines. For instance, it is common to limit the width of a line to 80 characters.

Following this limit may be difficult when creating long strings. To achieve this, we can split a long string on multiple lines, by enclosing multiple sub-strings between parentheses.

```{code-cell} ipython3
long_string = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
    "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim "
    "ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
    "aliquip ex ea commodo consequat."
)

print(long_string)
```
