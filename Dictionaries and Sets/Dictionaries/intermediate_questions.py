# Inventory Restock Checker

# **Problem:**
# You manage a small store inventory represented by a dictionary, where keys are product names (strings) and values are quantities (integers).

# You receive a restock request as another dictionary with product names and quantities to add.

# Write a program that:

# * Takes two dictionaries: `inventory` and `restock`.
# * For each product in `restock`, check if it exists in `inventory`.

#   * If yes, add the restock quantity to the inventory quantity.
#   * If no, add the product to the inventory with the restock quantity.
# * Print the updated inventory dictionary.

# ---

# **Constraints:**

# * No loops or functions allowed.
# * Use only dictionary operations, variables, conditionals.

# ---

# **Example:**

# ```python
# inventory = {"apple": 10, "banana": 5}
# restock = {"banana": 3, "orange": 7}
# ```

# Expected updated inventory:

# ```python
# {"apple": 10, "banana": 8, "orange": 7}
# ```
inventory = {"apple": 10, "banana": 5}
restock = {"banana": 3, "orange": 7}

# Check 'banana'
if "banana" in inventory:
    inventory["banana"] = inventory["banana"] + restock["banana"]
else:
    inventory["banana"] = restock["banana"]

# Check 'orange'
if "orange" in inventory:
    inventory["orange"] = inventory["orange"] + restock["orange"]
else:
    inventory["orange"] = restock["orange"]
    
print(inventory)
# ---



### Dictionary Key Permission Checker

# **Problem:**
# You have a dictionary that defines permissions for users, e.g.:

# ```python
# permissions = {
#     "Alice": "read",
#     "Bob": "write",
#     "Charlie": "admin"
# }
# ```

# Write a program that:

# * Takes a username as input.
# * Checks if the user exists in the permissions dictionary.
# * If the user exists, print:
#   `"User <username> has <permission> permission."`
# * If the user does not exist, print:
#   `"User <username> not found."`

# ---

# **Constraints:**

# * Use only variables, data types, dictionary operations, and conditionals.
# * No loops or functions.

# ---

permissions = {
    "Alice": "read",
    "Bob": "write",
    "Charlie": "admin"
}

username=input("Enter your username : ")
if username in permissions:
    print(f"User {username} has {permissions[username]} permission.")
else:
    print(f"User {username} not found.")


### Question: Product Price Checker

# You have a dictionary of products with their prices:

# ```python
# prices = {
#     "apple": 120,
#     "banana": 40,
#     "orange": 60,
#     "mango": 150
# }
# ```

# Write a program that:

# * Takes a product name as input.
# * Checks if the product exists in the dictionary.
# * If it exists, print:
#   `"Price of <product> is <price>."`
# * If it does not exist, print:
#   `"Product <product> not found."`

prices = {
    "apple": 120,
    "banana": 40,
    "orange": 60,
    "mango": 150
}
product=input("Enter the product you want : ")

if product in prices:
    print(f"Price of {product} is {prices[product]}.")
else:
    print(f"Product {product} not found.")


### Question: Membership Level Checker

# You have this dictionary of users and their membership levels:

# ```python
# memberships = {
#     "John": "Gold",
#     "Sara": "Silver",
#     "Mike": "Bronze"
# }
# ```

# Write a program that:

# * Takes a username as input.
# * If the username exists and the membership level is `"Gold"`, print:
#   `"Welcome, <username>! You have full access."`
# * If the username exists but membership is **not** `"Gold"`, print:
#   `"Hello, <username>. Upgrade to Gold for full access."`
# * If the username does **not** exist, print:
#   `"User <username> not found."`


memberships = {
    "John": "Gold",
    "Sara": "Silver",
    "Mike": "Bronze"
}
username=input("enter your username : ")
if username in memberships:
    if memberships[username] == "Gold":
        print(f"Welcome, {username}! You have full access.")
    else:
        print(f"Hello, {username}. Upgrade to Gold for full access.")
else:
    print(f"User {username} not found.")


### Question: Employee Salary Checker

# You have a dictionary of employee names and their salaries:

# ```python
# salaries = {
#     "Alice": 50000,
#     "Bob": 60000,
#     "Charlie": 55000
# }
# ```

