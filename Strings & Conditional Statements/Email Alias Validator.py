'''💡 Problem: Email Alias Validator
🔴 Difficulty: Hard
📂 Category: Strings, Indexing, Conditionals, Slicing, Real-World Logic
📝 Problem Statement
You're building a system that processes email aliases used in a corporate network.

In this system, the following rules are applied to the local part (before the @) of email addresses:

Any string after a plus sign (+) in the local part is ignored.

Any dots (.) in the local part are also ignored (they’re just visual).

The domain part (after the @) must exactly match "company.com" to be valid.

All comparisons are case-insensitive.

🧪 Input Format
You are given a single string representing an email address.
You must normalize and validate it based on the above rules.

✅ Output Requirements
Print "VALID" if the email is accepted by the system after normalization.
Otherwise, print "INVALID".

🔧 Constraints
Do not use loops or list comprehensions.

Use only string operations, slicing, indexing, and conditionals.

Only one @ will be present in the input.

📌 Examples
Example 1:
python
Copy
Edit
Input: "John.Smith+spam@company.com"
Output: VALID
Example 2:
python
Copy
Edit
Input: "Alice+newsletter@Company.Com"
Output: VALID
Example 3:
python
Copy
Edit
Input: "Bob+test@otherdomain.com"
Output: INVALID
Example 4:
python
Copy
Edit
Input: "Mark.Zucker+something@Company.Com"
Output: VALID
Example 5:
python
Copy
Edit
Input: "invalidemail@company.org"
Output: INVALID
💡 Hints
Use .lower() to make it case-insensitive.

Use .split('@') to separate local and domain parts.

Use .split('+')[0] to remove the aliasing.

Use .replace('.', '') to remove dots.

Compare domain part using ==.

'''


email = input("Enter your email to check VALID/INVALID : ")

if '@' in email:
    parts = email.split('@')
    local = parts[0]
    domain = parts[1].lower()

    # Safely remove '+' and everything after it
    if '+' in local:
        local = local[:local.index('+')]

    # Remove all dots from local part
    local = local.replace('.', '')

    # Convert domain to lowercase for comparison
    domain = domain.lower()

    if domain == 'company.com':
        print("VALID ->", local + '@' + domain)
    else:
        print("INVALID ->", local + '@' + domain)
else:
    print("INVALID ->", email)
