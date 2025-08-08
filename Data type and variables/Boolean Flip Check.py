'''Check
📜 Problem Statement:
User inputs 3 values:

An integer string (e.g., "8")

A boolean string ("True" or "False")

Another integer string (e.g., "4")

🎯 Your Tasks:
Convert all strings into their correct types

Convert the boolean into a number (True → 1, False → 0)

Do this logic:

scss
Copy
Edit
not ((first_int + third_int) > 10 and bool_input)
Convert the result into an int

Print that value

Sample Input:
arduino
Copy
Edit
"8"
"True"
"4"
Explanation:
8 + 4 = 12 → greater than 10 and boolean is True → full expression is True
But not True = False → Output: 0

'''
# Input
integer_string_input=input("A integer string : ")
bool_string_input=input("A boolean string : ")
integer_string_input_1=input("A integer string : ")

# Conversion
conversion_int=int(integer_string_input)
conversion_int_1=int(integer_string_input_1)
conversion_bool=bool_string_input=='True'

# Logic
result=not ((conversion_int + conversion_int_1) > 10 and conversion_bool)

# Convert result to int and print
print(int(result))