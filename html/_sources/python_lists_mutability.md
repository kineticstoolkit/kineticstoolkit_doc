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

# Manipulating lists

:::{card} Summary
This section shows to modify lists using indexing and slicing, and how to extend lists or append data to lists.
:::

## Modifying an element

In previous section, we learnt that we can read an element of a list using indexing and slicing:

```{code-cell}
a = [1, 2, 3]

# Read the first element (indexing)
print(a[0])

# Read the first and second elements (slicing)
print(a[0:2])
```

We can also use indexing and slicing to write elements of a list. To write one element using indexing:

```{code-cell}
a = [1, 2, 3]
a[0] = 10

a
```

To write multiple elements at once using slicing:

```{code-cell}
a = [1, 2, 3]
b = [10, 20, 30]

# Assign 20 and 30 from `b` in place of 1 and 2 in `a`
a[0:2] = b[1:3]

a
```

## Appending an element to a list

To append a new element to a list, we can use the list's `append` method, which takes the new value as an argument.

:::{admonition} Function vs method
We already saw what is a [function](python_functions.md): a subprogram that can process arguments and return a result.

```
output = function(input)
```

A method is a special type of function that is specific to a given variable type. It is called with the variable, using the dot `.` operator:

```
output = input.method()
```

:::

```{code-cell}
a = [1, 2, 3]
print('a_before = ', a)

a.append(4)

print('a_after = ', a)
```

## Extending a list

To append multiple elements at once, we instead use the lists' `extend` method, which takes a list of new values as an argument.

```{code-cell}
a = [1, 2, 3]
b = [4, 5]
print('a_before = ', a)

a.extend(b)

print('a_after = ', a)
```

## Exercise 1

Here is the progression of a person's maximal flexion angle of the shoulder during a 4-month stretching program, with the outer list corresponding to the month, and the inner lists being 10 consecutive measurements performed during the month.

```{code-cell}
max_flexion = [
    [ 98.5,  91.2,  94. ,  93.6,  98. ,  95.9,  96. ,  97. ,  99. , 103.2],
    [104.1, 105.2, 106.4, 104.6, 106. , 105.1, 108.3, 109.8, 112.2, 111.8],
    [114.9, 111.1, 112.5, 117.4, 116.8, 119.3, 118.3, 117.9, 120.8, 120.9],
    [122.3, 123.6, 123.6, 127.6, 125.4, 127. , 130.3, 129.7, 128.7, 131.2],
]
```

After verification, you realize that for the very first measurement, the instrument was not calibrated correctly and added 5 degrees to the real angle values. Please write a one-line code that corrects this measurement.

```{code-cell}
:tags: [hide-cell]

max_flexion[0][0] = max_flexion[0][0] - 5

# This line would be equivalent and still clearer:
# max_flexion[0][0] -= 5

max_flexion
```

## Exercise 2

Write a code that creates one single, un-nested list, that contains every 40 consecutive measurements.

```{code-cell}
:tags: [hide-cell]

one_list = max_flexion[0]
one_list.extend(max_flexion[1])
one_list.extend(max_flexion[2])
one_list.extend(max_flexion[3])

one_list
```