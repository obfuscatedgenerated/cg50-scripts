# CG50 Scripts

This repository contains scripts designed for the [Casio fx-CG50](https://education.casio.co.uk/products/cg50), although most may work on any Python/MicroPython enabled calculator.

The CG50 uses MicroPython 1.9.4. This means f-strings and other Python 3.6 features are not supported. You can test it here: https://micropython.org/unicorn/ (you may need to replace some stdin with defined values).

## Scripts

### [Pascal's Triangle](pascal.py)

This script calculates and displays Pascal's Triangle. It can be used to calculate the binomial coefficients.

### [Fibonacci](fibonacci.py)

This script calculates and displays the Fibonacci sequence. It also can be used to verify if a number is a Fibonacci number.

### [Binomial Expansion](binomial_expand.py)

This script uses the binomial expansion theorem to expand a polynomial. You may keep it in an algebraic form or substitute the variables with numbers.

### [Standard Derivatives](std_derivatives.py)

This script lists the standard derivatives and allows you to substitute into them. It also provides helper functions for other scripts to use (only works in non-minified script).

## The "min" directory

The "min" directory contains the scripts in a minified form. This is useful if you want to use the scripts on a calculator with limited storage, at the expense of readability, ease of editing, and initial load time. All were minified using [dflook's python-minifier](https://github.com/dflook/python-minifier) on default settings plus rename globals. This is done automatically on push via GitHub Actions.

## The "archive" directory

The "archive" directory contains scripts in a CPython 3.6 form. These were converted to support MicroPython on the CG50 and are kept for reference. They will not work on the CG50, and will not be maintained.