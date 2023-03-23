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

# Comments

Programs with only a few lines of code are generally easy to understand. As they grow in complexity, we need to document them, usually with comments.

Any text that follows `#` corresponds to a comment, and is not executed by Python. Usually, we use comments to explain what is the objective of a section of code.

These codes are completely equivalent:

**Without comments**

```{code-cell}
print("Here is a calculation")
print(10 + 5)
```


**With comments**

```{code-cell}
# Demonstrate comments

print("Here is a calculation")  # Print some text
print(10 + 5)  # Print the result of an addition
```
