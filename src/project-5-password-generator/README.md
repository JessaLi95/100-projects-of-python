# Secure password generator

_Select how many letters, numbers, and symbols you want, and generate a random strong password_

1. Define function to simplify the similar code.
```commandline
def function_name(variable1, variable2):
    action 1
    action 2
    return result_variable
    
```
2. Call the function after defining it.
```commandline
result = function(variable_1, variable_2)
```
3. Shuffle the string and convert it into a random list.
```
random_list = random.sample(string, len(string))
```
4. Convert the list into string with certain spacer.
```commandline
string = "spacer".join(map(str, list_name))
```
