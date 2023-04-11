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

# Adding and removing entries

Accessing a dictionary using a key that is not part of the dictionary results in a key error:

```{code-cell} ipython3
dict_of_integers = {1: 11, 2: 22, 5: 55}
```

```{code-cell} ipython3
:tags: [raises-exception]
dict_of_integers[3]
```

However, assigning a value to a key that does not exist **creates** this key. This is how we add entries to a dictionary:

```{code-cell} ipython3
dict_of_integers[3] = 33

dict_of_integers
```

To remove an entry from a dictionary, we use the `pop` method, which behaves [as the list's pop method](python_lists_modify.md). It returns the value being deleted, and removes this entry from the dictionary.

```{code-cell} ipython3
print(dict_of_integers.pop(1))  # Remove the element with key 1
print(dict_of_integers)
```
