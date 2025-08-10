#Problem 1 – Movie Ticket Booking
# 📂 Filename: movie_ticket_booking.py

# Problem Statement:
# A cinema hall has 3 types of seats:

# VIP seats → ("A1", "A2", "A3")

# Premium seats → ("B1", "B2", "B3")

# Regular seats → ("C1", "C2", "C3")

# Rules:

# VIP seats are only available for customers aged 21 and above.

# Premium seats are available for customers aged 18 and above.

# Regular seats are available for any age.

# If the seat number entered does not exist in the system, booking should be denied.


vip= ("A1", "A2", "A3")
premium=("B1", "B2", "B3")
regular=("C1", "C2", "C3")

name=input("Enter your name : ")
age=int(input("Enter your age : "))
seat_number=input("Enter your seat number : ")

if age>=21:
    if seat_number in vip:
        print("Booking Confirmed")
    else:
        print("Booking Denied – Age restriction")
elif age>=18:
    if seat_number in premium:
        print("Booking Confirmed")
    else:
        print("Booking Denied – Age restriction")
elif seat_number in regular:
    print("Booking Confirmed")
else:
    print("Booking Denied")

