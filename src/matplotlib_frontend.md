# Non-blocking, interactive Matplotlib figures

:::{card} Summary
This section illustrates how Matplotlib may behave differently on different computers and setups, and suggests a method to configure Spyder and Matplotlib to always generate non-blocking, interactive figures.
:::

## 📄 The problem with default settings

Matplotlib's behaviour can change between different Python environments. For instance, to plot a curve in the standard Python or IPython interpreter, we need to specify when to generate the figure using {{plt_show}}:

![Python interpreter -width:full](_static/images/matplotlib_python1.png)
![plt.show -width:wider](_static/images/matplotlib_python2.png)

The different buttons on the figure allow some interaction with the plot:

- ![](_static/images/matplotlib_move.png) Move the figure around (panning);
- ![](_static/images/matplotlib_zoom_to_rect.png) Zoom on the figure;
- ![](_static/images/matplotlib_back.png) Undo the last pan/zoom operation;
- ![](_static/images/matplotlib_forward.png) Redo the last pan/zoom operation;
- ![](_static/images/matplotlib_home.png) Reset to the initial pan/zoom;
- ![](_static/images/matplotlib_filesave.png) Save the figure to an image file.

However, by default, the figure blocks console and we must close it before writing new code, which can be an inconvenience.

On the contrary, Spyder and Jupyter do not need `plt.show` and do not block the console.

![Plotting in Spyder](_static/images/matplotlib_spyder_default.png)
![Plotting in JupyterLab](_static/images/matplotlib_jupyter.png)

However, by default, both Spyder and Jupyter generate static, non-interactive figures, that don't allow for zooming, panning, clicking, etc.

## 📄 Interactive figures

To get non-blocking **and** interactive figures in IPython-based environments such as IPython, Spyder and Jupyter, we need to specify an interactive frontend such as Qt5, which is often installed by default:

```
%matplotlib qt5
```

Subsequent calls of pyplot functions will happen in non-blocking, interactive windows:

```
plt.plot([1.0, 2.0, -1.0, -0.0])
```

![Matplotlib using Qt5 -width:wider](_static/images/matplotlib_qt5.png)

Please consult section [](getting_started_configuring_spyder.md) to configure Spyder to use Qt5 by default, and therefore always get non-blocking, interactive figures.
