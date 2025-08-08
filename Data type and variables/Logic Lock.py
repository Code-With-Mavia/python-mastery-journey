'''🧠 Problem: Logic Lock
Difficulty: 🔴 Very Hard
Concepts Covered: Data types, logical operators, input parsing, type conversion, boolean arithmetic

📜 Problem Statement:
You are building a logical lock system. The user provides three inputs:

A number that looks like an int, e.g., "12" (as a string)

A number that looks like a float, e.g., "4.5" (as a string)

A boolean string, either "True" or "False"

🎯 Your task:
Convert the first input to an int.

Convert the second input to a float.

Convert the third input to a bool (by checking if it equals "True").

Then, apply the following logic to unlock the system:

Calculate lock_code as:

scss
Copy
Edit
(int_input > 10 and bool_input) or (float_input < 5.0)
Convert lock_code (a boolean) into an integer (where True → 1, False → 0).

Print:

The data types of all variables

The final value of lock_code (as a boolean and also as an integer)

🧪 Sample Input:
arduino
Copy
Edit
"12"
"4.5"
"True"
✅ Sample Output:
python
Copy
Edit
<class 'str'>
<class 'str'>
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
<class 'bool'>
<class 'int'>
True
1
🔍 Explanation:
int_input = 12

float_input = 4.5

bool_input = True

Logic:

python
Copy
Edit
(12 > 10 and True) or (4.5 < 5.0)
→ True and True → True
→ True or True → True
Final lock_code = True, and int(lock_code) = 1

⚠️ Rules Recap:
Use only input(), casting (int(), float(), str()), bool, variables, logic operators.

❌ No if, for, while, def, etc.

✅ Must print all types and final result

'''
# Input from the user
int_input=input("A number that looks like an int : ")
float_input=input("A number that looks like a float : ")
bool_input=input("A boolean string : ")

# Convert inputs to appropriate types
convrsion_int_input=int(int_input)
convrsion_float_input=float(float_input)
convrsion_bool_input = bool_input == "True"
# Calculate lock_code based on the logic provided
lock_code=bool((convrsion_int_input > 10 and convrsion_bool_input) or (convrsion_float_input < 5.0))
Final_lock_code = int(lock_code)

# Print the types and final result
print(type(int_input))
print(type(float_input))
print(type(bool_input))
print(type(convrsion_int_input))
print(type(convrsion_float_input))
print(type(convrsion_bool_input))
print(type(lock_code))
print(type(Final_lock_code))

print(Final_lock_code)