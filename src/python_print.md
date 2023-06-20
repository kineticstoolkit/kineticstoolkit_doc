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

# Printing to the console

To print anything to the console, we use the `print` function:

```{code-cell} ipython3
print(1 + 2)
print(3 + 4)
```

The `print` function works with any contents, be it numbers or words:

```{code-cell} ipython3
print("Hello world")
```


:::{important}
Python is case-sensitive. This means that `a` is not the same thing as `A`. Consequently,

```
Print("Hello world")
```

or

```
PRINT("Hello world")
```

would result in an error because neither `Print` or `PRINT` exists. However,

```
print("Hello world")
```

works.
:::
