# Magic Methods in Python OOP

## Overview

This folder contains programs that demonstrate Python's **magic methods (dunder methods)**. These special methods allow custom objects to integrate seamlessly with Python's built-in functions and operators, making classes more readable, comparable, and expressive.

## Programs

### 1. `book_str_method.py`

* **Concept:** `__str__()`
* Returns a user-friendly string representation of a `Book` object.

### 2. `shopping_cart_len_method.py`

* **Concept:** `__len__()`
* Returns the total number of items in a `ShoppingCart` object.

### 3. `employee_repr_method.py`

* **Concept:** `__repr__()`
* Returns the official string representation of an `Employee` object.

### 4. `student_eq_method.py`

* **Concept:** `__eq__()`
* Compares two `Student` objects based on their USN.

### 5. `product_lt_method.py`

* **Concept:** `__lt__()`
* Compares two `Product` objects based on their price using the `<` operator.

### 6. `wallet_add_method.py`

* **Concept:** `__add__()`
* Adds the balances of two `Wallet` objects using the `+` operator.

## Learning Outcomes

After completing this module, you will be able to:

* Understand the purpose of Python magic methods.
* Customize how objects are represented using `__str__()` and `__repr__()`.
* Compare custom objects using `__eq__()` and `__lt__()`.
* Overload operators such as `+` using `__add__()`.
* Make custom classes work naturally with Python's built-in functions and operators.
* Write cleaner, more Pythonic, and maintainable OOP code.


