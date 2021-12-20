# Who is more popular

1. Define empty global variable to store the return value from a function.
```commandline
vairable_name = None
```
2. To modify a global variable inside the function:
```commandline
def function():
global variable_name
```
3. Make the boolean condition statement more concise.
```commandline
def compare_choice():
    flag = a > b        # a > b = True,
    if user_chose == 'a':   # user thinks a > b,
        return flag         # flag = True
    elif user_chose == 'b':     # a > b is True, user thinks b > a
        return not flag     # if user is wrong, flag = False; if user is right, 'a > b' is wrong, flag = Flase
```
4. Return a f-string from function:
```commandline
def function_name():
    action
    return f"{variable_a}, and {variable_b}."
```