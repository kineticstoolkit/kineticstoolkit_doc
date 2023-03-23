# Single and double quotes

A string is created by enclosing characters between quotes. Python does not make a difference between single-quotes `'` and double-quotes `"`. Therefore, the following strings are equivalent:

```
"Hello world!"
'Hello world!'
```

Normally, we will use `"` if the string contains apostrophes `'`; inversely, we will use `'` if the string contains double-quotes `"`. For instance, both these strings are correctly defined:

```
"It's time to lunch."
'I would not call it "results"...'
```

but the following ones generate syntax errors, because the apostrophe or double-quote closes the string before reaching the ending delimiter:

```
'It's time to lunch'
"I would not call it "results"..."
```
