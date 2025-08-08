'''🧠 TOUGHEST CONDITIONAL STATEMENTS CHALLENGE
🔐 Multi-Condition Access Control System
You're building a smart access system for a secure building. A user must provide the following inputs:

username (string)

role (can be: "admin", "employee", or "guest")

access_code (4-digit number)

floor_requested (integer)

🛑 Access Rules:
If role is "admin":

Grant access to any floor if access_code ends in an even number.

If role is "employee":

Only allow access to floors 2 to 5 (inclusive) if access code is divisible by 5.

If role is "guest":

Only allow floor 1 access, and access_code must be exactly 1234.

If the role is not one of "admin", "employee", "guest":

Print "INVALID ROLE".

✅ Output:
Print:

"ACCESS GRANTED -> <username> to floor <floor_requested>"

or "ACCESS DENIED -> <reason>"

🔍 Example Inputs & Outputs:
Input:
yaml
Copy
Edit
username: Sarah
role: admin
access_code: 4862
floor_requested: 10
Output:
pgsql
Copy
Edit
ACCESS GRANTED -> Sarah to floor 10
Input:
yaml
Copy
Edit
username: Alex
role: guest
access_code: 1234
floor_requested: 1
Output:
pgsql
Copy
Edit
ACCESS GRANTED -> Alex to floor 1
Input:
yaml
Copy
Edit
username: John
role: employee
access_code: 1002
floor_requested: 4
Output:
pgsql
Copy
Edit
ACCESS DENIED -> Access code must be divisible by 5
'''


username = input("Enter your username: ")
role = input("Enter your role: ")
access_code = int(input("Enter your code: "))
floor_requested = int(input("Enter your floor: "))

if role == 'admin':
    if access_code % 2 == 0:
        print(f"ACCESS GRANTED -> {username} to floor {floor_requested}")
    else:
        print(f"ACCESS DENIED -> Access code must be even for admin")

elif role == 'employee':
    if access_code % 5 != 0:
        print(f"ACCESS DENIED -> Access code must be divisible by 5")
    elif not (2 <= floor_requested <= 5):
        print(f"ACCESS DENIED -> Floor must be between 2 and 5 for employee")
    else:
        print(f"ACCESS GRANTED -> {username} to floor {floor_requested}")

elif role == 'guest':
    if access_code != 1234:
        print(f"ACCESS DENIED -> Access code must be 1234 for guest")
    elif floor_requested != 1:
        print(f"ACCESS DENIED -> Guest can only access floor 1")
    else:
        print(f"ACCESS GRANTED -> {username} to floor {floor_requested}")

else:
    print("INVALID ROLE")
