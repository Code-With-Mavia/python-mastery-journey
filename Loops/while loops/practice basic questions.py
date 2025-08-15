#print numbers 1-100
# counter=1
# while counter<=100:
#     print(counter)
#     counter+=1
# print("\nloop ended\n")

#print numbers 100-1
# a=100
# while a>=1:
#     print(a)
#     a-=1
# print("\nloop ended\n")

#print the multiplaction table of number n
# c=int(input("Enter your numbr : "))
# b=0
# while b<=10:
#     print(f"{c} x {b} = {c*b}")
#     b+=1
# print("\nloop ended\n")
    
#print the elements of following list using a loop
# d=[1,4,9,16,25,36,49,81,100]
# index=0
# #here we are traversing as in travelling and performing action on each element
# while index<len(d):
#     print(d[index])
#     index+=1
    
#search for a number in the tuple by a loop  
# f=int(input("Enter the word you want to search : "))
# e=(1,4,9,16,25,36,49,81,100)
# i=0
# while i<len(e):
#     if e[i]==f:
#         print(f"Found {f} at index {i}")
#         break
#     else:
#         print('Finding .....')
#     i+=1
# print("End of loop!!")



# ## **While Loop Ladder (10 Levels)**

# ---

# ### **Level 1 – Count from 1 to 5**

# **Goal:** Just run a loop.
# **Logic:**

# 1. Start `i = 1`.
# 2. While `i <= 5`: print `i`, then `i += 1`.

# i=1
# while i <=5:
#     print(i)
#     i+=1
# ---

# ### **Level 2 – Count from any number to another**

# **Goal:** Introduce input.
# **Logic:**

# 1. Take `start` and `end` from user.
# 2. While `start <= end`: print `start`, then `start += 1`.

# start=int(input())
# end=int(input())
# while start<=end:
#     print(start)
#     start+=1
# ---

# ### **Level 3 – Count backwards**

# **Goal:** Loop with decrement.
# **Logic:**

# 1. Take `n` from user.
# 2. While `n >= 1`: print `n`, then `n -= 1`.

# n=int(input())
# while n>= 1:
#     print(n)
#     n-=1
# ---

# ### **Level 4 – Sum numbers from 1 to n**

# **Goal:** Accumulate values in a variable.
# **Logic:**

# 1. Take `n`.
# 2. `total = 0`, `i = 1`.
# 3. While `i <= n`: add `i` to `total`, then `i += 1`.
# 4. Print `total`.

# n=int(input())
# total=0
# i=0
# while i<=n:
#     total+=i
#     i+=1
# print(total)


# ---

# ### **Level 5 – Print only even numbers from 1 to n**

# **Goal:** Add condition inside loop.
# **Logic:**

# 1. Take `n`.
# 2. `i = 1`.
# 3. While `i <= n`: if `i % 2 == 0`, print it. Increment `i`.

# n=int(input())
# i=1
# while i<=n:
#     if i%2==0:
#          print(i)
#     i+=1
        
# ---

# ### **Level 6 – Reverse a number**

# **Goal:** Use division and modulus.
# **Logic:**

# 1. Take `n`.
# 2. `rev = 0`.
# 3. While `n > 0`:

#    * `last = n % 10`
#    * `rev = rev * 10 + last`
#    * `n //= 10`
# 4. Print `rev`.

# n=int(input())
# rev=0
# while n > 0:
#     last = n % 10
#     rev = rev * 10 + last
#     n //= 10
# print(rev)
# ---

# ### **Level 7 – Count digits of a number**

# **Goal:** Same as reverse but count instead.
# **Logic:**

# 1. Take `n`.
# 2. If `n == 0`: count = 1.
# 3. Else, `count = 0`.
# 4. While `n > 0`: `n //= 10`, `count += 1`.
# 5. Print `count`.

# n=int(input())
# if n==0:
#     print(1)
# else:
#     count=0
#     while n > 0:
#         n //= 10
#         count+=1
#     print(count)
# ---

# ### **Level 8 – Multiplication table**

# **Goal:** Loop with fixed iterations (10).
# **Logic:**

# 1. Take `n`.
# 2. `i = 1`.
# 3. While `i <= 10`: print `n * i`, then `i += 1`.

# n=int(input())
# c=int(input())
# i=1
# while i <= c :
#     print(f"{n} x {i} = {n*i}")
#     i+=1
# ---

# ### **Level 9 – Sum of digits**

# **Goal:** Similar to reverse but sum digits.
# **Logic:**

# 1. Take `n`.
# 2. `sum_digits = 0`.
# 3. While `n > 0`:

#    * `sum_digits += n % 10`
#    * `n //= 10`
# 4. Print `sum_digits`.

# n=int(input())
# sum_digits=0
# while n > 0:
#     sum_digits += n % 10
#     n //= 10
# print(sum_digits)
# ---

# ### **Level 10 – Guess the secret number**

# **Goal:** While loop until condition is met.
# **Logic:**

# 1. Set secret number (or read it).
# 2. Ask for guess.
# 3. While guess != secret: ask again.
# 4. Print `"Correct!"`.

# secret_number = 2
# guess = int(input("Enter your guess: "))

# while guess != secret_number:
#     guess = int(input("Enter your guess again: "))

# print("Correct!")

# ---

# ## **While Loop Ladder – Part 2**

# ---

