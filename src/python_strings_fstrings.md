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

# Including variables in strings using f-strings

We often use strings to report results. For instance, one way of reporting the ankle moment would be to use two `print` calls:

```{code-cell} ipython3
ankle_moment = 100.1  # (for instance)

print("The calculated moment at the ankle in Nm is:")
print(ankle_moment)
```

A single string that includes both the definition and the result would be more readable:

> "The calculated ankle moment is 100.1 Nm."

Including variables into strings is easily done using f-strings. F-strings' name comes from their `f` prefix. With f-strings, Python evaluates the content between curly braces `{}` and replaces this content by its evaluation.

```{code-cell} ipython3
# Here, we create the sentence above.
the_string = (
    f"The calculated ankle moment is {ankle_moment} Nm."
)

# And here, we print it.
print(the_string)
```

When an f-string contains a float, we can print it to a given precision, using `:.xf` just after the expression in braces, where `x` is the number of digits after the decimal point. For instance:

```{code-cell}
print(f"The calculated ankle moment is {ankle_moment:.0f} Nm.")
print(f"The calculated ankle moment is {ankle_moment:.2f} Nm.")
print(f"The calculated ankle moment is {ankle_moment:.5f} Nm.")
```
