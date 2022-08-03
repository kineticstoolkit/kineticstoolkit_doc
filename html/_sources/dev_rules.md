# Development rules

## Rule 1: Code of conduct

Please make sure to adhere to our [code of conduct](dev_code_of_conduct.md).

## Rule 2: Consider writing documentation instead of code

Before even starting to develop a new function, one should ask this important question: **Should this feature really be developed, or should I write a tutorial instead?**

We remind that Kinetics Toolkit aims to provide tools for the user to achieve their needs in biomechanical research. Often, the best way to control our data is by learning how to do it instead of using a function performs it for us. In that view, any new feature should start with a [discussion](https://github.com/felixchenier/kineticstoolkit/discussions).

- To develop documentation, please contribute to the [kineticstoolkit_doc](https://github.com/felixchenier/kineticstoolkit_doc) repository, that versions this website's code.
- Otherwise, to develop code, then continue with this guide.

## Rule 3: For new features, consider writing an extension

Kinetics Toolkit supports extensions. This means you can program and distribute your own functions withing ktk, while keeping in full control and property of your code. Extensions are a good way to test new features and evaluate if they should or shouldn't become part of the core library.

## Rule 4: Contributing code to the core library

To contribute code to the core library, please use the usual method of forking, writing, testing, and writing a pull request that is described [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models).

Before creating a pull request, please ensure that:

- The new code respects the [coding style](dev_coding_style.md).
- Your new code is tested using proper unit tests.

To ensure that this is the case, run `ktk.dev.run_tests()`. You should get no error.