# Write a program that:

# * Takes an employee name as input.
# * Checks if the employee exists.
# * If the employee exists and salary is greater than or equal to 60000, print:
#   `"Employee <name> is eligible for a bonus."`
# * If the employee exists but salary is less than 60000, print:
#   `"Employee <name> is not eligible for a bonus."`
# * If the employee does not exist, print:
#   `"Employee <name> not found."`

salaries = {
    "Alice": 50000,
    "Bob": 60000,
    "Charlie": 55000
}

employee=input("Enter your name : ")

if employee in salaries and salaries[employee]>=60000:
    print(f"Employee {employee}is eligible for a bonus.")
elif employee in salaries and salaries[employee]<60000:
    print(f"Employee {employee} is not eligible for a bonus.")
else:
    print(f"Employee {employee} not found.")


### Question: Library Book Availability

# You have a dictionary representing books and their availability status:

# ```python
# library = {
#     "Python Basics": True,
#     "Data Science": False,
#     "Machine Learning": True,
#     "AI Fundamentals": False
# }
# ```

# Write a program that:

# * Takes a book title as input.
# * Checks if the book is in the library dictionary.
# * If the book exists and is available (`True`), print:
#   `"The book '<book_title>' is available."`
# * If the book exists but is not available (`False`), print:
#   `"The book '<book_title>' is currently checked out."`
# * If the book does not exist, print:
#   `"The book '<book_title>' does not exist in the library."`

library = {
    "Python Basics": True,
    "Data Science": False,
    "Machine Learning": True,
    "AI Fundamentals": False
}
book_title=input("Enter the book you want : ").title()
if book_title in library and library[book_title]==True:
    print(f"The book {book_title} is available.")
elif book_title in library and library[book_title]==False:
    print(f"The book {book_title} is currently checked out.")
else:
    print(f"The book {book_title} does not exist in the library.")


#Nested Dictionaires

### Question: Company Employee Role Checker (Nested Dictionary)

# You have a nested dictionary representing departments and their employees with roles:

# ```python
# company = {
#     "HR": {
#         "Alice": "Manager",
#         "Bob": "Recruiter"
#     },
#     "IT": {
#         "Charlie": "Developer",
#         "David": "SysAdmin"
#     },
#     "Sales": {
#         "Eva": "Salesperson"
#     }
# }
# ```

# Write a program that:

# * Takes two inputs from the user:

#   1. Department name (e.g., `"HR"`)
#   2. Employee name (e.g., `"Alice"`)

# * Checks if the department exists in the dictionary.

# * If the department exists, check if the employee exists in that department.

# * If both exist, print:
#   `"<Employee> works as <Role> in <Department> department."`

# * If the department does not exist, print:
#   `"Department <Department> not found."`

# * If the employee does not exist in that department, print:
#   `"Employee <Employee> not found in <Department>."`

# ---

# **Note:** Since you know only conditionals and basic data types, you can access nested dictionaries using keys without loops.

company = {
    "HR": {
        "Alice": "Manager",
        "Bob": "Recruiter"
    },
    "IT": {
        "Charlie": "Developer",
        "David": "SysAdmin"
    },
    "Sales": {
        "Eva": "Salesperson"
    }
}

department_name=input("Enter your depatment : ").strip().upper()
employee_name=input("Enter your name : ").title()

if department_name in company:
    if employee_name in company[department_name]:
        print(f"{employee_name} works as {company[department_name][employee_name]} in {department_name} department.")
    else:
        print(f"Department {department_name} not found.")
elif employee_name not in company[department_name]:
    print(f"Employee {employee_name} not found in {department_name}.")
else:
    print("Wrong entry")
        


### Question: Hotel Room Booking System

# You have a nested dictionary representing floors and rooms booked by guests:

# ```python
# hotel = {
#     "Floor1": {
#         "101": "Alice",
#         "102": "Bob"
#     },
#     "Floor2": {
#         "201": "Charlie",
#         "202": "David"
#     }
# }

# Write a program that:

# * Takes three inputs from the user:

