'''🧠 Problem: Type Twister
Difficulty: 🟥 Very Hard (for your current level)
Topics: int, float, str, bool, input(), operators, variables

📜 Problem Statement:
You are given three inputs by the user, each on a separate line:

A number (could be a float or int) as a string

A boolean value (True or False) as a string

A number (as a float, not string)

🎯 Your goal:
You must perform the following transformations and calculations:

Convert the first input from string to float.

Convert the second input from string to real boolean (True or False).

Multiply the first input (as float) with the third input.

Convert the result to an int and assign it to final_number.

Convert the boolean (step 2) to an int (True → 1, False → 0), and assign it to bool_as_int.

Add final_number + bool_as_int and print the result.

You must also print the data types of every variable involved (so we can check your types).

📥 Input Format:
Each input is provided by the user on a new line:

arduino
Copy
Edit
"5.5"
"True"
3.0
📤 Output Format:
You must print exactly the following, one per line:

kotlin
Copy
Edit
<class 'float'>
<class 'bool'>
<class 'float'>
<class 'int'>
<class 'int'>
<class 'int'>
final_result
Where final_result is the sum of the converted number and the boolean as integer.

🧪 Sample Input:
arduino
Copy
Edit
"5.5"
"True"
3.0
✅ Sample Output:
kotlin
Copy
Edit
<class 'float'>
<class 'bool'>
<class 'float'>
<class 'int'>
<class 'int'>
<class 'int'>
17
🔍 Explanation:
First input "5.5" → float(5.5)

Second input "True" → bool(True)

Third input is already 3.0 → float

Multiply: 5.5 * 3.0 = 16.5

Convert to int → 16

"True" → True → int(True) → 1

16 + 1 = 17

🚫 Rules:

❌ No if, for, while, or function definitions

✅ You must use only: input(), int(), float(), str(), bool(), arithmetic and logical operators, and print()'''

# Input from the user
input_1=input("Enter first input : ")
input_2=input("Enter second input : ")
input_3=input("Enter third input : ")
# Convert inputs to appropriate types
a=float(input_1)
b=input_2=='True'
c=float(input_3)

# Perform calculations
sum_of_all=a*c
final_number=int(sum_of_all)

# Convert boolean to int
bool_as_int=int(b)

# Calculate final result
total=final_number+bool_as_int

# Print the types and final result
print(type(input_1))
print(type(input_2))
print(type(input_3))
print(type(a))
print(type(b))
print(type(c))
print(type(sum_of_all))
print(type(final_number))
print(type(bool_as_int))
print(type(total))

print(int(total))