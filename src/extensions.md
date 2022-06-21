# Extensions

{{ dev }}

Kinetics Toolkit provides very generic functions that should apply to a wide variety of use cases. For more specific use cases, or to quickly develop and share new features, we provide a simple extension mechanism.

## Installing extensions

Here is a list of known extensions and how to install it. Please [contact us](https://github.com/felixchenier/kineticstoolkit/discussions) to add your own extension to this list.

### [pushrimkinetics](https://github.com/felixchenier/kineticstoolkit_pushrimkinetics)

Provide functions to process kinetic data from instrumented wheelchair wheels.

Installing: 
```
pip install git+https://github.com/felixchenier/kineticstoolkit_pushrimkinetics
```

Uninstalling:
```
pip uninstall kineticstoolkit_pushrimkinetics
```

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

Long story short, any installed package whose name begins with `kineticstoolkit_` is considered as an extension to Kinetics Toolkit. Its contents will be imported in the `ktk.ext` namespace.

If you want to develop and share your own extensions, but do not know how to share python modules or packages, we provide a template and guidelines to get you on road, using the `pip git+https` installation method.

**Step 1.** Install the `pytest` module. This will allow you to write and run unit tests for your extension.

**Step 2.** Find a name for your extension.

**Step 3.** Go to this repository: https://github.com/felixchenier/kineticstoolkit_extension, and use it as a template for your own, new repository. In the following example, we will use `pushrimkinetics` as the extension name.

![](_static/images/extension_github_template.png)

Name your new repository `kineticstoolkit_EXTENSIONNAME`, replacing EXTENSIONNAME by the name of your extension.

![](_static/images/extensions_github_new_repository.png)

**Step 4.** Clone your new repository on your computer using the git tool of your choice.

**Step 5:** Edit the header of `setup.py` to match your extension and personal information.

````
"""Setup tool for building a pip-accessible package."""

import setuptools

#--------------------------------------------------------------------------------
# Please modify to fit your extension (particularly the text in CAPITALS)
#--------------------------------------------------------------------------------
name = "kineticstoolkit_pushrimkinetics"
description = "Provide functions to process kinetic data from instrumented wheelchair wheels."
url = "https://github.com/felixchenier/kineticstoolkit_pushrimkinetics"
author = "Félix Chénier"
author_email = "chenier.felix@uqam.ca"
#--------------------------------------------------------------------------------
````

**Step 6:** Change `EXTENSIONAME`, `AUTHORNAME`, `AUTHOREMAIL`, `YEAR` and `GITHUBUSER` in every file for their real values.

**Step 7:** Put your actual code in `kineticstoolkit_EXTENSIONNAME.py`.

**Step 8:** Write some test functions in `test_extension.py`. Such test functions usually perform a simple operation and ends with:

```
assert some_variable == some_contents
```

**Step 9:** Check that your extension works. In a terminal, change directory to the toplevel of your repository, then run `pytest`. All your test functions should be launched and pass.

**Step 10:** Edit `README.md` to include installation and usage instructions.

**Step 11:** Commit and push your changes.

Your extension can now be installed using:

```
pip install git+https://github.com/USERNAME/kineticstoolkit_EXTENSIONNAME
```

It would be a good idea to test it a last time in a fresh testing environment. If you are using conda:

````
cd
conda create -n test -c conda-forge kineticstoolkit
conda activate test
pip install git+https://github.com/USERNAME/kineticstoolkit_EXTENSIONNAME
````

Now launch python, import kineticstoolkit and try your extension.

**Step 12.** Publicize your extension on the [Kinetics Toolkit's discussions forum](https://github.com/felixchenier/kineticstoolkit/discussions). We'll add it to this page. If things are not as smooth as you'd want, don't hesitate to [ask for help](https://github.com/felixchenier/kineticstoolkit/discussions).
