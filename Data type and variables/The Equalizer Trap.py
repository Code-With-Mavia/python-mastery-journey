'''📜 Problem Statement:
You're given 3 inputs:

A number as a string that looks like a float (e.g., "7.0")

A number as a string that looks like an int (e.g., "7")

A boolean string "True" or "False"

🎯 Your Tasks:
Convert all inputs to correct types

Check whether the float and int are equal

Then apply this logic:
(float == int and bool_input) or (float != int and not bool_input)
Convert the final result to int and print

Sample Input:
"7.0"
"7"
"True"

Output:
1
(Why? 7.0 == 7 is True, and bool is True → result = True → output = 1)

'''

# Input strings
float_string_input=input("A float string : ")
input_string_input_1=input("A input string : ")
bool_string_input=input("A boolean string : ")

# Convert inputs to appropriate types
conversion_float=float(float_string_input)
conversion_int=int(input_string_input_1)
bool_conversion=bool_string_input=='True'

# Check equality and apply the logic
result=(conversion_float == conversion_int and bool_conversion) or (conversion_float != conversion_int and not bool_conversion)

# Convert the final result to int and print
print(int(result))
