---
kernelspec:
  name: python3
---

# Printing to the console

To print anything to the console, we use the `print` function:

```{code-cell}
print(1 + 2)
print(3 + 4)
```

The `print` function works with any content, be it numbers or words:

```{code-cell}
print("Hello world")
```


:::{important}
Python is case-sensitive. This means that `a` is not the same as `A`. Consequently,

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
