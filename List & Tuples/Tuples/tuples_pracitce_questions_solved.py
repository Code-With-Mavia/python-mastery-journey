###################### 🟣 Question 1 – Preferred Travel Mode Checker ######################
# You are given a tuple of available travel modes for an employee
# Task:

# If the preferred mode is in the tuple, print:
# APPROVED: <mode>

# If it’s not in the tuple, print:
# NOT APPROVED

modes = ("car", "train", "bicycle")
preferred_mode=input("Enter your prefered mode : ")
if preferred_mode in modes:
    print(f"Approved {preferred_mode}")
else:
    print(f"Not Approved")
    
######################Question 2 – VIP Seat Access######################
# You are given a tuple of VIP seat numbers in a theatre:
# Input:
# An integer representing the seat number a customer booked.

# Task:
# If the booked seat is in vip_seats, print:
# VIP ACCESS GRANTED

# Otherwise, print:
# REGULAR ACCESS

vip_seats = (5, 10, 15, 20)
booked_seats=int(input("Enter the seat you wish to book : "))

if booked_seats in vip_seats:
    print("VIP ACCESS GRANTED")
else:
    print("REGULAR ACCESS")

#######################Question 3 – Airport Lounge Access######################
# You are given two tuples:
# first_class_passengers = ("Alice", "Bob", "Charlie")
# business_class_passengers = ("David", "Eva")

# Input:

# A passenger’s name.

# A string representing their ticket type: "First", "Business", or "Economy".

# Task:

# If their ticket type is "First" and their name is in first_class_passengers → print:
# Access to VIP Lounge

# If their ticket type is "Business" and their name is in business_class_passengers → print:
# Access to Business Lounge

# Otherwise → print:
# No Lounge Access

# Example 1:
# Input:
# Alice
# First

# Output:
# Access to VIP Lounge

# Example 2:
# Input:
# David
# First

# Output:
# No Lounge Access

# Example 3:
# Input:
# Eva
# Business

# Output:
# Access to Business Lounge

first_class_passengers = ("Alice", "Bob", "Charlie")
business_class_passengers = ("David", "Eva")

name=input("Enter your name : ")
ticket_type=input("Enter your ticket type : ")

if name in first_class_passengers and ticket_type=='First':
    print("Access to VIP Lounge")
elif name in business_class_passengers and ticket_type=='Business':
    print("Access to Business Lounge")
else:
    print("No Lounge Access")

#######################Question 4 – Conference Room Booking#######################
# You have the following tuples:
# vip_members = ("Alice", "Bob")
# regular_members = ("Charlie", "David")
# reserved_rooms = ("Room101", "Room102")

# Input:

# name → attendee’s name (string)

# room → requested room (string)

# day → booking day (string, e.g., "Monday")

# Rules:

# VIP members can book any room except if it’s "Room102" and the day is "Monday".

# Regular members can only book "Room101" and not on weekends ("Saturday" or "Sunday").

# Anyone else → Booking Denied.

# Expected Output:

# "Booking Confirmed" if allowed.

# "Booking Denied" otherwise.

#Example 1: 
# Input:
# Alice
# Room101
# Monday

# Output:
# Booking Confirmed

vip_members = ("Alice", "Bob")
regular_members = ("Charlie", "David")
reserved_rooms = ("Room101", "Room102")

name=input("Enter your name : ")
room=input("Enter your room number : ")
day=input("Enter your bookin day : ")

if room in reserved_rooms[0]:
    if day=='Monday' and name in vip_members:
        print("Booking Denied")
    else:
        print("Booking Confirmed")
elif room in reserved_rooms[1]:
    if  (day!="Saturday" and  day !="Sunday") and name in regular_members:
        print("Booking Confirmed")
    else:
        print("Booking Denied")
else:
    print("Booking Denied")
