# Introduction to arrays

While a NumPy array could be seen as an extension of the [Python lists](python_lists.md) list to multiple dimensions, it has fundamental differences which make both types powerful in their own ways. The main differences between both types are:

| Lists                                                                                                                                        | Arrays                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Are unidimensional. We can use nested lists to simulate multiple dimensions, but these values are harder to access, calculate, reshape, etc. | Can have any number of dimensions; they can represent matrices, or even series of matrices. | 
| Can be a sequence of different types, which makes them very versatile.                                                                       | Only hold elements of the same type.                            |
| Have a dynamic size that can be modified using `append`, `expand` and `pop`.                                                                 | Cannot "grow" as we do with lists.                                                          |
| Only hold data, they don't provide methods to compute data.                                                                                  | Can be used directly for calculations such as linear algebra, filtering, etc.               |

List and arrays can be converted one to the other, as we will see in [](numpy_ndarray_creating_from_lists.md).

