# Simple Perceptron

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success)]()

I could make an simple Perceptron that you give him Data and he will try to predict the result, with the validation and data i gave him in the Training.

#### I think everyone knows how it works but:
- the main Part is how you implement to make it "learn" adjusting the Weights using a gradient ecuation
``` python
                        gradient = (2 / len(X)) * (X.T @ L)
```
- YOU CANT GIVE HIM ANY DATA. I put an python file named
> see_linear.py

Where you can see if your Data is Linealy Separable

- All the System idea is about Proportions, how much of this part of the data actually Import in the final result. The more complex the neural network **the more** *abstract* it is.