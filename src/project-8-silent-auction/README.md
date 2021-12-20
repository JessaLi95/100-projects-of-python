# Secret auction
_!!! This code only works in replit.com, because there is no [clean_screen() function](https://www.py4u.net/discuss/236233) that can be defined in Python IDEs._

1. Append to dictionary
```
dictionary_name[new_key] = "new_value"
```
2. Retrieve from a dictionary
```
dictionary[key_name]
```
3. Build a dictionary
```
new_dictionary = {
    "key_1" : "Value_1",
    "key_2" : "Value_2",
    "key_3" : "Value_3",
}
```
4. Loop in dictionary
```
for key in dictionary_name:
    print(key)
# Will print each key name
```

5. Find the maximum value in a dictionary
```
find_max = max(dictionary_name, key=dictionary_name.get)
print(find_max)
# Will print the key name instead of value.
```