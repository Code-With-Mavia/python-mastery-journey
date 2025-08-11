# **Question 1: Dictionary Length**
# Given a dictionary, print how many key-value pairs it contains.

# Example:

# ```python
# data = {"name": "Alice", "age": 25, "city": "New York"}
# ```

# Output: `3`
data = {"name": "Alice", "age": 25, "city": "New York"}
print(len(data))

# ---

# **Question 2: Access Value by Key**
# Given a dictionary and a key, print the value for that key.

# Example:

# ```python
# person = {"name": "Bob", "age": 30}
# key = "name"
# ```

# Output: `Bob`

person = {"name": "Bob", "age": 30}
print(person["name"])
# ---

# **Question 3: Check if Key Exists**
# Given a dictionary and a key, print `"Found"` if the key exists, otherwise print `"Not Found"`.

# Example:

# ```python
# info = {"brand": "Toyota", "model": "Corolla"}
# key = "year"
# ```

# Output: `Not Found`
info = {"brand": "Toyota", "model": "Corolla"}
if 'year' in info:
    print("Found")
else:
    print("Not Found")
# ---

# **Question 4: Add New Key-Value Pair**
# Given an empty dictionary, add a key `"color"` with value `"red"`, then print the dictionary.

# Example:

# ```python
# d = {}
# ```

# Output: `{"color": "red"}`

d = {}
d.update({'color': 'red'})
print(d)
# ---

# **Question 5: Update Existing Value**
# Given a dictionary and a key `"score"`, increase its value by 10 and print the updated dictionary.

# Example:

# ```python
# scores = {"score": 50}
# ```

# Output: `{"score": 60}`
scores = {"score": 50}
scores["score"]=60
print(scores)
# ---

# **Question 6: Get All Keys**
# Given a dictionary, print all its keys as a list.

# Example:

# ```python
# student = {"name": "Sam", "grade": "A", "age": 20}
# ```

# Output: `['name', 'grade', 'age']`
student = {"name": "Sam", "grade": "A", "age": 20}
print(list(student))
# ---

# **Question 7: Get All Values**
# Given a dictionary, print all its values as a list.

# Example:

# ```python
# product = {"id": 101, "price": 20.5, "stock": 15}
# ```

# Output: `[101, 20.5, 15]`
product = {"id": 101, "price": 20.5, "stock": 15}
print(list(product.values()))
# ---

# **Question 8: Remove a Key**
# Given a dictionary and a key, remove the key-value pair if the key exists and print the dictionary.

# Example:

# ```python
# car = {"make": "Honda", "year": 2020, "color": "blue"}
# key_to_remove = "year"
# ```

# Output: `{"make": "Honda", "color": "blue"}`
car = {"make": "Honda", "year": 2020, "color": "blue"}
car.pop('year')
print(car)
# ---

# **Question 9: Clear Dictionary**
# Given a dictionary, clear all its contents and print the empty dictionary.

# Example:

# ```python
# info = {"a": 1, "b": 2, "c": 3}
# ```

# Output: `{}`
info = {"a": 1, "b": 2, "c": 3}
info.clear()
print(info)
# ---

# **Question 10: Safe Access with Default**
# Given a dictionary and a key, print the value if key exists; otherwise print `"Not Available"`.

# Example:

# ```python
# data = {"x": 100, "y": 200}
# key = "z"
# ```

# Output: `Not Available`
data = {"x": 100, "y": 200, }

if 'z' in data:
    print(data["z"])
else:
    print("Not Available")
 
# ---

# Question 11: Print Value for Key "name"
# Given a dictionary, print the value for the key "name" if it exists; otherwise, print "Key not found".
a={
    'name': 'Ali',
}
if 'name' in a:
    print(a["name"])
else:
    print("Key not found")
# Question 12: Add Key-Value Pair if Missing
# Given a dictionary, check if the key "age" exists. If not, add "age": 25 to the dictionary and print it.
b={
    'name': 'Ali',
}
if 'age' in a:
    print(a["age"])
else:
    b.update({'age':25})
    print(b)
# Question 13: Update Value for a Key
# Given a dictionary with a key "count", increase its value by 1 and print the updated dictionary.
c={
    "count":1
}
c["count"]+=1
print(c)
# Question 14: Check if Dictionary is Empty
# Given a dictionary, print "Empty" if it has no elements; otherwise, print "Not Empty".
d={
    "count":1 
}
if len(d)==0:
    print("Empty")
else:
    print("Not Empty")
# Question 15: Combine Two Dictionaries
# Given two dictionaries, combine them into one and print the result.

e={
    "count":1 
}
f={
    'name': 'Ali',
}
g={}
g.update({**e, **f})

print(g)
