# 🟣 Question 1 – Reverse the Words
# Input: "hello world python"
# Task: Reverse the order of the words (not the letters).
# Expected Output: "python world hello"
# (Hint: use .split() and .join())

# 🟣 Question 2 – Make It Snake Case
# Input: "This Is Snake Case"
# Task: Convert it to: "this_is_snake_case"
# (Hint: .lower(), .split(), .join())

# 🟣 Question 3 – Middle Character
# Input: "Python"
# Task: Print only the middle character(s)

# If odd length → one character

# If even length → two characters
# Expected Output: "th" (for "Python")

# (Hint: Use len() and slicing, no if-else, so think of it like: use slicing range from len//2 - 1 to len//2 + 1)

# 🟣 Question 4 – Remove All Vowels
# Input: "Remove my vowels"
# Task: Output with vowels removed → "Rmv my vwls"
# (Hint: You can chain .replace() calls like s.replace("a", "")...)

# 🟣 Question 5 – Hide Half the Word
# Input: "secret"
# Task: Replace the first half of the word with "*"
# Expected Output: "***ret"
# (Hint: use len() to get half, and use slicing + * multiplication)

s="hello world python"
words=s.split()
reversed_words=words[::-1]
result= " ".join(reversed_words)
print(result)

a="This Is Snake Case"
words=a.lower()
split_it=words.split()
result1="_".join(split_it)
print(result1)

b="Python"
mid=len(b)//2
print(b[mid-1:mid+1])

c="Remove my vowels"
c=c.replace('a', '')
c=c.replace('e', '')
c=c.replace('i', '')
c=c.replace('o', '')
c=c.replace('u', '')

print(c)

d="secret"
masked="*"*(len(d)//2)
visible=d[len(d)//2:]
secret=masked+visible
print(secret)


