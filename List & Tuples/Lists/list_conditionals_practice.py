###################################### 🟣 Problem 1 — VIP Event Check#####################################
# Description
# You are organizing an exclusive event. Only certain people are allowed entry. You have a list of invited guests.
# A person will only be allowed in if:

# Their name is in the guest list AND

# Their name starts with an uppercase letter.
#input and outputs 
# guests = ["Alice", "Bob", "Charlie"]
# visitor = "Alice"

guests = ["Alice", "Bob", "Charlie"]
visitor=input("Enter your name : ")

if visitor in guests and visitor[0].upper():
    print(f"Access granted {visitor}")
else:
    print(f"Access denied {visitor}")
    
    
    
    
#####################################🟣 Problem 2 — Grocery Item Availability#####################################
# Description
# You have a grocery store inventory stored as a list of items. A customer asks if a particular item is available.
# You must check:

# The item must be in the inventory list.

# The item name must be at least 3 characters long.

# Input
# A list of items in stock:


# inventory = ["milk", "bread", "eggs", "cheese"]
# A string representing the item the customer wants. Example:
# milk
# Output
# "Available" if the item meets both conditions.

# "Not available" otherwise.

# Example 1
# Input:

# inventory = ["milk", "bread", "eggs", "cheese"]
# item = "bread"
# Output:
# Available

# Example 2
# Input:


# inventory = ["milk", "bread", "eggs", "cheese"]
# item = "hi"
# Output:

# Not available

    
inventory = ["milk", "bread", "eggs", "cheese"]
item=input("Enter the item you want : ")

if item in inventory and len(item)!=3:
    print(f"{item} is Available")
else:
    print(f"{item} is not available")



#####################################Problem 3 — VIP Event #####################################
# Description
# A VIP event has a guest list stored as a list of names.
# To allow entry:

# The guest’s name must be on the guest list.

# The guest must have a valid pass type — either "gold" or "platinum". 

guest_list = ["Alice", "Bob", "Charlie"]
valid_pass=['gold','platinum']
visitor=input("Enter your name : ")
pass_type=input("Enter your pass for access : ")

if visitor not in guest_list and visitor[0].upper() :
    print(f"Entry Denied to {visitor}")

elif pass_type not in valid_pass:
        print(f"Entry Denied to {visitor} due to wrong pass which is {pass_type}")
else: 
    print(f"Entry Granted to {visitor}")


######################################Problem 4 — Shopping Cart Discount#####################################
# Description
# A store is giving discounts based on the number of items in a customer's shopping cart.

# If the cart contains "Laptop" and the number of items in the cart is more than 3 → "20% Discount".

# If the cart contains "Phone" and the number of items is at least 2 → "10% Discount".

# Otherwise → "No Discount".

items = input("Enter items separated by whitesapces: ").split()
print(items)
if 'Laptop' in items and len(items)>3:
    print("20% Discount")
elif 'Phone' in items and len(items)>=2:
    print("10% Discount")
else:
    print("No Discount")
    
    
