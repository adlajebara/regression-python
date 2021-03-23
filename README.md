# Regression-Python
I wrote this code as part of an assingemnt while taking a summer course in Python at Chalmers university.

The program takes a set of data and with polynomial regression, it can find a polynom of an arbitrary degree n and plots it using [matplotlib](https://matplotlib.org/). The task of the polynomial regression is to find the list of parameters a for a given polynomial degree n. 

## Setup
Install the [NumPy](https://numpy.org/) library: 
```bash
$ pip3 install numpy
```

Install the [matplotlib](https://matplotlib.org/) library: 
```bash
$ pip3 install matplotlib
```


## How to run it

To compute a polynomial of degree four: 
```bash
$ python3 numpy_regression.py dataset3.txt 4
```

To compute a polynomial of degree three: 
```bash
$ python3 numpy_regression.py dataset2.txt 3
```

To compute a polynomial of degree two: 
```bash
$ python3 numpy_regression.py dataset1.txt 2
```

