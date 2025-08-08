'''🧠 TOUGHEST STRINGS-ONLY CHALLENGE
🔍 String Dissection Puzzle
You are given a long sentence as input. Perform exactly the following operations in order using only string methods:

📝 Input:
A single string sentence (e.g., s = "The Quick Brown Fox Jumps Over The Lazy Dog")

🚧 Transformations (in this order):
Convert the entire string to lowercase.

Replace all spaces with underscores _.

Replace the word "the" with "xxx" only if it's a full word (not part of "them" or "other").

Remove the first 3 characters and the last 3 characters of the result.

Count how many times the letter "o" appears.

Print:

the final transformed string,

its length,

and the count of "o".'''


s = input("Enter any sentence : ")

s=s.lower()
s=s.replace(" ","_")
s=s.replace('the','xxx')
s[:3]

print(s)
print(len(s))
print(s.count('o'))
