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

# Creating dictionaries and accessing/modifying entries

A dictionary is created using curly braces `{}` and colons `:`, using a "key: value" syntax:

```{code-cell} ipython3
empty_dict = {}
dict_of_integers = {1: 11, 2: 22, 5: 55}
```

Here, we used integers for both the keys and values, but in reality:
- the key can be of many types such as integers or strings;
- the value can be of any type.

```{code-cell} ipython3
dict_of_anything = {
    1: "String for integer key 1",
    2: "String for integer key 2",
    "three": "String for string key 'three'",
    "some_int_value": 10,
    "some_float_value": 10.0,
    "some_list": [1, 3, 5, 7],
    "some_nested_dict": {
        "a": "A",
        "b": "B",
    },
}
```

To access a dictionary entry, we use `[]`, exactly as we would [index a list or tuple](python_lists_indexing.md):

```{code-cell} ipython3
dict_of_anything[2]
```

```{code-cell} ipython3
dict_of_anything["three"]
```

```{code-cell} ipython3
dict_of_anything["some_nested_dict"]
```

To change the value of an existing element:

```{code-cell} ipython3
dict_of_anything[2] = 66

dict_of_anything
```

We can list the available keys in a dictionary using its `keys` method:

```{code-cell} ipython3
dict_of_anything.keys()
```

or we can test if the dictionary contains a certain key using the `in` keyword:

```{code-cell} ipython3
print(1 in dict_of_anything)
print(3 in dict_of_anything)
```