#   1. Floor name (e.g., `"Floor1"`)
#   2. Room number (e.g., `"101"`)
#   3. Guest name (e.g., `"Alice"`)

# * Checks if the floor exists.

# * If the floor exists, check if the room exists on that floor.

# * If the room exists, check if the guest name matches the booking.

# * Print:

#   * `"Booking confirmed for <guest> in room <room> on <floor>."` if all matches.
#   * `"Room <room> on <floor> is booked by someone else."` if the room is booked but the guest name does not match.
#   * `"Room <room> not found on <floor>."` if the room doesn’t exist on that floor.
#   * `"Floor <floor> not found."` if the floor doesn’t exist.

# ---


hotel = {
    "Floor1": {
        "101": "Alice",
        "102": "Bob"
    },
    "Floor2": {
        "201": "Charlie",
        "202": "David"
    }
}



floor_name=input("Enter your desired floor : ").title()
room_number=input(" enter your desired room number : ")
name=input("enter your name : ").title()

if floor_name in hotel:
    if room_number in hotel[floor_name]:
        if name in hotel[floor_name][room_number]:
            print(f"Booking confirmed for {name} in room {room_number} on {floor_name}.")

        else:
            print(f"Room {room_number} on {floor_name} is booked by someone else.")
    else:
        print(f"Room <{room_number} not found on {floor_name}.")
else:
    print(f"Floor {floor_name} not found.")

## **Question 1 – Nested Dictionary Lookup**

# **Problem:**
# You have the following nested dictionary:

# ```python
# company = {
#     "IT": {"Alice": "Developer", "Bob": "SysAdmin"},
#     "HR": {"Charlie": "Recruiter"}
# }
# ```

# **Task:**
# Ask the user to enter a **department** and an **employee name**.
# If that employee exists in that department, print their **role**. Otherwise, print `"Employee not found in department"`.

company = {
    "IT": {"Alice": "Developer", "Bob": "SysAdmin"},
    "HR": {"Charlie": "Recruiter"}
}
department=input("Enter your department : ").upper()
employee=input("Enter your name : ").title()
if department in company:
    if employee in company[department]:
        print(f" Role of {employee} is {company[department][employee]}")
    else:
        print("Employee not found in department")
else:
    print(f"Department {department} not found")
# ---

# ## **Question 2 – Nested Booking Check**

# **Problem:**

# ```python
# hotel = {
#     "Floor1": {"Room101": "Alice", "Room102": "Bob"},
#     "Floor2": {"Room201": "Charlie"}
# }
# ```

# **Task:**
# Ask the user for a **floor name** and a **room number**.
# If the room exists, print the guest's name. Otherwise, print `"Room not found"`.
hotel = {
    "Floor1": {"Room101": "Alice", "Room102": "Bob"},
    "Floor2": {"Room201": "Charlie"}
}
floor=input("Enter your floor : ").title()
room=input("Enter your room number : ").title()

if floor in hotel:
    if room in hotel[floor]:
        print(f"Room is {room} for {hotel[floor][room]}")
    else:
        print("Room not found")
else:
    print("Floor not found")
# ---

# ## **Question 3 – Modify Nested Dictionary**

# **Problem:**

# ```python
# university = {
#     "Science": {"John": "Physics", "Mary": "Chemistry"},
#     "Arts": {"Tom": "History"}
# }
# ```

# **Task:**
# Ask for a **faculty name**, **student name**, and **new subject**.
# If that student exists in that faculty, update their subject to the new one and print the updated faculty data.
# If not found, print `"Student not found"`.
university = {
    "Science": {"John": "Physics", "Mary": "Chemistry"},
    "Arts": {"Tom": "History"}
}

faculty = input().title()
student = input().title()
new_subject = input().title()

if faculty in university:
    if student in university[faculty]:
        university[faculty][student] = new_subject
        print(university[faculty][student])
        print(university[faculty])
    else:
        print("Student not found")
else:
    print("Faculty not found")

# ---

# ## **Question 4 – Nested Key Existence**

# **Problem:**

# ```python
# library = {
#     "Fiction": {"Book1": "Available", "Book2": "Issued"},
#     "NonFiction": {"Book3": "Available"}
# }
# ```

