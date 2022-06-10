# Extensions

{{ dev }}

The core Kinetics Toolkit library aims to provide very generic functions that apply to a wide variety of use cases. For more specific use cases, or to quickly develop and share new features, we provide an extension mechanism.

Any package that starts by `kineticstoolkit_` registers as an extension. After installing such package, it can be loaded in the `ktk.ext` namespace.

For example, the `kineticstoolkit_pushrimkinetics` package provides functions that are specific to wheelchair propulsion analysis using instrumented wheels, e.g.:
- `read_file()`
- `calculate_velocity()`
- etc.

After installing this package, then any of these lines:

````
import kineticstoolkit.lab as ktk
````

```
import kineticstoolkit as ktk
ktk.ext.load_extensions()
````

will import it under the `ktk.ext.pushrimkinetics` namespace:
- `ktk.ext.pushrimkinetics.read_file()`
- `ktk.ext.pushrimkinetics.calculate_velocity()`
- etc.

## List of available extensions

Please contact us to add your own extension to this list.

| Name            | Description                                                                    | How to install |
| --------------- | ------------------------------------------------------------------------------ | -------------- |
| pushrimkinetics | Provide functions to process kinetic data from instrumented wheelchair wheels. |                | 

:::{margin} #todo
Link to the github repository.
:::

## Developing extensions

:::{margin} #todo
write how to develop extensions, based on fork of a template repository.
:::
