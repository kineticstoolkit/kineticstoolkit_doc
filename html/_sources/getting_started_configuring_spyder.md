# Configuring Spyder

Spyder is a general purpose programming environment for scientific applications, and it suits very well biomechanical data processing. We however recommend doing these steps to enhance your experience with interactive data processing.


```{figure-md} fig_spyder_ide
:width: 4in
![](_static/images/fig_spyder_ide.jpg)

The Scientific Python Development Environment (spyder)
```

## Mandatory: Interactive Matplotlib figures

To pan and zoom plots, or to use Kinetics Toolkit's interactive functions (e.g., editing events, visualizing 3D points), you must use an interactive frontend for Matplotlib. Follow these steps to configure Spyder for interactive graphics, as shown in {numref}`fig_spyder_qt5`.

- Go to the Spyder's preferences
- to the **IPython console** item
- then to the **Graphics** pane.
- In the **Graphics backend** box, select **Qt5**, then restart Spyder.


```{figure-md} fig_spyder_qt5
:width: 7in
![](_static/images/fig_spyder_qt5.png)


Enabling interactive graphics in Spyder
```

:::{note}

If you are not using Spyder (but you do use an IPython console), or you do not want to change your Spyder configuration, you can enable interactive graphics temporarily by typing:

```
%matplotlib qt5
```

:::

## Optional: Automatic code style

While most Python code is generally readable, there are still many official and unofficial rules that define how code "should" look. For example, we usually put spaces between operators, no more than two blank lines between statements, etc. To focus on learning **what** to code rather than how code should **look**, we recommend to use the [Black](https://black.readthedocs.io) formatter. Follow these steps, as shown in {numref}`fig_spyder_black`:

- Go to the Spyder's preferences
- to the **Completion and linting** item
- then to the **Code style and formatting** pane.
- In the **Code formatting** box, select **black** and check **Autoformat files on save**.

Now, your code will always respect most common style rules.

```{figure-md} fig_spyder_black
:width: 7in
![](_static/images/fig_spyder_black.png)

Enabling Black formatter in Spyder
```

## Optional: Docstring linting

If you start writing lots of functions, you will want your functions to be [well documented](python_functions_docstrings.md). To help you in this objective, activate Docstring linting, which will provide hints in the editor to help you formatting your docstrings. Follow these steps, as shown in {numref}`fig_spyder_docstring_linting`:

- Go to the Spyder's preferences
- to the **Completion and linting** item
- then to the **Docstring style** pane.
- Check **Enable docstring type linting** and choose **Numpy** in the selection box.

```{figure-md} fig_spyder_docstring_linting
:width: 7in
![](_static/images/fig_spyder_docstring_linting.png)

Enabling docstring linting in Spyder
```
