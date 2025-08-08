Great! Below is an **improved HackerRank/LeetCode-style Markdown file** of **20 Python questions** focused only on **variables and data types** (no loops, no conditionals, no DSA). Each question includes:

* ✅ Problem title
* 📋 Problem description
* 🔢 Input format
* 🧾 Constraints
* 🧮 Output format
* 🔍 Sample Input/Output

---

### 📁 File Name: `variables_and_data_types_challenges.md`

---

```markdown
# 🐍 Python Challenges: Variables & Data Types (Beginner to Advanced)

Welcome to a curated set of **20 Python problems** that test your understanding of **primitive data types**, **type conversion**, **input handling**, and **expressions**.

---

## ✅ Level: Beginner (Q1–Q5)

---

### Q1. Type Check
**Description:**  
Assign `5` to a variable and print its data type.

**Input Format:**  
None

**Output Format:**  
Print the data type of the variable.

**Sample Output:**  
```

\<class 'int'>

```

---

### Q2. Print 3 Types  
**Description:**  
Create three variables: one `int`, one `str`, and one `float`. Print all of them with their types.

**Input Format:**  
None

**Output Format:**  
Three lines showing variable values and their types.

---

### Q3. String to Int Addition  
**Description:**  
Convert the string `"10"` into an integer and add `5` to it.

**Output Format:**  
Print the result as an integer.

**Sample Output:**  
```

15

```

---

### Q4. Float to Integer  
**Description:**  
Convert `3.5` into an integer using type casting and print it.

**Sample Output:**  
```

3

```

---

### Q5. Mixed-Type Addition  
**Description:**  
Add `10` (int) and `3.5` (float). Store and print the result and its type.

**Sample Output:**  
```

13.5
\<class 'float'>

```

---

## ✅ Level: Intermediate (Q6–Q12)

---

### Q6. User Input & Type Conversion  
**Description:**  
Take 3 user inputs:  
- A float string  
- An int string  
- A boolean string (`"True"` or `"False"`)

Multiply the float and int, add the boolean value as `1` or `0`, and print the total.

**Input Format:**  
```

2.5
4
True

```

**Sample Output:**  
```

11.0

```

---

### Q7. Convert Boolean String  
**Description:**  
Assign `"False"` to a variable, convert it to a boolean, then to an integer. Print the result.

**Sample Output:**  
```

1

```

---

### Q8. Multiply String Numbers  
**Description:**  
You are given `"2.5"` and `"4"` as strings. Convert them to appropriate types and multiply.

**Sample Output:**  
```

10.0

```

---

### Q9. Concatenate All Types  
**Description:**  
Concatenate an int `5`, float `3.2`, and string `"Hello"` into a final string.

**Sample Output:**  
```

5 3.2 Hello

```

---

### Q10. Division & Type  
**Description:**  
Take input strings `"10"` and `"2.5"`, convert to number types, divide, and print result and type.

**Sample Output:**  
```

4.0
\<class 'float'>

````

---

### Q11. Boolean and Operator  
**Description:**  
Evaluate this expression and print its result and type:  
```python
(5.0 > 2) and bool("False")
````

---

### Q12. Nested Type Conversion

**Description:**
What is the result of this expression?

```python
int(float("5.9")) + int(True)
```

**Sample Output:**

```
6
```

---

## ✅ Level: Advanced (Q13–Q20)

---

### Q13. Multi Conversion & Math

**Description:**
Take 3 inputs:

* String like int: `"3"`
* String like float: `"2.5"`
* String like boolean: `"True"`

Convert and calculate:

```python
result = float_input * int_input + int(boolean_input)
```

**Sample Output:**

```
8.5
```

---

### Q14. Bool of String "False"

**Description:**
Evaluate:

```python
x = bool("False")  
print(int(x))
```

**Output:**

```
1
```

---

### Q15. String Multiplication & Conversion

**Description:**
Evaluate the following:

```python
result = ("5" * 2) + str(10.0)
```

**Sample Output:**

```
5510.0
```

---

### Q16. Complex Expression

**Description:**
Evaluate the following with proper conversions:

```python
a = "10"
b = "3.5"
c = "False"
result = int(a) + float(b) + int(c == "True")
```

**Output:**

```
13.5
```

---

### Q17. No Conditions Bool Check

**Description:**
Take user input `"True"` or `"False"`, and convert to 1 or 0 using `==`.

**Sample Input:**

```
True
```

**Output:**

```
1
```

---

### Q18. Empty String to Bool

**Description:**
What does this print?

```python
x = bool("")
y = int(x)
print(y)
```

**Output:**

```
0
```

---

### Q19. Float × 10 − Bool

**Description:**
Input:

* `"3.3"`
* `"False"`

Multiply float by 10, subtract boolean value as int.

**Output:**

```
33.0
```

---

### Q20. All Types in One

**Description:**
Take:

* `"10.5"` as float
* `"5"` as int
* `"True"` as boolean

Calculate:

```python
float + int + bool
```

**Sample Output:**

```
16.5
```

---

🧠 Want Solutions, Explanations, Test Scripts, or PDF Export? Just ask!

```

