# What is Kinetics Toolkit

## Summary

Kinetics Toolkit is a Python package for generic biomechanical analysis of human motion that is easily accessible by new programmers. The only prerequisite for using this toolkit is having minimal to moderate skills in Python and Numpy.

While Kinetics Toolkit provides a dedicated class for containing and manipulating data (`TimeSeries`), it loosely follows a procedural programming paradigm where processes are grouped as interrelated functions in different submodules, which is consistent with how people are generally introduced to programming. Each function has a limited and well-defined scope, making Kinetics Toolkit generic and expandable. Particular care is given to documentation, with extensive tutorials and API references. Special attention is also given to interoperability with other software programs by using Pandas Dataframes (and therefore CSV files, Excel files, etc.), JSON files or C3D files as intermediate data containers.

Kinetics Toolkit is accessible at https://kineticstoolkit.uqam.ca and is distributed via conda and pip[^1].

[^1]: This Summary is from the white paper published in
[Journal of Open Source Software](https://joss.theoj.org/papers/10.21105/joss.03714).

## Objectives of this project

- Build an intuitive and elegant Python package that leverages the power of biomechanical analysis to people who are not formed in programming or engineering;

- Build a strong documentation around this package to:
    - Teach or remind the basic principles of biomechanics to newcomers;
    - Explain how Kinetics Toolkit implements these principles; 
    - Teach users how to use Kinetics Toolkit on their data without relying on do-it-all, commercial graphical interfaces.

## How to contribute

At the moment, I think Kinetics Toolkit has made a moderate way into its first objective. There is however still much to do. If you find this long-term project appealing and want to contribute, here are different ways to help:

- Try it and tell me your thoughts and ideas on the interface, features and documentation;
- Test it and report bugs;
- Communicate with me to help with documentation;
- Extend it to develop missing functionality and share the results;
- Citing it in your work;
- Possibly many other ways to help.

A good start would be to check out the [development website](https://felixchenier.uqam.ca/ktk_develop) or fork the repository on [GitHub](https://github.com/felixchenier/kineticstoolkit).


## How to cite

If you find Kinetics Toolkit useful and want to credit it in your work (which I would much appreciate), then please cite this paper:

Chénier, F., 2021. Kinetics Toolkit: An Open-Source Python Package to Facilitate Research in Biomechanics.
*Journal of Open Source Software* 6(66), 3714. https://doi.org/10.21105/joss.03714

---

I hope Kinetics Toolkit may help you in your biomechanical analyses; have a good read!
