# Flight Seat Upgrade Eligibility
# Problem Statement:
# An airline is offering a free seat upgrade for certain passengers.
# A passenger qualifies for an upgrade if:

# Their ticket class is "Economy" and their loyalty tier is "Gold" or "Platinum".

# OR their ticket class is "Business" and their flight is on a weekend ("Saturday" or "Sunday").

weekend_days = ["Saturday", "Sunday"]
loyal_tier=['Gold','Platinum','Silver']
ticket_class=["Economy", "Business", "First"]

flight_day=input("Enter your flight day : ")
loyalty=input("Enter your loyalty tier : ")
ticket_type=input("Enter your ticket type : ")

if flight_day in weekend_days:
    if loyalty in loyal_tier:
        if ticket_type in ticket_class :
            print(" UPGRADE APPROVED ")
        else:
            print(f" NO UPGRADE {ticket_type} ")
    else:
        print(f" Invalid loyalty tier {loyalty} ")
else:
    print(f" Invalid flight day {flight_day} ")
    