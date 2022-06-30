# Extensions

Kinetics Toolkit provides very generic functions that should apply to a wide variety of use cases. For more specific use cases, or to quickly develop and share new features, we provide a simple extension mechanism.

## Installing extensions

Here is a list of known extensions. Follow the link for a detailed description, tutorials, and installation procedure. Please [contact us](https://github.com/felixchenier/kineticstoolkit/discussions) to add your own extension to this list.

- [pushrimkinetics](https://github.com/felixchenier/kineticstoolkit_pushrimkinetics): Provide functions to process kinetic data from instrumented wheelchair wheels. Replaces the former `ktk.pushrimkinetics` module that is now deprecated.

## Using extensions

If you imported Kinetics Toolkit in lab mode:

```
import kineticstoolkit.lab as ktk
```

then the contents of all installed extensions is available under the `ktk.ext` namespace. Type `dir(ktk.ext)` to know what extensions are available.

If you imported Kinetics Toolkit directly, you need to manually load the extensions:

```
import kineticstoolkit as ktk
ktk.ext.load_extensions()
```



## Developing extensions

Please consult [this page](dev_extensions) to learn how to develop and share your own extensions.
