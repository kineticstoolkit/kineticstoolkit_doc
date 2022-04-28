# Simple operations

{{ stub }}

- Addition, subtraction
    - print(4 + 3)
    - print(4 - 3)

:::{admonition} Good practice
Put spaces between operators (PEP8)
:::

- Using variables
    - a = 4; b = 3; print(a + b);
    - c = a + b; print(c);
    - c = c + 1; print(c);
    - Good practice: use clear names for variables (PEP8) (distance, duration, speed).
    - Good practice: use lowercase and underscores for variable names (PEP8).
- ints and floats
    - a = 1; print(a); print(type(a)); print(a, type(a));
    - a = 0.5; print(a, type(a));
    - a = 1.0; print(a, type(a));
- Inputing variables
    - a = input()
    - a = input("Enter a number: ")  *We already saw a string in the Hello World example, we will see it in more details in the Strings section.*
    - a = float(input("Enter a number: "))
- Multiplication, division
    - a = 4 + 3; print(a, type(a));
    - a = 4 * 3; print(a, type(a));
    - a = 4 / 3; print(a, type(a));
- Exponentiation and root
    - a = 4 ** 2; print(a, type(a));
    - a = 4 ** (1 / 2); print(a, type(a));
- Integration exercise: speed calculation *KEEP YOUR EXERCICES SINCE THEY ARE CONTINUOUSLY REUSED IN FOLLOWING EXERCICES.*
    - Given the following variables: (TODO use realistic values)
        - time_gate1 = 0.0
        - time_gate2 = 5.4
        - distance_gates12 = 50.0
    - Write a program that prints the mean velocity of the sprinter between gates 1 and 2.
