# 🚧 More advanced concepts

{{ stub }}

For now, this page contains material that I'm not sure where to introduce yet.

- None
- List comprehension


## Mutability

In Python, variables generally do not contain a value, but a reference to a value in memory. This may be confusing at first and is better understood with an example. Let's create a list of three integers:

```{code-cell}
a = [1, 2, 3]
```

and another list `b`, which is exactly like list `a`:

```{code-cell}
b = [1, 2, 3]
```

In this example, we created two completely different lists, that happen to have an equal contents. Therefore, if we modify an element of `b`, then `a` keeps its original value:

```{code-cell}
print('a before = ', a)
print('b before = ', b)

b[0] = 10

print('a after = ', a)
print('b after = ', b)
```

Now, let's create another list `c`, which is not only like list `a`, but that really **is** list `a`:

```{code-cell}
c = a
```

Since both list point to the same memory, then modifying `c` will also modify `a`:

```{code-cell}
print('a before = ', a)
print('c before = ', c)

c[0] = 10

print('a after = ', a)
print('c after = ', c)
```