# **Task:**
# Ask for a **category** and **book name**.
# If the book exists, print its status. Otherwise, print `"Book not found in category"`.
library = {
    "Fiction": {"Book1": "Available", "Book2": "Issued"},
    "NonFiction": {"Book3": "Available"}
}
category=input().title()
book=input().title()
if category in library:
    if book in library[category]:
        print(library[category][book])
    else:
        print("Book not found in category")
else:
    print("Category not found")
# ---

# ## **Question 5 – Add to Nested Dictionary**

# **Problem:**

# ```python
# store = {
#     "Electronics": {"Laptop": 10, "Phone": 5},
#     "Groceries": {"Apple": 20}
# }
# ```

# **Task:**
# Ask for a **category**, **item name**, and **quantity**.
# If the category exists, add the item to that category with the given quantity.
# If not, print `"Category not found"`.
store = {
    "Electronics": {"Laptop": 10, "Phone": 5},
    "Groceries": {"Apple": 20}
}
category=input().title()
name=input().title()
quantity=int(input())

if category in store:
    if name in store[category]:
        store[category][name]+=quantity
        print(store[category])
    else:
        print(f"{name} not found ")
else:
    print("Category not found")


#store following words in a python dicitonary
a={
    'table': ['a piece of furniture','lists of facts and figures'],
    'cat': 'a small animal',
   }
print(a)
#given list. assume one classroom is required for 1 subject. how many classrooms needed by all students
b={'python','java','c++','python','js','java','python','java','c++','c'}
print(len(b))

#enter marks of 3 subjects from useer and store them in a dicitornat. 
# start with an empty dicitonary and add one by one . use subject name as key and marks as value 

subject=input("Enter your subject :")
marks=int(input("Enter your marks : "))
subject1=input("Enter your subject :")
marks1=int(input("Enter your marks : "))
subject2=input("Enter your subject :")
marks2=int(input("Enter your marks : "))
course={}
course.update({subject:marks})
course.update({subject1:marks1})
course.update({subject2:marks2})

print(type(course))
print(course)

#figure out a way how to store 9 and 9.0 as a seprate values in the set 
#you can take help of built-in datatypes

a=set()
a={('float', 9.0),('int', 9)}
print(type(a))
print(a)

# 1. Nested Conditional Dictionary Lookup
# You have the dictionary:


# students = {
#     "Ali": {"marks": 85, "grade": "A"},
#     "Sara": {"marks": 72, "grade": "B"},
#     "Omar": {"marks": 50, "grade": "C"}
# }
# Question:
# Write a program that takes a student's name as input.

# If the student exists,

# If marks ≥ 80 → print "Excellent"

# If marks between 60–79 → print "Good"

# Else → print "Needs Improvement"

# If the student doesn’t exist → print "Student not found"

students = {
    "Ali": {"marks": 85, "grade": "A"},
    "Sara": {"marks": 72, "grade": "B"},
    "Omar": {"marks": 50, "grade": "C"}
}

name=input("Enter your name : ").title()
if name in students:
    marks=students[name]['marks']
    if marks>=80 :
        print("Excellent")
    elif 70<=marks>=60:
        print("Good")
    else:
        print("Needs Improvement")
else:
    print("Student not found")
    
# 2. Type & Key Existence Check
# You have:


# data = {
#     "user_id": 101,
#     "is_active": True,
#     "role": "admin"
# }
# Question:
# Take a key name as input.

# If the key exists in data:

# If its value is str, print "This is text data"

# If its value is int, print "This is a number"

# If its value is bool, print "This is a boolean"

# Else → print "Invalid key"

user = {
    "name": "Ali",      # string
    "age": 25,          # integer
    "active": True,     # boolean
    "role": "Admin"     # string
}


key=input("Enter your key : ")
if key in user:
    value = user[key]
    if type(value)==str:
        print("This is text data")
    elif type(value)==int:
        print("This is a number")
    elif type(value)==bool:
        print("This is a boolean")
else:
    print("Invalid key")
    


# 3. Nested Keys with Conditional Access
# Problem:
# Check if the user’s plan matches and see if renewal is needed.

# Input Format:

# First line: Plan type (string)

