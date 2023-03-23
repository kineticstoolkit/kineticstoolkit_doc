---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]

%matplotlib inline
```


# Writing code in the console

:::{sidebar}
![Spyder screenshot](_static/images/spyder_screenshot.png)
:::

The console (section A) allows executing one command at a time. It also shows the result of calculations. Try entering this simple calculation in the console:

```{code-cell} ipython3
:tags: [remove-output]
1 + 2
```

The console will show the results just below your command:

```{code-cell} ipython3
:tags: [remove-input]
1 + 2
```

You can also write multiple-line commands using CTRL+Enter. Both are executed, but only the result from the last command is printed:

```{code-cell} ipython3
1 + 2
3 + 4
```
