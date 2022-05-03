---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Getting started with Spyder

[Spyder](https://spyder-ide.org) is an open-source integrated development environment (IDE) that was created explicitely for a scientific use. For those who are used to Matlab, its interface should immediately look familiar. Spyder's standard look is shown below:

(fig:screenshot)=
![](_static/images/spyder_screenshot.png)


## Writing code in a console

In the figure above, Section A is the console, and is the equivalent of the `>>>` console that we regularly see in tutorials. Any command that you enter here is executed immediately, and the output is returned just below. You can try it with the most ubiquitous example in computer science: "Hello World". Try typing this command in the console:

```{code-cell}
print("Hello world")
```

The print function prints something in the console, and in this very short program, this "something" is "Hello world".

## Writing code in a script

In the figure above, Section B is the script editor. This is where you will be writing most of your code. It is simply a text editor that allows saving our code (in a .py text file) to execute it all together later. You can execute a script by clicking on the `Run File` button (leftmost in the following toolbar, which can have different looks according to your configuration):

![](_static/images/spyder_run_toolbar.png)
![](_static/images/spyder_run_toolbar_mac.png)

:::{exercise} Hello world
Create a file named `hello_world.py` that prints "Hello World", and run it using the `Run File` button.
:::


## Writing code in a cell

When scripts start to be long, it can be practical to run only one section of the script at a time. Scripts can be split into cells using this sequence of characters which acts as a separator:

```
#%%
```

:::{goodpractice} Cells
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

:::{exercise} Cells
Create a file named `hello_north_south.py` that contains two cells. A first cell prints "Hello north", and a second cell prints "Hello south". Run the cell of your choice using the toolbar icons.
:::

## Getting help

In the [screenshot](fig:screenshot) above, Section C is a collection of panes that can be helpful during data processing. The help pane is particularly helpful to navigate the documentation of a given module or package. For example, to better understand how to use the numpy's `mean()` function, you could write `np.mean` in the help pane.

:::{tip}
The corresponding module must be loaded before. We will see later the concept of module. For this example, you must enter:
```
import numpy as np
```
in the console before entering `np.mean` in the help browser.
:::

:::{margin}
 #todo Add references for navigating in Spyder
:::