# ### **Level 11 – Factorial**

# **Goal:** Multiply numbers from 1 to n.
# **Logic:**

# 1. Take `n`.
# 2. `fact = 1`, `i = 1`.
# 3. While `i <= n`: `fact *= i`, `i += 1`.
# 4. Print `fact`.

# n=int(input())
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)
    
# ---

# ### **Level 12 – Find the first multiple of 7 greater than n**

# **Goal:** Use loop to search.
# **Logic:**

# 1. Take `n`.
# 2. `num = n + 1`.
# 3. While `num % 7 != 0`: `num += 1`.
# 4. Print `num`.

# n=int(input())
# num=n+1
# while num %7 != 0:
#     num+=1
    
# print(num)
# ---

# ### **Level 13 – Count vowels in a string**

# **Goal:** Loop over each character manually.
# **Logic:**

# 1. Take a string.
# 2. Set `count = 0`, `i = 0`.
# 3. While `i < len(string)`:

#    * If char in `"aeiouAEIOU"` → `count += 1`.
#    * `i += 1`.
# 4. Print `count`.

# s=input("")
# count = 0
# i=0
# while i < len(s):
#     if s[i] in "aeiouAEIOU":
#         count += 1
#     i+=1
# print(count)
# ---

# ### **Level 14 – Check if a number is prime**

# **Goal:** Break early when divisor is found.
# **Logic:**

# 1. Take `n`.
# 2. `i = 2`, flag = True.
# 3. While `i <= n // 2`:

#    * If `n % i == 0`: flag = False, break.
#    * Else, `i += 1`.
# 4. Print “Prime” if flag True else “Not prime”.

# n = int(input())
# i = 2
# flag = True

# while i <= n // 2:
#     if n % i == 0:
#         flag = False
#         break
#     i += 1

# if flag and n > 1:
#     print("Prime")
# else:
#     print("Not Prime")

    
# ---

# ### **Level 15 – Fibonacci series (n terms)**

# **Goal:** Generate series in loop.
# **Logic:**

# 1. Take `n`.
# 2. `a = 0`, `b = 1`, `count = 0`.
# 3. While `count < n`:

#    * Print `a`.
#    * `a, b = b, a + b`.
#    * `count += 1`.

# n = int(input())
# a=0
# b=1
# count=0
# while count<n:
#     print(a)
#     a=b
#     b=a+b
#     count+=1
    
# ---

# ### **Level 16 – Keep summing until user enters 0**

# **Goal:** Loop until a sentinel value.
# **Logic:**

# 1. `total = 0`.
# 2. Take input `num`.
# 3. While `num != 0`:

#    * Add to total.
#    * Take next input.
# 4. Print total.


# total=0
# num=int(input())
# while num!=0:
#     total+=num
#     num=int(input())

# print(total)
    
# ---

# ### **Level 17 – Find smallest number from inputs until negative number**

# **Goal:** Loop until stopping signal.
# **Logic:**

# 1. Take first input → smallest = that number.
# 2. While input >= 0:

#    * If input < smallest: update smallest.
#    * Take next input.
# 3. Print smallest.

# num = int(input("Enter number: "))

# if num < 0:
#     print("No positive numbers entered")
# else:
#     smallest = num
#     while num >= 0:
#         if num < smallest:
#             smallest = num
#         num = int(input("Enter number: "))
#     print("Smallest number is:", smallest)
        
# ---

# ### **Level 18 – Power of a number (a^b)**

# **Goal:** Repeat multiplication b times.
# **Logic:**

# 1. Take base `a` and exponent `b`.
# 2. `result = 1`, `i = 0`.
# 3. While `i < b`:

#    * Multiply `result *= a`.
#    * `i += 1`.
# 4. Print result.


# a=2
# b=3
# result=1
# i=0
# while i < b:
#     result*=a
#     i+=1
# print(result)
    
# ---

# ### **Level 19 – GCD of two numbers**

# **Goal:** Use repeated subtraction method.
# **Logic:**

# 1. Take `a` and `b`.
# 2. While `a != b`:

#    * If a > b: a -= b.
#    * Else: b -= a.
# 3. Print `a`.

# c=18
# d=24
# while c!=d:
#     if c>d:
#         c-=d
#     else:
#         d-=c
# print(c)
# ---

# ### **Level 20 – Guess the word (like Hangman)**

# **Goal:** Multiple wrong guesses allowed, reveal progress.
# **Logic:**

# 1. Set secret word.
# 2. Create `progress` as underscores for each letter.
# 3. While progress is not equal to secret word:

#    * Ask for a letter.
#    * If in word: update progress.
#    * Else: tell “Wrong guess”.
# 4. Print “You guessed it!”.

# secret_word = "Hang Man"
# progress = "_" * len(secret_word)

# while progress != secret_word:
#     word = input("ENTER YOUR LETTER : ")
#     new_progress = ""

#     if word in secret_word:
#         for i in range(len(secret_word)):
#             if secret_word[i].lower() == word.lower():
#                 new_progress += secret_word[i]
#             else:
#                 new_progress += progress[i]
#         progress = new_progress
#         print(progress)
#     else:
#         print("Wrong guess")

# print("You guessed it!")

# ---

#find the sum of first n numbers

n=int(input())
sum=0
count=0
while count <=n:
    sum+=count
    count+=1
print(sum)

