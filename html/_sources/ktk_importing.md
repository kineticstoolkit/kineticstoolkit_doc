# Importing Kinetics Toolkit

There are two ways to import Kinetics Toolkit:

- In standard mode: `import kineticstoolkit as ktk`
- In lab mode: `import kineticstoolkit.lab as ktk`

:::{note}
The first import can take several seconds; subsequent imports are much faster.
:::

Lab mode is a convenience tool that sets some defaults for a more enjoyable data processing session in IPython-based environments such as Spyder. It automatically imports all installed [Kinetics Toolkit extensions](extensions.md), makes cosmetics changes to the representations (repr) of dictionaries, arrays and warnings, and improves Matplotlib defaults colours and sizes for interactive biomechanics work. See [](api/ktk.import_extensions.rst) and [](api/ktk.change_defaults.rst) for more information.

```
import kineticstoolkit.lab as ktk
```

is equivalent to:
```
import kineticstoolkit as ktk
ktk.import_extensions()
ktk.change_defaults()
```
