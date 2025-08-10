grades=('C','D','A','A', 'B', 'B', 'A')
print(type(grades))
print(grades)
results=list(grades)
print(grades.count("A"))
results.sort()
print(type(results))
print(results)

#Create a tuple named colors containing "red", "green", and "blue".
colors=("red", "green", "blue")
print(type(colors))
print(colors)

#Given the tuple numbers = (10, 20, 30, 40), print the second element
numbers = (10, 20, 30, 40)
print(numbers[1])
#Given the tuple letters = ('a', 'b', 'c', 'd', 'e'), print only the first three elements using slicing.
letters = ('a', 'b', 'c', 'd', 'e')
print(letters[:3])
# Given the tuple fruits = ("apple", "banana", "cherry"), check if "banana" is in the tuple. If yes, print "Found".
fruits = ("apple", "banana", "cherry")
if 'banana' in fruits:
    print(f"Found ")
else:
    print(f"Not Found ")
# Given the tuple animals = ("dog", "cat", "elephant", "lion"), print how many items are in it.
animals = ("dog", "cat", "elephant", "lion")
print(len(animals))
