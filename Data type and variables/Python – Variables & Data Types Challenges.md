# 🧠 Python Challenge Set – Variables & Data Types Only

This problem set is designed to test your understanding of **Python variables and data types** — nothing else.

---
![Repo Size](https://img.shields.io/github/repo-size/yourusername/python-variable-datatype-challenges)
![Forks](https://img.shields.io/github/forks/yourusername/python-variable-datatype-challenges?style=social)
![Stars](https://img.shields.io/github/stars/yourusername/python-variable-datatype-challenges?style=social)
![Issues](https://img.shields.io/github/issues/yourusername/python-variable-datatype-challenges)


## 📘 Problem List

### 🟢 Easy

---

#### 💡 Problem 1: `Type Checker`
Declare a variable with an integer value. Print its type.

---

#### 💡 Problem 2: `Three Types`
Declare three variables:  
- one integer  
- one float  
- one string  
Print their types, each on a new line.

---

#### 💡 Problem 3: `String to Integer`
You are given a string containing a number: `"10"`  
Convert it to an integer and add `5`.  
Print the result.

---

#### 💡 Problem 4: `Float to Int`
You are given a float value `3.8`  
Convert it to an integer and print the result.

---

#### 💡 Problem 5: `Add Float and Int`
Declare a float `a = 2.5` and an integer `b = 2`.  
Add them and print:  
1. The result  
2. The data type of the result

---

### 🟡 Medium

---

#### 💡 Problem 6: `User Input Casting`
Take three inputs from the user:
1. A float  
2. An integer  
3. A boolean in string form (`"True"` or `"False"`)  

Convert them to their correct types and compute:  
```

(float\_input \* int\_input) + bool\_input

````

---

#### 💡 Problem 7: `String to Bool`
Given the string `"False"`, convert it to a boolean.  
Then cast it to an integer and print the result.

---

#### 💡 Problem 8: `Multiply String Numbers`
You are given two string inputs:
- `"2.5"`
- `"4"`  

Multiply them after converting to appropriate types.  
Print the result.

---

#### 💡 Problem 9: `Concatenate Mixed Types`
You are given:
- an integer `x = 5`
- a float `y = 3.14`
- a string `z = "Python"`  

Concatenate all three into a single string and print.

---

#### 💡 Problem 10: `Division Type`
You are given:
- `a = "10"` (string)
- `b = "2.5"` (string)  

Convert them to their proper types and divide `a / b`.  
Print:
1. The result  
2. The data type of the result

---

#### 💡 Problem 11: `String Truth`
You are given the string `"False"`  
Convert it to a boolean and print its truthiness as an integer.

---

#### 💡 Problem 12: `Nested Casting`
Perform the following:
1. Convert `"5.9"` to float  
2. Convert the result to int  
3. Add `True` to it  
Print the final result.

---

### 🔴 Hard

---

#### 💡 Problem 13: `Evaluate Expression`
Given:
```python
a = "3"
b = "2.5"
c = "True"
````

Compute the following:

```python
int(a) * float(b) + int(c == "True")
```

---

#### 💡 Problem 14: `Bool of "False"`

Convert the string `"False"` to a boolean.
Then convert that boolean to an integer.
Print the result.

---

#### 💡 Problem 15: `String * Int + Float`

Perform the operation:

```python
("5" * 2) + str(10.0)
```

Print the result.

---

#### 💡 Problem 16: `Mixed Logic`

You are given:

* `a = "10"`
* `b = "3.5"`
* `c = "False"`

Compute:

```python
int(a) + float(b) + int(c == "True")
```

---

#### 💡 Problem 17: `Truthy Without If`

Take user input (`"True"` or `"False"` as string).
Print `1` if the input is `"True"`, otherwise `0`.
**Do not use if-else or any conditions.**

---

#### 💡 Problem 18: `Empty String`

Print the integer value of:

```python
bool("")
```

---

#### 💡 Problem 19: `Float × 10 - Bool`

Given:

* `x = "3.3"`
* `y = "False"`

Compute:

```python
float(x) * 10 - int(y == "True")
```

---

#### 💡 Problem 20: `All-in-One Expression`

Given:

```python
a = "10.5"
b = "5"
c = "True"
```

Compute:

```python
float(a) + int(b) + int(c == "True")
```
