# Looping

In [this exercise](python_lists_slicing_exercise2.md), we repeated a similar instruction three times:

```
one_list.extend(max_flexion[1])
one_list.extend(max_flexion[2])
one_list.extend(max_flexion[3])
```

Obviously, while this was perfectly fine for only three repetitions, this solution would not scale well for tens or even hundreds of repetitions.

When we need to repeat operations, we can use two instructions: `while` and `for`. This section explains when and how to use each form.

```{tableofcontents}
```

Looping through a dictionary will be shown later in section [](python_dicts.md).
