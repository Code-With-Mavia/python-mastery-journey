code = input("Enter product code: ").strip()
parts = code.split("-")

# Step 1: Check if exactly two hyphens (=> 3 parts)
if len(parts) != 3:
    print("INVALID – not exactly 2 hyphens")
    print("INVALID ->", code)

else:
    category, year, batch = parts[0], parts[1], parts[2]
    
    # Rule 1: Category must be 3 uppercase letters
    if len(category) != 3 or not category.isalpha() or not category.isupper():
        print("INVALID – category must be 3 uppercase letters")
        print("INVALID ->", code)

    # Rule 2: Year must be 4-digit and between 2000-2025
    elif not (year.isdigit() and len(year) == 4):
        print("INVALID – year must be 4 numeric digits")
        print("INVALID ->", code)
    elif not (2000 <= int(year) <= 2025):
        print("INVALID – year out of valid range (2000-2025)")
        print("INVALID ->", code)

    # Rule 3: Batch must be alphanumeric and at least 3 characters
    elif len(batch) < 3 or not batch.isalnum():
        print("INVALID – batch must be at least 3 alphanumeric characters")
        print("INVALID ->", code)

    else:
        print("VALID ->", code)
