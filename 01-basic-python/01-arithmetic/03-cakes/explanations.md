# Assignment

Write a function `cakes(eggs, butter, flour)` that computes
the number of cakes you can bake using the given ingredients.
For each cake, you need 5 eggs, 250g butter and 250g of flour.
The parameters `butter` and `flour` are given in grams.

## Two kinds of division

Open the Python console:

```bash
$ python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

Experiment to determine what the difference is between
Python's two division operators `/` and `//`. For example, you can try inputting the
following lines (omit the `>>>`, it represents the Python prompt):

```python
>>> 5 / 2

>>> 5 // 2
```

## Minimum and maximum

Python has `min` and `max` built-in:

```python
# You can give the values to be compared as a series of arguments
min(3, 5, 2, 6, 1, 4)    # Returns 1
max(3, 5, 2, 6, 1, 4)    # Returns 6

# You can also pass a list
min([5, 2, 9, 4])        # Returns 2

# Works on all comparable values
min('t', 'd', 'p')       # Returns 'd'
```

Now, to test your `cake` function, enter the following command in this directory:

```bash
$ scripting test
PASS 7
FAIL 0
SKIP 0
Score: 1.0/1
```
