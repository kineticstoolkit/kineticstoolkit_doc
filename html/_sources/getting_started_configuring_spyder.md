# Configuring Spyder

Spyder is a general purpose programming environment for scientific applications. These steps are recommended to enhance your experience in processing biomechanical data interactively.

## Mandatory: Interactive Matplotlib graphics

To pan and zoom plots, or to use Kinetics Toolkit's interactive functions (e.g., editing events, visualizing 3d points), you must use an interactive frontend for Matplotlib. To configure Spyder for interactive graphics:

- Go to the Spyder's preferences
- to the **IPython console** item
- then to the **Graphics** pane.
- In the **Graphics backend** box, select **Qt5**, then restart Spyder.

:::{important}

If you are not using Spyder (but you do use a IPython console), or you do not want to change your Spyder configuration, you can enable interactive graphics temporarily by typing:

```
%matplotlib qt5
```

:::

## Facultative: Automatic code style

While most Python code is generally readable, there are still many official and unofficial rules that define how code "should" look. For example, we usually put spaces between operators, no more than two blank lines between statements, etc. To focus on learning **what** to code rather than how code should **look**, we recommend to use the [Black](https://black.readthedocs.io) formatter.

Go to the Spyder's preferences, to the **Completion and linting** item, then to the **Code style and formatting** pane. In the **Code formatting** box, select **black** and check **Autoformat files on save**. Now, your code will always respect most common style rules.

## Facultative: Docstring linting

If you start writing lots of functions, you will want your functions to be [well documented](python_functions_docstrings.md). To help you in this objective, activate Docstring linting, which will provide hints in the editor to help you formatting your docstrings. 

Go to the Spyder's preferences, to the **Completion and linting** item, then to the **Docstring style** pane. Check **Enable docstring type linting** and choose **Numpy** in the selection box.
