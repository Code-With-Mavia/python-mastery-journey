# 🟣 Question 1 – Remove Extra Spaces
# Input: " Hello World "
# Task: Remove spaces from the beginning and end.
# Expected Output: "Hello World"

# 🟣 Question 2 – Convert to Uppercase
# Input: "python is fun"
# Task: Convert all letters to uppercase.
# Expected Output: "PYTHON IS FUN"

# 🟣 Question 3 – Replace a Word
# Input: "I like java"
# Task: Replace "java" with "Python"
# Expected Output: "I like Python"

# 🟣 Question 4 – First 3 Letters
# Input: "Elephant"
# Task: Show only the first 3 letters using slicing.
# Expected Output: "Ele"

# 🟣 Question 5 – Last 2 Letters
# Input: "Notebook"
# Task: Show only the last 2 letters using slicing.
# Expected Output: "ok"

# 🟣 Question 6 – Count Words
# Input: "The sky is blue"
# Task: Count the number of words.
# Expected Output: 4
# (Hint: use .split() and len())


s=" Hello World "
s=s.strip()
print(s)

a="python is fun"
print(a.upper())

b="I like java"
print(b.replace("java","Python"))

c="Elephant"
print(c[:3])

d="Notebook"
print(d[6:])

e="The sky is blue"
print(len(e.split()))