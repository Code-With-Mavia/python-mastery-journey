'''📜 Problem Statement:
You are given three inputs from the user:

A float string (e.g., "9.9")

Another float string (e.g., "1.1")

A boolean string ("True" or "False")


🎯 Your Tasks:
Convert both strings to float

Convert the boolean string to a real bool

Multiply the two float numbers

Add the result to the boolean as int (True → 1, False → 0)

Check:

(result > 10.0 and bool_input) or (result == 10.89)
Print the final True/False result as an int

🔍 Sample Input:
arduino
Copy
Edit
"9.9"
"1.1"
"True"
Output:

Copy
Edit
1
(Why? 9.9 × 1.1 = 10.89, which matches result == 10.89, so it returns True → 1)'''

# Input from the user
float_string_input=input("A float string : ")
float_string_input_1=input("A float string : ")
bool_string_input=input("A boolean string : ")

# Conversion of inputs
conversion_float=float(float_string_input)
conversion_float_1=float(float_string_input_1)
conversion_bool=bool_string_input=='True'

# Calculation
product=conversion_float*conversion_float_1
result=product+int(conversion_bool) 

# Final output
print(result)
