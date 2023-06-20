# Argument names

In this `print_sum` example, we used `arg1` and `arg2` as argument names:

```
def print_sum(arg1, arg2):
    print("Hi!")
    print(f"The first variable is {arg1}.")
    print(f"The second variable is {arg2}.")
    print(f"The sum of both variables is {arg1 + arg2}.")
```

Virtually any other name would work equally. For instance, we could use `first` and `second`, as long as we also use these names in the implementation:

```
def print_sum(first, second):
    print("Hi!")
    print(f"The first variable is {first}.")
    print(f"The second variable is {second}.")
    print(f"The sum of both variables is {first + second}.")
```

:::{good-practice} Clear argument names
It is important to use clear names for function arguments. Argument names are selected using the same best practices as standard [variable](python_variables.md) names.
:::
