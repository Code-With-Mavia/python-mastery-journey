#######################################check if a person is eligible for vote or not######################################
age=int(input('Ente your age : '))
if age>=18:
    print('Person is eligible to vote' )
else:
    print('Person is not eligible to vote')

######################################Grade students based on marks######################################

marks=int(input("Enter your marks : "))

# First appraoch
if marks>=90:
    grade='A'
elif 90>marks>=80:
    grade='B'
elif 80>marks>=70:
    grade='C'
elif marks>70:
    grade='D'
else:
    grade='F'

#2nd approach

if marks>=90:
    grade='A'
elif marks>=80 and marks<90:
    grade='B'
elif marks>=70 and marks<80:
    grade='C'
elif marks>70:
    grade='D'
else:
    grade='F'

print("Your Grdae is -> ", grade)

#######################################check if a person is eligible for drive or not and also check if he is elgible till 80 or not to not drive######################################
#nesting in conditions like a condition in a conditon 
age=int(input('Ente your age : '))
if age>=18:
    if age>=80:
        print('Person is not elgible to drive' )
    else:
        print('Person is  elgible to drive' )
else:
    print('Person is not eligible to drive')
    

#######################################check if the number is odd or even######################################
#odd= not divisible by 2
#even= divisible by 2

a=int(input("Enter number :  "))

if a%2==0:
    print("The number is even")
else:
    print("The number is odd")
    
    
#######################################find greatest of 4 numbers entered by a user######################################

a=int(input("Enter First number :  "))
b=int(input("Enter Second number :  "))
c=int(input("Enter Third number :  "))
d=int(input("Enter Fourth number :  "))

if a>=b and a>=c and a>=d:
    print('First number :',a)
elif b>=c and b>=d :
    print('Second number :',b)
elif c>=d :
    print('Third number :',b)
else:
    print('Fourth number :',d)




######################################check if a numer is a mutliple of 7 or not######################################
a=int(input("Enter number :  "))

if a%7==0:
    print("The number is multiple of 7")
else:
    print("The number is not multiple of 7")