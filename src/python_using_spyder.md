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

# 📖 Using Spyder

:::{card} Summary
This section shows how to use Spyder to execute your first lines of code and build your first program.
:::

For those who are used to Matlab, Spyder's interface should immediately look familiar. Spyder's standard look is shown below:

(fig:screenshot)=
![](_static/images/spyder_screenshot.png)


## 📄 Writing code in a console

In the figure above, Section A is the console, and is the equivalent of the `>>>` console that we regularly see in tutorials. Any command that you enter here is executed immediately, and the output is returned just below.

You can try it with a very simple calculation:

```{code-cell} ipython3
1 + 2
```

You can also write multiple-line commands using CTRL+Enter. Both are executed, but only the result from the last command is printed:

```{code-cell} ipython3
1 + 2
3 + 4
```

To force the console to print something, and not only the result of the last operation, we use the `print` function:

```{code-cell} ipython3
print(1 + 2)
print(3 + 4)
```

The `print` function works with any contents, be it numbers or words. Here is the most ubiquitous first program in computer science: "Hello World". Try typing this command in the console:

```{code-cell} ipython3
print("Hello world")
```


:::{important}
Python is case-sensitive. This means that `a` is not the same thing as `A`. Similarly,

```
Print("Hello world")
```

or

```
PRINT("Hello world")
```

would result in an error because neither `Print` or `PRINT` exists. However,

```
print("Hello world")
```

works.
:::

## 📄 Writing code in a script

In the figure above, Section B is the script editor. This is where you will be writing most of your code. It is simply a text editor that allows saving our code (in a .py text file) to execute it all together later. You can execute a script by clicking on the `Run File` button (leftmost in the following toolbar, which can have different looks according to your configuration):

![](_static/images/spyder_run_toolbar.png)
![](_static/images/spyder_run_toolbar_mac.png)

## 💪 Exercise 1
Create a file named `hello_world.py` that prints "Hello World", and run it using the `Run File` button.


## 📄 Comments

For now, our first program has only one line, it is easy to understand. As our programs grow over time, we need to document them. To this effect, any text that follows `#` is considered by python as a comment, and is not executed. Usually, we use comments to explain what is the objective of a section of code.

## 📄 Writing code in a cell

When scripts are getting longer, it can be practical to run only one section of the script at a time. Scripts can be split into cells using this sequence of characters which acts as a separator:

```
#%%
```

:::{good-practice} Cells
You can name cells by adding a title next to the separator. This is generally a good idea to keep control of your growing script.
```
#%% Load results from previous acquisition

[...]

#%% Report these results in a local coordinate system

[...]

```
:::

You can execute a cell by placing the cursor in that cell, then by clicking on the `Run current cell` (middle button) or `Run current cell and go to the next one` (right button) in the following toolbar:

![](_static/images/spyder_run_toolbar.png)
![](_static/images/spyder_run_toolbar_mac.png)

## 💪 Exercise 2

Create a file named `hello_north_south.py` that contains two cells. A first cell prints "Hello north", and a second cell prints "Hello south". Run the cell of your choice using the toolbar icons.

## 📄 Getting help

In the [screenshot](fig:screenshot) above, Section C is a collection of panes that can be helpful during data processing. The help pane is particularly helpful to navigate the documentation of a given module or package. For example, to better understand how to use the numpy's `mean()` function, you could write `np.mean` in the help pane.

:::{tip}
The corresponding module must be loaded before. We will see later the concept of module. For this example, you must enter:
```
import numpy as np
```
in the console before entering `np.mean` in the help browser.
:::

Note that you can also get help in the command line, using the `help` function:

```{code-cell} ipython3
import numpy as np
help(np.mean)
```
