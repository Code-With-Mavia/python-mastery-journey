'''🧠 Problem: Weird Type Swap
Difficulty: Hard
Topics: int, str, float, variables only

🔒 Problem Statement:
You are given three lines of input:

A string that looks like an integer (e.g., "45").

A float (e.g., 3.14).

An integer (e.g., 10).

Your task is to reassign each of the three variables so that:

The first variable becomes the sum of the original float and original integer.

The second variable becomes the string version of the original integer.

The third variable becomes the float version of the original string (which looks like an int).

You must print all three variables in a single line separated by a single space in the following order:

nginx
Copy
Edit
new_var1 new_var2 new_var3
All type conversions must be done explicitly.

📥 Input Format:
Each input is given on a separate line:

nginx
Copy
Edit
string_int
float_val
int_val
📤 Output Format:
python
Copy
Edit
float str float
Print the converted and reassigned variables in the specified order.

🧪 Sample Input:
arduino
Copy
Edit
"45"
3.14
10
✅ Sample Output:
Copy
Edit
13.14 10 45.0
🔍 Explanation:
First variable: 3.14 + 10 = 13.14 → float

Second variable: 10 → "10" → string

Third variable: "45" → 45.0 → float

⚠️ Constraints:
Do not use any conditionals, functions, or loops.

You can only use:
int, str, float, variable assignment, and print.'''

#variables
var1='45'
var2=3.14
var3=10

#type casting
new_var1=var2+var3
new_var2=str(var3)
new_var3=float(var1)

#results 
print(type(new_var1))
print(type(new_var2))
print(type(new_var3))
print(new_var1, new_var2 ,new_var3)