# Constraints:
# user_plan = {
#     "plan": "premium",
#     "expiry_days": 3
# }
# Plan type is case-sensitive.

# Output Format:

# "Renew soon!" if matching type and expiry_days ≤ 5

# "Your plan is active" if matching and expiry_days > 5

# "Plan mismatch" otherwise

# Sample Input:


# premium
# Sample Output:

# Renew soon!

user_plan = {
    "plan": "premium",
    "expiry_days": 3
}

plan_type = input()

if plan_type == user_plan["plan"]:
    if user_plan["expiry_days"] <= 5:
        print("Renew soon!")
    else:
        print("Your plan is active")
else:
    print("Plan mismatch")

# 4. Multi-Dictionary Condition
# Problem:
# Given two users' info, take a username as input.

# If name matches user1 and online is True → "User1 is active"

# Else if name matches user2 and online is True → "User2 is active"

# Else → "User is either offline or does not exist"

# Given Dictionary:

# users = {
#     "user1": {"name": "Ali", "online": True},
#     "user2": {"name": "Sara", "online": False}
# }
# Sample Input:
# Ali
# Sample Output:
# User1 is active

users = {
    "user1": {"name": "Ali", "online": True},
    "user2": {"name": "Sara", "online": False}
}

username=input().title()

if username == users["user1"]["name"] and users["user1"]["online"] == True:
    print("User1 is active")
elif username == users["user2"]["name"] and users["user2"]["online"] == True:
    print("User2 is active")
else:
    print("User is either offline or does not exist")

# 5. Conditional Merge Without Loops
# Problem:
# Take "yes" or "no" as input.

# If yes → print combined dictionary of dict1 and dict2

# If no → print dict1

# Given:
# dict1 = {"name": "Ali", "city": "Lahore"}
# dict2 = {"age": 25, "job": "Engineer"}
# Sample Input:
# yes
# Sample Output:
# {'name': 'Ali', 'city': 'Lahore', 'age': 25, 'job': 'Engineer'}

dict1 = {"name": "Ali", "city": "Lahore"}
dict2 = {"age": 25, "job": "Engineer"}

info=input("Yes/No: ").title()

if info=='Yes':
    #these are 3 methods 
    #dict1.update(dict2)
    #info={**dict1,**dict2}
    info=dict1 | dict2
    print(info)
else:
    print(dict1)

# 6. Deep Nested Value Check
# Problem:
# If phone is None → "No phone number" else → "Phone available"

# Given:
# contact = {
#     "email": "ali@example.com",
#     "phone": None
# }
# Sample Output:
# No phone number

contact = {
    "email": "ali@example.com",
    "phone": None
}
if contact["phone"]==None:
    print("No phone number")
else:
    print("Phone available")

# 7. Value Comparison Between Two Dictionaries
# Problem:
# Compare price of order1 and order2.

# If equal → "Same price"

# If order1 > order2 → "Order1 is expensive"

# Else → "Order2 is expensive"

# Given:
# order1 = {"item": "Laptop", "price": 1000}
# order2 = {"item": "Laptop", "price": 950}
# Sample Output:
# Order1 is expensive

order1 = {"item": "Laptop", "price": 100}
order2 = {"item": "Laptop", "price": 100}

if order1["price"]==order2["price"]:
    print("Same price")
elif order1["price"] > order2["price"]:
    print("Order1 is expensive")
else:
    print("Order2 is expensive")

# 8. Multiple Type Validation
# Problem:
# Take a key as input.

# If not in dictionary → "Invalid key"

# If boolean → "Boolean value"

# If int → "Number value"

# If string → "Text value"

# Given:
# settings = {
#     "theme": "dark",
#     "notifications": True,
#     "max_users": 50
# }
# Sample Input:
# notifications

# Sample Output:
# Boolean value

settings = {
    "theme": "dark",
    "notifications": True,
    "max_users": 50
}
key=input()
value=settings[key]
if type(value)==str:
    print("Text value")
elif type(value)==bool:
    print("Boolean value")
elif type(value)==int:
    print("Number value")
else:
    print("Invalid key")


