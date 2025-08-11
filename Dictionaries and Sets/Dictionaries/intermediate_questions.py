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
