# Lists and tuples

Suppose that we take three measurements of a given quantity (for instance, the height of a person). We could assign three variables for it (`height1`, `height2`, and `height3`) and write some code that processes it:

```
# Calculate the mean height
height = (height1 + height2 + height3) / 3
```

But what if we take hundreds of even thousands of measurements? At some point, it will be impossible to write clean code that processes so many variables.

Python provides powerful constructs to contain large numbers of values in a structured way, the most common being the list, the tuple and the dictionary. This section introduces the list and the tuple.
