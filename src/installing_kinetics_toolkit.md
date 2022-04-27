# Installing Kinetics Toolkit

Kinetics Toolkit is distributed via both [conda-forge](https://anaconda.org/conda-forge/kineticstoolkit) and [PyPi](https://pypi.org/project/kineticstoolkit). The source code is hosted on [git-hub](https://github.com/felixchenier/kineticstoolkit).

Since reading c3d files relies on [ezc3d](https://github.com/pyomeca/ezc3d) which binaries are distributed only via conda-forge, the recommended installation method is therefore using conda-forge. If needed, go to the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html) to install a minimal conda installation.

## Install and update Kinetics Toolkit

In the Anaconda/Miniconda prompt or terminal:

```
conda install -c conda-forge kineticstoolkit
```

You can keep Kinetics Toolkit up to date by typing this command regularly:

```
conda update -c conda-forge kineticstoolkit
```

## Configuring Matplotlib graphics in IPython/Spyder

Kinetics Toolkit's interactive functions make use of IPython's integration of Matplotlib/Qt5's event loop. When you want to use interactive functions in IPython, type:

```
%matplotlib qt5
```

beforehand.

Alternatively, I highly recommend using the Spyder development environment since it is so oriented towards science. To configure Spyder for interactive graphics, go to the Spyder's preferences, to the **IPython console** item, then to the **Graphics** pane. In the **Graphics backend** box, select **Qt5**, then restart Spyder.

## Check that Kinetics Toolkit loads

The last step is to verify that you are able to import Kinetics Toolkit in an interactive IPython console. This should work without error:

```
>>> import kineticstoolkit as ktk
```

or

```
>>> import kineticstoolkit.lab as ktk
````
