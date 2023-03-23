# Extensions

Kinetics Toolkit provides very generic functions that should apply to a wide variety of use cases. For more specific use cases, or to quickly develop and share new features, we provide a simple extension mechanism.

## 📄 Installing extensions

Here are links to known extensions, where you can find a detailed description, tutorials, and installation procedure. Please [contact us](https://github.com/felixchenier/kineticstoolkit/discussions) to add your own extension to this list.

- [n3d](https://github.com/felixchenier/kineticstoolkit_n3d): Provide the `read_n3d` function to read Optotrak n3d acquisition files.
- [pushrimkinetics](https://github.com/felixchenier/kineticstoolkit_pushrimkinetics): Provide functions to process kinetic data from instrumented wheelchair wheels. Replaces the former `ktk.pushrimkinetics` module that is being moved out from the core library.

## 📄 Using extensions

Use [](api/ktk.import_extensions.rst) to import all installed extensions into the `ktk.ext` namespace. For example, if you installed the pushrimkinetics extension above, then its functions will be available as `ktk.ext.pushrimkinetics.read_smartwheel()`, `ktk.ext.pushrimkinetics.calculate_power()`, etc.

If you imported Kinetics Toolkit in [lab mode](getting_started_installing.md), the extensions are already imported. There is no need to use [](api/ktk.import_extensions.rst).

## 🛠 Developing extensions

Please consult [](dev_extensions) to learn how to develop and share your own extensions.
