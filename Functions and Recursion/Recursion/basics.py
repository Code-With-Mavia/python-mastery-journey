
# #print the element of lists in a single line using functions
numbers= [1, 2, 3, 4, 5]
def print_elements_in_single_line(lst,index):
    if index==len(lst):
        return 0
    print(lst[index])
    return print_elements_in_single_line(lst,index+1)
print()
result=print_elements_in_single_line(numbers,0)  # Output: 12345
print(result)
#find the factorial of n (n is a paremeter)
n=int(input("Enter a number to find its factorial: "))
def factorial(n):
    if n==0 or n ==1:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(n)
print(f"The factorial of {n} is: {result}")

#recursive fucntion to calcuate the sum of first n natural numbers
n=int(input("Enter a number to find its sum: "))

def sum_of_first_n_natural_numbers(n):
    if n == 0:
        return 0
    print(n)
    return  n + sum_of_first_n_natural_numbers(n-1) 
result=sum_of_first_n_natural_numbers(n)
print(result)