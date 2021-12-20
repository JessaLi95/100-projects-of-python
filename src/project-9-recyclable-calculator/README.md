# Python recyclable calculator

_Do the calculation based on the previous result or start a new calculation_

1. Output function, return instead of print the action, makes the action recyclable.
```
def function_name():
    action
    return action
```
2. Multiple return _*return is the end of a function_
```
def function_name_2():
    action_1
    action_2
    return action_1
    return action_2
```
3. Docstring, write the explanation of a function, hover over the function, show description.
```
def function_name_3():
    """ description of the function."""
```
4. Change the string to Title Case format.
```
str.title()
```
5. Function recursion - Recursion is the process of defining a problem (or the solution to a problem) in terms of (a simpler version of) itself.
```
def function_name_4():
    action_1
    action_2
    function_name_4() # Each time call the function, reset the variable inside.
```