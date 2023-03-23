---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```

# Modifying a dictionary

## 📄 Adding elements

Accessing a dictionary using a key that is not part of the dictionary results in a key error:

```{code-cell} ipython3
dict_of_integers = {1: 11, 2: 22, 5: 55}
```

```{code-cell} ipython3
:tags: [raises-exception]
dict_of_integers[3]
```

However, assigning a value to a key that does not exist creates this key:

```{code-cell} ipython3
dict_of_integers[3] = 33

dict_of_integers
```

## 📄 Removing elements

Similarly to lists, we remove an element from a dictionary using the `pop` method, which both returns the value being deleted, and deletes it.

```{code-cell} ipython3
print(dict_of_integers.pop(1))  # Remove the element with key 1
print(dict_of_integers)
```
