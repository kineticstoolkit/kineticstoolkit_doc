# 🚧 Numpy

{{ incomplete }}

:::{margin} #todo
Write a proper tutorial for biomechanics, with examples.
:::

```{tableofcontents}
```

:::{note}
This page is a subset from [Jay Alammar](https://jalammar.github.io/)'s excellent tutorial: *Alammar, J (2019). A Visual Intro to NumPy and Data Representation [Blog post]. Retrieved from [](https://jalammar.github.io/visual-numpy/)*

[![Creative Commons License](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/).

Please credit and refer to Jay Alammar's work for all this page contents.
:::

## A Visual Intro to NumPy and Data Representation

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image.png)

The [NumPy](https://www.numpy.org/) package is the workhorse of data analysis, machine learning, and scientific computing in the python ecosystem. It vastly simplifies manipulating and crunching vectors and matrices. Some of python’s leading package rely on NumPy as a fundamental piece of their infrastructure (examples include scikit-learn, SciPy, pandas, and tensorflow). Beyond the ability to slice and dice numeric data, mastering numpy will give you an edge when dealing and debugging with advanced usecases in these libraries.

In this post, we’ll look at some of the main ways to use NumPy and how it can represent different types of data (tables, images, text…etc) before we can serve them to machine learning models.

```
import numpy as np
```

## Creating Arrays

We can create a NumPy array (a.k.a. the mighty [ndarray](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html)) by passing a python list to it and using ` np.array()`. In this case, python creates the array we can see on the right here:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-1.png)

There are often cases when we want NumPy to initialize the values of the array for us. NumPy provides methods like ones(), zeros(), and random.random() for these cases. We just pass them the number of elements we want it to generate:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-2-1024x228.png)

Once we’ve created our arrays, we can start to manipulate them in interesting ways.

## Array Arithmetic

Let’s create two NumPy arrays to showcase their usefulness. We’ll call them `data` and `ones`:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-3.png)

Adding them up position-wise (i.e. adding the values of each row) is as simple as typing `data + ones`:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-4.png)

When I started learning such tools, I found it refreshing that an abstraction like this makes me not have to program such a calculation in loops. It’s a wonderful abstraction that allows you to think about problems at a higher level.

And it’s not only addition that we can do this way:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-5-1024x123.png)

There are often cases when we want to carry out an operation between an array and a single number (we can also call this an operation between a vector and a scalar). Say, for example, our array represents distance in miles, and we want to convert it to kilometers. We simply say `data * 1.6`:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-6-1024x116.png)

See how NumPy understood that operation to mean that the multiplication should happen with each cell? That concept is called _broadcasting_, and it’s very useful.

## Indexing

We can index and slice NumPy arrays in all the ways we can slice python lists:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-7.png)

## Aggregation

Additional benefits NumPy gives us are aggregation functions:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-8-1024x185.png)

In addition to `min`, `max`, and `sum`, you get all the greats like `mean` to get the average, `prod` to get the result of multiplying all the elements together, `std` to get standard deviation, and [plenty of others](https://jakevdp.github.io/PythonDataScienceHandbook/02.04-computation-on-arrays-aggregates.html).

## In more dimensions

All the examples we’ve looked at deal with vectors in one dimension. A key part of the beauty of NumPy is its ability to apply everything we’ve looked at so far to any number of dimensions.

### Creating Matrices

We can pass python lists of lists in the following shape to have NumPy create a matrix to represent them:

```
np.array([[1,2],[3,4]])
```

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-9.png)

We can also use the same methods we mentioned above (`ones()`, `zeros()`, and `random.random()`) as long as we give them a tuple describing the dimensions of the matrix we are creating:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-10-1024x184.png)

### Matrix Arithmetic

We can add and multiply matrices using arithmetic operators (`+-*/`) if the two matrices are the same size. NumPy handles those as position-wise operations:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-11.png)

We can get away with doing these arithmetic operations on matrices of different size only if the different dimension is one (e.g. the matrix has only one column or one row), in which case NumPy uses its broadcast rules for that operation:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-12-1024x186.png)

### Dot Product

A key distinction to make with arithmetic is the case of [matrix multiplication](https://www.mathsisfun.com/algebra/matrix-multiplying.html) using the dot product. NumPy gives every matrix a `dot()` method we can use to carry-out dot product operations with other matrices:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-13-1024x256.png)

I’ve added matrix dimensions at the bottom of this figure to stress that the two matrices have to have the same dimension on the side they face each other with. You can visualize this operation as looking like this:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-14-1024x252.png)

### Matrix Indexing

Indexing and slicing operations become even more useful when we’re manipulating matrices:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-15.png)

### Matrix Aggregation

We can aggregate matrices the same way we aggregated vectors:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-16-1024x197.png)

Not only can we aggregate all the values in a matrix, but we can also aggregate across the rows or columns by using the `axis` parameter:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-17-1024x183.png)

## Transposing and Reshaping

A common need when dealing with matrices is the need to rotate them. This is often the case when we need to take the dot product of two matrices and need to align the dimension they share. NumPy arrays have a convenient property called `T` to get the transpose of a matrix:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-18.png)

In more advanced use case, you may find yourself needing to switch the dimensions of a certain matrix. This is often the case in machine learning applications where a certain model expects a certain shape for the inputs that is different from your dataset. NumPy’s `reshape()` method is useful in these cases. You just pass it the new dimensions you want for the matrix. You can pass -1 for a dimension and NumPy can infer the correct dimension based on your matrix:

![](https://felixchenier.uqam.ca/wp-content/uploads/2021/02/image-19-1024x379.png)