# ls=[1,4,9,16,25,36,49,64,81,100]
# for val in ls:
#     print(val)
    
# tup=(1,4,9,16,25,36,49,64,81,100)
# x=16
# for el in tup:
#     if el==x:
#         print(f"{el} FOUND!!!")
#         break
    
# for i in range(1,101):
#     print(i)
# for i in range(100,0,-1):
#     print(i)

# n=5 
# for i in range(11):
#     print(f'{n} x {i} = {n*i}')

# #find the sum of first n numbers
# a=int(input())
# for i in range(a):
#     a+=i
# print('Sum is = ',a)

# #find factorial of first n numbers
# b=int(input())
# fact=1
# for i in range(1,b+1):
#     fact*=i
# print('Factorial is = ',fact)

# For Loop Practice – Level-wise
# Level 1 – Print numbers 1 to N
# Goal: Simple counting with a for loop.
# Logic:

# Take input N.

# Use for i in range(1, N+1).

# Print i.

# n=5
# for i in range(1,n):
#     print(i)
    
# # Level 2 – Sum of first N natural numbers
# # Goal: Loop to add numbers.
# # Logic:

# # Take N.

# # Create total = 0.

# # For i in 1 to N, add i to total.

# # Print total.

# a=5
# total=0
# for i in range(1,n):
#     total+=i
# print(total)

# Level 3 – Multiplication table
# Goal: Print table of a given number.
# Logic:

# Take num.

# Loop i from 1 to 10.

# Print num × i.
# b=10
# for i in range(1,10):
#     print(b*i)
# Level 4 – Factorial of a number
# Goal: Multiply sequence of numbers.
# Logic:

# Take N.

# Start fact = 1.

# For i in 1 to N, multiply fact *= i.

# Print fact.

# c=3
# fact=1
# for i in range(1,c+1):
#     fact*=i
# print(fact)
# # Level 5 – Reverse a string
# # Goal: Loop backward over a string.
# # Logic:

# # Take a string.

# # Loop from last index to first.

# # Build reverse string.
# str1 = 'Mavia'
# rev = ''
# for i in range(len(str1)-1, -1, -1):
#     rev += str1[i]
# print(rev)

    
# Level 6 – Count vowels in a string
# Goal: Check each letter for vowel.
# Logic:

# Take string input.

# Set count = 0.

# For each char in string, if vowel → increment.

# Print count.
# a=input("Enter a string: "  )
# count=0
# for char in a:
#     if char.lower() in 'aioue':
#         count += 1
# print("Number of vowels in the string is: ", count)
# Level 7 – Print pattern: right triangle
# Goal: Nested loops for stars.
# Logic:

# Take rows.

# Outer loop: i from 1 to rows.

# Inner loop: print i stars.

# Example:

# markdown
# Copy
# Edit
# *
# **
# ***
# ****

for i in range(6, 0, -1):
    for j in range(i):
        print(' ', end='*')
    print()  # New line after each row

# Level 8 – Sum of even numbers between 1 and N
# Goal: Skip odd numbers in loop.
# Logic:

# Take N.

# For i in range 1 to N.

# If i % 2 == 0, add to total.
# n=int(input("Enter a number to check if it is prime: "))
# total=0
# for i in range(1,n):
#     if i %2 ==0:
#         total += i
# print("Sum of even numbers is: ", total)
# Level 9 – Prime number check
# Goal: Find if number has factors.
# Logic:

# Take number.

# Loop from 2 to num-1.

# If divisible → not prime.
# number=int(input("Enter a number to check if it is prime: "))
# for i in range(2,number-1):
#     if number % i == 0:
#         print(f"{number} is not a prime number")
#         break
# else:
#     print(f"{number} is a prime number")      
# Level 10 – Fibonacci series
# Goal: Generate series using loop.
# Logic:

# Take N terms.

# Start with 0, 1.

# Loop and calculate next term.
n=int(input("Enter the number of terms for Fibonacci series: "))
for i in range(n):
    if i == 0:
        a = 0
    elif i == 1:
        a = 1
    else:
        a = b + c
    b, c = a, b if i > 1 else 1
    print(a, end=' ')
# Level 11 – Print multiplication tables 1–10
# Goal: Nested loop.
# Logic:

# Outer loop → number from 1 to 10.

# Inner loop → multiply by 1 to 10.

# Level 12 – Find largest number in a list
# Goal: Compare in loop.
# Logic:

# Take list.

# Assume first element is largest.

# Loop through rest, update if bigger.

# Level 13 – Count words in a sentence
# Goal: Split and loop.
# Logic:

# Take string input.

# Split into words.

# Count via loop.

# Level 14 – Check palindrome string
# Goal: Compare reverse with original.
# Logic:

# Take string.

# Reverse with loop.

# Compare.

# Level 15 – GCD of two numbers (division method)
# Goal: Find greatest common divisor.
# Logic:

# Take a and b.

# Loop i from 1 to min(a, b).

# If divides both, update gcd.

# Level 16 – Print diamond pattern
# Goal: Nested loops, spaces + stars.
# Logic:

# Take rows.

# First half: increase stars.

# Second half: decrease stars.

# Level 17 – Guess the number (fixed tries)
# Goal: Limit attempts in loop.
# Logic:

# Set secret number.

# Loop for 5 tries.

# Ask guess, check match.

# Level 18 – List comprehension challenge
# Goal: Squares of even numbers.
# Logic:

# Take list of numbers.

# Loop through and if even → square.

# Level 19 – Matrix addition
# Goal: Loop over 2D lists.
# Logic:

# Take 2 same-size matrices.

# Nested loops → sum each position.

# Level 20 – Hangman (for-loop version)
# Goal: Reveal progress in fixed turns.
# Logic:

# Set secret word.

# Start with underscores.

# For each turn:

# Ask for letter, reveal if correct.

# Stop if guessed.