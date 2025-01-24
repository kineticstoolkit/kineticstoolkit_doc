# Looping

In section [](python_lists_modify_exercise2.md), we repeated a similar instruction multiple times:

```
one_list.extend(max_flexion[1])
one_list.extend(max_flexion[2])
one_list.extend(max_flexion[3])
```

While this was perfectly fine for only three repetitions, it would not scale well for tens or even hundreds of repetitions.

When we need to repeat operations multiple times, we can use two types of loops: `while` and `for`. This section explains when and how to use each form. Looping through a dictionary will be covered later in section [](python_dicts.md).
