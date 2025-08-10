# Movie Ticket Pricing System
# You are building a simple movie ticket system.
# A ticket price depends on the day and the seat type.

# If the day is "Saturday" or "Sunday" → weekend prices apply.

# If the seat is "VIP" → weekend price is $20, weekday price is $15.

# If the seat is "Standard" → weekend price is $12, weekday price is $8.

# If the seat type is anything else → output "Invalid Seat Type".

# If the day is invalid (not Mon–Sun) → output "Invalid Day".

# Constraints:

# day and seat_type will be strings.

# You cannot use loops or imports. Only variables, lists, and if-else.


day=input("Enter the day : ")
seat_type=input("Enter the seat type want VIP/Standard : ")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]

if day in weekend_days:
    if seat_type == 'VIP':
        print(f"Price: $20 for {seat_type}")
    elif seat_type == 'Standard':
        print(f"Price: $12 for {seat_type}")
    else:
        print(f"Invalid Seat Type {seat_type}")
elif day in days:
    if seat_type == 'VIP':
        print(f"Price: $15 for {seat_type}")
    elif seat_type == 'Standard':
        print(f"Price: $8 for {seat_type}")
    else:
        print(f"Invalid Seat Type {seat_type}")
else:
    print("Invalid Day")