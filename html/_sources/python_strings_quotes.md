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

# Creating strings using quotes

A string is created by enclosing characters between quotes. Python does not make a difference between single-quotes `'` and double-quotes `"`. Therefore, the following strings are equivalent:

```{code-cell}
s1 = "Hello world!"
s2 = 'Hello world!'
```

Normally, we use double-quotes if the string contains apostrophes `'`; inversely, we will use single-quotes if the string contains double-quotes `"`. For instance, both these strings are correctly defined:

```{code-cell}
s3 = "It's time to lunch."
s4 = 'I would not call it "results"...'
```

but the following ones generate syntax errors, because the apostrophe or double-quote closes the string before reaching the ending delimiter:

```{code-cell}
:tags: [raises-exception]
s5 = 'It's time to lunch'
s6 = "I would not call it "results"..."
```
