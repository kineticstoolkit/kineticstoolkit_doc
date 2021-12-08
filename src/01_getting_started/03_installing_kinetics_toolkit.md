# Installing Kinetics Toolkit

Kinetics Toolkit is distributed via both [conda-forge](https://anaconda.org/conda-forge/kineticstoolkit) and [PyPi](https://pypi.org/project/kineticstoolkit). The source code is hosted on [git-hub](https://github.com/felixchenier/kineticstoolkit).

Since reading c3d files relies on [ezc3d](https://github.com/pyomeca/ezc3d) which binaries are distributed only via conda-forge, the recommended installation method is therefore using conda-forge.

## Install and update Kinetics Toolkit

Still in the prompt/terminal:

```
conda install -c conda-forge kineticstoolkit ezc3d
```

You can keep Kinetics Toolkit up to date by typing this command regularly:

```
conda update -c conda-forge kineticstoolkit
```

## Configuring Matplotlib graphics in IPython/Spyder

Kinetics Toolkit's interactive functions make use of IPython's integration of Matplotlib/Qt5's event loop. When you want to use interactive functions in IPython, type:

    %matplotlib qt5

beforehand.

Alternatively, since the Spyder IDE is so oriented towards science and it uses IPython, I highly suggest using this development environment. To configure Spyder for interactive graphics, go to the Spyder's preferences, to the **IPython console** item, then to the **Graphics** pane. In the **Graphics backend** box, select **Qt5**, then restart Spyder.

## Check that Kinetics Toolkit loads

The last step is to verify that you are able to import Kinetics Toolkit in an interactive IPython console. This should work without error:

```
>>> import kineticstoolkit
```

or

```
>>> import kineticstoolkit.lab as ktk
````
