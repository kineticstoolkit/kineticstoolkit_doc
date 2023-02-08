# 📖 Matplotlib frontend

:::{card} Summary
This section illustrates how Matplotlib may behave differently on different computers and setups, and suggests a method to configure Spyder and Matplotlib to always generate non-blocking, interactive figures.
:::

Matplotlib runs on almost any platform, can be embedded in applications, can be interactive or generate static figures... since its purposes are so varied, its main behaviour can change from one setup to another. For instance:

## 📄 Python and IPython

To plot a curve in the standard Python or IPython interpreter, we need to tell it to show the curve, using {{plt_show}}:

![](_static/images/matplotlib_python1.png)
![](_static/images/matplotlib_python2.png)
The different buttons on the figure allow some interaction with the plot:

- ![](_static/images/matplotlib_move.png) Move the figure around (panning);
- ![](_static/images/matplotlib_zoom_to_rect.png) Zoom on the figure;
- ![](_static/images/matplotlib_back.png) Undo the last pan/zoom operation;
- ![](_static/images/matplotlib_forward.png) Redo the last pan/zoom operation;
- ![](_static/images/matplotlib_home.png) Reset to the initial pan/zoom;
- ![](_static/images/matplotlib_filesave.png) Save the figure to an image file.

However, by default, it is impossible to write new code while the figure is displayed, which can be an inconvenience.


## 📄 Spyder and Jupyter

On the contrary, in Spyder, plots appear by default in the Plots pane and do not block the command console. We don't need to run `plt.show`.

![](_static/images/matplotlib_spyder_default.png)

In Jupyter, plots appear by default just after its command block, and we also don't need to run `plt.show`.

![](_static/images/matplotlib_jupyter.png)

However, in both Spyder and Jupyter, the default settings generate static (non-interactive) figures, that don't allow for zooming, panning, clicking, etc.

## 📄 Interactive figures

To get non-blocking **and** interactive figures in IPython-based environments such as IPython itself, Spyder and Jupyter, we need to specify an interactive frontend (such as Qt5 which is often installed by default, but others also exist) using this "magic command":

```
%matplotlib qt5
```

Subsequent calls of pyplot functions will happen in discrete, interactive windows:

![](_static/images/matplotlib_qt5.png)

In Spyder, it is possible to configure Matplotlib to always use Qt5. This is what we recommend, particularly if you aim to use the interactive objects of the Kinetics Toolkit package, such as the 3D visualizer [ktk.Player](kinematics_load_visualize.md).

Please consult section [](python_configuring_spyder.md) to know how to perform this configuration in Spyder.

