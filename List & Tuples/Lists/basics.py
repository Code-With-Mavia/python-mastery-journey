
#1️⃣ First and Last Element
a=[10, 20, 30, 40]
print(a[0], a[-1]) 

#2️⃣ List Length
b=['apple', 'banana', 'cherry']
print(len(b))

#3️⃣ Add Element to List
c=[1, 2, 3]
c.append(4)
print(c)

#4️⃣ Change Element Value
d=[5, 6, 7]
d[1]=60
print(d)

#5️⃣ Remove Element
e=['a', 'b', 'c']
e.remove('b')
print(e)

# sort the list in asceding and descending order

f=['banana', 'apple', 'cherry']
f.sort()
print(f)
f.sort(reverse=True)
#f.reverse() we can use this also 
print(f)


#ask the user to enter thier 3 favourtie movies atlest and store them in a list 

g=input(" Enter your movies ").split() # a common way to take input from a user as a list
result=[]
if len(g)!=3:
    print("Enter atleast 3 movies ")
else:
    result=g
    print(type(result))
    print(result)
    
#to check if a list contains a palindrom of elements or not 

list1=[1,2,1,3]
copy_list1=list1.copy()
copy_list1.reverse()

if copy_list1==list1:
    print("Palindrome")
else:
    print("Not palindrome")