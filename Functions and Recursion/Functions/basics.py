# Level 1 — Basics: Defining and Calling Functions
#print the lenght of list using fucntions 
numbers= [1, 2, 3, 4, 5]
def lenght(list):
    print(len(list))
lenght(numbers)  # Output: 5

#print the element of lists in a single line using functions
def print_elements_in_single_line(lst):
    for i in lst:
        print(i,end='')
    print()
print_elements_in_single_line(numbers)  # Output: 12345

#find the factorial of n (n is a paremeter)
n=int(input("Enter a number to find its factorial: "))
def factorial(n):
    fact=1
    for i in range(1, n + 1):
        fact *= i
    print(fact)
factorial(n)


currency=int(input("Enter your currency : "))
# convert usd to pkr
def usd_to_pkr(usd):
    conversion=usd*283.61
    print(conversion)
usd_to_pkr(currency)

#Write a function square(num) that returns the square of a number. Call it with different numbers.
def square(num):
    print(num**2)
square(2)

#Write a function add_two_numbers(a, b) that returns the sum of a and b
def add_two_numbers(a, b):
    print(a+b)
add_two_numbers(1,2)

#Write a function is_even(num) that returns True if the number is even, otherwise False.
def is_even(num):
    if num %2 == 0:
        print(True)
    else:
        print(False)
is_even(2)
is_even(3)

# Level 2 — Parameters & Return Values

# Write a function greet_user(name, age) that prints "Hi <name>, you are <age> years old".
def greet_user(name, age):
    return name , int(age )
name,age=greet_user('Ali', 20)
print(f'Hi {name}, you are {age} years old')
# Write a function fahrenheit_to_celsius(f) that converts Fahrenheit to Celsius using the formula:
# 𝐶 =(𝐹 −32)×5/9​
def fahrenheit_to_celsius(f):
    c=(f-32)*5/9
    return int(c)
print(fahrenheit_to_celsius(112))   

# Write a function max_of_two(a, b) that returns the bigger of the two numbers.
def max_of_two(a, b):
    if a>b:
        return a 
    else:
        return b
print(max_of_two(2, 1))
# Write a function repeat_text(text, times) that prints text exactly times times.
def repeat_text(text, times):
    times=int(times)
    for _ in range(times):
        print(text)
repeat_text('text', 2)
# Write a function calculate_area_rectangle(length, width) that returns the area of a rectangle.
def calculate_area_rectangle(length, width):
    area= length*width
    return area
print(calculate_area_rectangle(2, 2))

# Level 3 — Slightly More Logic
# Write a function is_palindrome(word) that returns True if the word is a palindrome (same forward & backward).
def is_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
print(is_palindrome('alao'))
# Write a function sum_list(numbers) that returns the sum of all numbers in a list.

def sum_list(numbers):
    total=0
    for i in numbers:
        total+=i
    return total
print(sum_list([1, 2, 3, 4, 5]))
# Write a function count_vowels(text) that returns the number of vowels in a string.
def count_vowels(text):
    count=0
    text=str(text)
    for char in text:
        if char.lower() in 'aeiou' :
            count+=1
    return count
        
print(count_vowels('alifallahorinsans'))
# Write a function find_max_in_list(numbers) that returns the largest number from a list.
def find_max_in_list(numbers):
    max_num = numbers[0]    
    for i in numbers:
        if i>max_num:
            max_num=i
    return max_num

print(find_max_in_list([1, 2, 6, 4, 5]))