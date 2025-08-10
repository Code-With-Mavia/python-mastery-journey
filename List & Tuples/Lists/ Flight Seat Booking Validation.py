# Flight Seat Booking Validation
# Description
# An airline’s booking system needs to check if a passenger’s selected seat is available and valid for booking.

# The list booked_seats contains seat numbers that are already taken.

# Seat numbers are in the format: "A1", "B3", "C5", etc.

# A valid seat is one from row "A" to "F" and seat numbers 1 to 6.

# The program should:

# Check if the chosen seat is in a valid format and within allowed range.

# If it’s valid and not in booked_seats → Output "Seat Available".

# If it’s valid but already booked → Output "Seat Already Taken".

# If it’s invalid → Output "Invalid Seat".


booked_seats = ["A1", "B3", "C5"]
chosen_seat=input("Enter the desired seat you want : ")
valid_rows = ["A", "B", "C", "D", "E", "F"]
valid_numbers = ["1", "2", "3", "4", "5", "6"]

if chosen_seat[0] in valid_rows:
    if chosen_seat[1:] in valid_numbers:
        if chosen_seat in booked_seats:
            print(f"Seat Already Taken {chosen_seat}")
        else:
            print(f"Seat is available {chosen_seat}")
    else:
        print(f"Invalid seat {chosen_seat}")
else:
    print(f"Invalid seat {chosen_seat}")


            
            
            
        
    
