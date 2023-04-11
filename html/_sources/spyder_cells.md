# Code cell

When a script grows in length, it can be practical to run only one section at a time. A script can be split into cells using this sequence of characters which acts as a separator:

```
# %%
```

You can also name cells by adding a title next to the separator. This is generally a good idea to keep control of your growing script:
```
# %% Load results from previous acquisition

[...]

# %% Report these results in a local coordinate system

[...]

```

You can execute a cell by placing the cursor in that cell, then by clicking on the `Run current cell` (middle button) or `Run current cell and go to the next one` (right button) in the following toolbar:

![](_static/images/spyder_toolbar.png)

As an exercise, create a file named `exercise.py` that contains two cells. A first cell prints "Hello", and a second cell prints "World". Run the cell of your choice using the toolbar icons.
