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


# Looping through a dictionary

Similarly to lists, we can loop through every element of a dictionary, using the `for` instruction. The variable returned by `for` is the key. For example, to loop over every keys of this dictionary:

```{code-cell} ipython3
dict_of_anything = {
    1: "I have an integer key",
    2: "I have another integer key",
    "three": "I have a string key",
    "some_int_value": 10,
    "some_float_value": 10.0,
    "some_list": [1, 3, 5, 7],
    "some_nested_dict": {
        "a": "A",
        "b": "B",
    },
    100: "ok that's enough",
}
```

we would do:

```{code-cell} ipython3
for key in dict_of_anything:
    print(f"Key {key} contains this value: {dict_of_anything[key]}")
```

