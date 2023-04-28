---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell}
:tags: [remove-cell]

%matplotlib inline
```

# Setting the axes limits

When we create a plot interactively, we can zoom on a particular section using the figure's Zoom and Pan buttons. It is also possible to zoom programmatically while we create the figure, using {{plt_axis}}.

## Rectangular zoom

Let's create some random data:

```{code-cell}
import matplotlib.pyplot as plt

random_data = [
    0.60921838, 0.80049539, 0.11593785, 0.90703271, 0.75252107,
    0.72976933, 0.93364321, 0.14401492, 0.35255034, 0.68628490,
    0.76262073, 0.48124243, 0.73965093, 0.21237858, 0.63081351,
    0.75098067, 0.87658458, 0.68637267, 0.30947229, 0.19968510,
    0.59710015, 0.98464582, 0.05031455, 0.56996651, 0.74360835,
    0.30706612, 0.92693383, 0.63387122, 0.30740088, 0.46847444,
    0.99559865, 0.84777408, 0.21486266, 0.65472302, 0.51600203,
    0.3724475 , 0.0579805 , 0.62423827, 0.33997655, 0.14256265,
    0.5013935 , 0.98862076, 0.58028518, 0.15716675, 0.83572021,
    0.0119542 , 0.7257411 , 0.99901993, 0.69608303, 0.46573617
]

plt.plot(random_data, "o-");
```

To zoom on a specific portion of the plot, we call {{plt_axis}}, which takes for argument a list containing `[xmin, xmax, ymin, ymax]`. For example, to better see the portion between $x \geq 20$ and $x \leq 30$:

```{code-cell}
plt.plot(random_data, "o-")
plt.axis([20, 30, 0, 1]);
```

## 📄 Square zoom

By defaults, plots are rectangular and will adapt their shape to maximize the span on both x and y axes. However, in some circumstances, we need both x and y axes to have the same scale, e.g., to plot the (x, y) trajectory of a point in space. To set the same scale to both axes, we use `plt.axis("square")`. For example, plotting the (x, y) coordinates of a true circle looks like an ellipse by default:

```{code-cell}
x = [ 1.        ,  0.96592583,  0.8660254 ,  0.70710678,  0.5       ,
      0.25881905,  0.        , -0.25881905, -0.5       , -0.70710678,
     -0.8660254 , -0.96592583, -1.        , -0.96592583, -0.8660254 ,
     -0.70710678, -0.5       , -0.25881905, -0.        ,  0.25881905,
      0.5       ,  0.70710678,  0.8660254 ,  0.96592583,  1.        ]
     
y = [ 0.        ,  0.25881905,  0.5       ,  0.70710678,  0.8660254 ,
      0.96592583,  1.        ,  0.96592583,  0.8660254 ,  0.70710678,
      0.5       ,  0.25881905,  0.        , -0.25881905, -0.5       ,
     -0.70710678, -0.8660254 , -0.96592583, -1.        , -0.96592583,
     -0.8660254 , -0.70710678, -0.5       , -0.25881905, -0.        ]
     
plt.plot(x, y, "o-");
```

This is solved by setting the axis to "square":

```{code-cell}
plt.plot(x, y, "o-")
plt.axis("square");
```