# 9. Nested Data Type Decision
# Problem:
# If debug is True → "Debug mode on"
# Else → "Debug mode off" and print server ip and port.

# Given:
# config = {
#     "server": {"ip": "192.168.1.1", "port": 8080},
#     "debug": False
# }
# Sample Output:
# Debug mode off
# 192.168.1.1 8080

config = {
    "server": {"ip": "192.168.1.1", "port": 8080},
    "debug": False
}

if config["debug"]==True:
    print("Debug mode on")
else:
    print(f"Debug mode off and your ip is {config['server']['ip']}  and port is {config['server']['port']}")

# 10. Dictionary Switch Based on Condition
# Problem:
# Take "vip" or "guest" as input.
# If vip → print vip dict.
# If guest → print guest dict.
# Else → "Invalid type"

# Given:
# vip = {"name": "Ali", "access": "full"}
# guest = {"name": "Sara", "access": "limited"}
# Sample Input:
# guest
# Sample Output:
# {'name': 'Sara', 'access': 'limited'}

vip = {"name": "Ali", "access": "full"}
guest = {"name": "Sara", "access": "limited"}

status=input()
if status=='vip':
    print(vip)
elif status=='guest':
    print(guest)
else:
    print("wrong entry")
    
    
# 11. Two-Level Nested Check
# Problem:
# If department location is "Building A" → "Same building" else "Different building"

# Given:
# employee = {
#     "id": 101,
#     "department": {"name": "IT", "location": "Building A"}
# }
# Sample Output:
# Same building

employee = {
    "id": 101,
    "department": {"name": "IT", "location": "Building A"}
}

if employee["department"]['location']=="Building A":
    print("Same building")
else:
    print("Different building")


# 12. Mixed Data Match
# Problem:
# Take product name as input.

# If not available → "Out of stock"

# If available → print "Price is X"

# Given:
# products = {
#     "Laptop": {"available": True, "price": 1200},
#     "Phone": {"available": True, "price": 500}
# }
# Sample Input:
# Laptop
# Sample Output:
# Price is 1200

products = {
    "Laptop": {"available": True, "price": 1200},
    "Phone": {"available": False, "price": 500}
}
product_name=input().title()
if product_name in products:
    if products[product_name]['available']==True:
        print(f"Price is {products[product_name]['price']}")
    else:
        print("Out of stock")
else:
    print("Product doesnt exist")


# 13. Conditional Overwrite
# Problem:
# If score ≥ 80 → change status to "approved" and print dict
# Else → "Not approved"

# Given:
# record = {"status": "pending", "score": 85}
# Sample Output:
# {'status': 'approved', 'score': 85}

record = {"status": "pending", "score": 85}

score=record["score"]
if score>=80:
    record["status"]='approved'
    print(record)
else:
    record["status"]='Not approved'
    print(record)

# 14. Compare Nested Key Values
# Problem:
# Compare math grades.

# If equal → "Same marks"

# If student1 > student2 → "Student1 scored higher"

# Else → "Student2 scored higher"

# Given:
# student1 = {"name": "Ali", "grades": {"math": 90}}
# student2 = {"name": "Sara", "grades": {"math": 85}}
# Sample Output:

# Student1 scored higher

# student1 = {"name": "Ali", "grades": {"math": 90}}
# student2 = {"name": "Sara", "grades": {"math": 115}}

# if student1["grades"]['math']==student2["grades"]['math']:
#     print("Same marks")
# elif student1["grades"]['math'] >= student2["grades"]['math']:
#     print("Student1 scored higher")
# else:
#    print("Student2 scored higher") 

# 15. Triple Condition Access
# Problem:
# If vehicle type is "Car" and year ≥ 2022 and is_new is True → "Latest model" else "Old model"

# Given:
# vehicle = {
#     "type": "Car",
#     "brand": "Toyota",
#     "year": 2022,
#     "is_new": True
# }
# Sample Output:
# Latest model

vehicle = {
    "type": "Car",
    "brand": "Toyota",
    "year": 2022,
    "is_new": True
}

if vehicle["type"]=='Car' and vehicle["year"]>=2022 and vehicle["is_new"]==True:
    print("Latest model")
else:
    print("Old model")
