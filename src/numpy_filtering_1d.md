# Filtering

We learned how to access **one data** using indexing, and **multiple regularly-spaced data** using slicing. To read **multiple non-regularly-spaced data**, we use filtering. We call it filtering because we selectively filter out some data using a mask.

### Boolean mask

Here is our original array or 10 values:

```{code-cell} ipython3
data = np.array([0.0, 0.58, 0.95, 0.95, 0.58, 0.0, -0.59, -0.96, -0.96, -0.59])
time = np.arange(10) / 10

plt.plot(data, "s-")
plt.grid(True)
plt.show()
```

Let's say we want to keep only the following indexes:

```{code-cell} ipython3
:tags: [remove-input]

bool_mask = [True, False, False, True, False, False, False, False, True, True]

plt.plot(time, data, "s-")
plt.grid(True)
for i, value in enumerate(bool_mask):
    if value:
        plt.text(
            time[i],
            data[i] + 0.04,
            "$\checkmark$",
            ha="center",
            fontsize=50,
            color="g",
        )
    else:
        plt.text(
            time[i], data[i] + 0.04, "x", ha="center", fontsize=30, color="r"
        )
```

We can create a boolean mask where each data to keep is True, and each data to discard is False:

```{code-cell} ipython3
bool_mask = [True, False, False, True, False, False, False, False, True, True]
```

Then, we use the mask exactly like we would index or slice the list:

```{code-cell} ipython3
plt.plot(time, data, "s-", label="Original data")
plt.plot(time[bool_mask], data[bool_mask], "o-", label="Filtered data")
plt.legend()
plt.show()
```

### Integer mask

We can also build a mask using a list or array of integers. In this case, this is a list of the indexes to keep:

```{code-cell} ipython3
int_mask = [0, 3, 8, 9]

plt.plot(time, data, "s-", label="Original data")
plt.plot(time[int_mask], data[int_mask], "o-", label="Filtered data")
plt.legend()
plt.show()
```

:::{tip}
Since indexes can also be negative, then masks of integers can also use negative values.
:::

