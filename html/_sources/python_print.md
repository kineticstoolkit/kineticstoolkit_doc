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

The `print` function works with any contents, be it numbers or words. Try typing this command in the console:

```{code-cell} ipython3
print("Hello world")
```


::::::{note}
In section [](spyder_console.md), we learned that running a command already prints the result to the console. However, it only prints the result of the last performed operation, while `print` explicitly prints something when it is called.

:::::{grid}
::::{grid-item-card} Without `print`
```
1 + 2
3 + 4
```
+++++
Result:
```
7
```
::::

::::{grid-item-card} With `print`
```
print(1 + 2)
print(3 + 4)
```
+++++
Result:
```
3
7
```
::::

:::::
::::::

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
