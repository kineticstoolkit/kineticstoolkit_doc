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

# Return values

Most functions do not print results in the console. Instead, they calculate something and return the result as an output. This is done using the `return` statement. Although the following function is not that useful, it illustrates how it works:

```{code-cell}
# Define a function
def calculate_sum(arg1, arg2):
    result = arg1 + arg2
    return result

# Call the function with some values
print(calculate_sum(2, 6))
```

The function `calculate_sum()` is called with arguments 2 and 6. It executes, and then returns 8. Therefore, the `print()` function prints 8.

As a second example:

```{code-cell}
print(calculate_sum(calculate_sum(2, 6), 5))
```

The inner function calls `calculate_sum()` with arguments 2 and 6. The function executes and returns 8. Then, the outer function calls `calculate_sum()` with arguments 8 and 5. The function executes again and this time returns 13. Therefore, the `print()` function prints 13.
