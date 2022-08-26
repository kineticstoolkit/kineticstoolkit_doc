# Configuring Spyder for Python biomechanics

Spyder just works out of the box. However, we suggest to use these alternative settings, which we believe are helpful to get on track as fast as possible in writing great code and processing biomechanical data.

## Interactive graphics

By default, figures are plotted in a static pane which does not support interactive features such as zooming, panning or clicking. It is however much more convenient to use interactive graphics.

To configure Spyder for interactive graphics, go to the Spyder's preferences, to the **IPython console** item, then to the **Graphics** pane. In the **Graphics backend** box, select **Qt5**. Restart Spyder.

## Automatic code style

While most Python code is generally readable, there are still many official and unofficial rules that define how code "should" look. For example, we usually put spaces between operators, no more than two blank lines between statements, etc. To focus on learning what to code, and not how code should look, we recommend to use the [Black](https://black.readthedocs.io) formatter.

Go to the Spyder's preferences, to the **Completion and linting** item, then to the **Code style and formatting** pane. In the **Code formatting** box, select **black** and check **Autoformat files on save**. Now, your code will always respect most common style rules.

:::{note}
In this interactive book, we assume that you are using automatic code style, and therefore there will be very little content on code styling.
:::

## Docstring linting

If you start writing lots of functions, you will want your functions to be [well documented](python_functions_docstrings.md). To help you in this objective, activate Docstring linting. This shows hints in the editor to help you to code good docstrings. 

Go to the Spyder's preferences, to the **Completion and linting** item, then to the **Docstring style** pane. Check **Enable docstring type linting** and choose **Numpy** in the selection box.
