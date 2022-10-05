# CG50 Scripts

This repository contains scripts designed for the [Casio fx-CG50](https://education.casio.co.uk/products/cg50), although most may work on any Python/MicroPython enabled calculator.

## Scripts

### [Pascal's Triangle](pascal.py)

This script calculates and displays Pascal's Triangle. It can be used to calculate the binomial coefficients.

### [Fibonacci](fibonacci.py)

This script calculates and displays the Fibonacci sequence. It also can be used to verify if a number is a Fibonacci number.

### [Binomial Expansion](binomial_expand.py)

This script uses the binomial expansion theorem to expand a polynomial. You may keep it in an algebraic form or substitute the variables with numbers.

## The "min" directory

The "min" directory contains the scripts in a minified form. This is useful if you want to use the scripts on a calculator with limited storage, at the expense of readability, ease of editing, and initial load time. All were minified using [dflook's python-minifier](https://github.com/dflook/python-minifier) on default settings plus rename globals. This is done automatically on push via GitHub Actions.