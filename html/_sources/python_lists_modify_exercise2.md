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


# Exercise: Modifying lists 2

Here is the progression of a person's maximal flexion angle of the shoulder during a 4-month stretching program, with the outer list corresponding to the month, and the inner lists containing 10 consecutive measurements performed during each month.

```{code-cell} ipython3
max_flexion = [
    [ 98.5,  91.2,  94. ,  93.6,  98. ,  95.9,  96. ,  97. ,  99. , 103.2],
    [104.1, 105.2, 106.4, 104.6, 106. , 105.1, 108.3, 109.8, 112.2, 111.8],
    [114.9, 111.1, 112.5, 117.4, 116.8, 119.3, 118.3, 117.9, 120.8, 120.9],
    [122.3, 123.6, 123.6, 127.6, 125.4, 127. , 130.3, 129.7, 128.7, 131.2],
]
```

Write code that creates one single, un-nested list containing all 40 consecutive measurements.

```{code-cell} ipython3
:tags: [hide-cell]

one_list = max_flexion[0]
one_list.extend(max_flexion[1])
one_list.extend(max_flexion[2])
one_list.extend(max_flexion[3])

one_list
```
