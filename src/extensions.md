# Extensions

Kinetics Toolkit provides very generic functions that should apply to a wide variety of use cases. For more specific use cases and for future feature development, we use extensions, via the [kineticstoolkit_extensions](https://github.com/kineticstoolkit/kineticstoolkit_extensions) package.


## Installing extensions

All extensions are included in the single `kineticstoolkit_extensions` package, which is installed like you installed `kineticstoolkit`, e.g., using pip, conda or mamba:

```
pip install kineticstoolkit_extensions
```

or

```
mamba install kineticstoolkit_extensions
```

or

```
conda install -c conda-forge kineticstoolkit_extensions
```


## Using extensions

When `kineticstoolkit_extensions` is installed, all its contents becomes available in the `kineticstoolkit.ext` namespace. For example, to calculate the velocity of a wheelchair wheel using the `pushrimkinetics` extension:

```
import kineticstoolkit.lab as ktk

ktk.ext.pushrimkinetics.calculate_velocity()
```


## Developing extensions

Please consult [](dev_extensions) to learn how to develop and share your own extensions.
