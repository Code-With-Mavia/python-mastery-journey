# ### **1. Common Students**

# **Problem:**
# You are given two sets of student names — one for students enrolled in a Python course and another for students enrolled in a Java course. Your task is to find students who are enrolled in **both** courses.

# **Input:**

# * Two sets:

#   * `python_students`
#   * `java_students`

# **Output:**

# * If there are common students, print their names as a set.
# * If there are no common students, print `No common students`.
python_students={"ali","asghar","javaid","mavia"}
java_students={'ahmad','asghar','','ghamis','mavia'}
common_students = python_students & java_students

if java_students.union(python_students):
   print( common_students)
else:
    print("No common students")
# ---

# ### **2. Unique Ingredients**

# **Problem:**
# Two chefs have provided their recipe ingredient lists. You need to print the ingredients that are unique to the **first recipe** only.

# **Input:**

# * Two sets:

#   * `recipe1`
#   * `recipe2`

# **Output:**

# * Print a set containing only the ingredients in `recipe1` but not in `recipe2`.
recipe1 = {"flour", "sugar", "eggs", "butter"}
recipe2 = {"sugar", "eggs", "milk", "vanilla"}
unique_ingredients=recipe1.difference(recipe2)

print(unique_ingredients)



# ### **3. VIP Access**

# **Problem:**
# You are managing a VIP lounge with a predefined list of VIP members.
# Check if a person’s name entered by the user is in the VIP list.

# **Input (example values):**

# ```python
# vip_members = {"Alice", "Bob", "Charlie", "Diana"}
# name = input("Enter your name: ")
# ```

# **Expected Output:**

# * `"Access Granted"` if the name is in `vip_members`.
# * `"Access Denied"` otherwise.
vip_members = {"Alice", "Bob", "Charlie", "Diana"}
name = input("Enter your name: ").title()
if name in vip_members:
    print("Access Granted")
else:
    print("Access Denied")
# ---

# ### **4. Symmetric Difference for Events**

# **Problem:**
# You have two events, and each has a set of attendees.
# Find the names of people who attended **exactly one** event.

# **Input (example values):**

# ```python
# eventA_attendees = {"John", "Alice", "Mark", "Nina"}
# eventB_attendees = {"Alice", "George", "Nina", "Tom"}
# ```

# **Expected Output:**

# * A set containing attendees who went to **only one** event.
#   For the above input:

# ```python
# {'Tom', 'George', 'John', 'Mark'}
# ```
eventA_attendees = {"John", "Alice", "Mark", "Nina"}
eventB_attendees = {"Alice", "George", "Nina", "Tom"}
only_one_event=eventA_attendees.symmetric_difference(eventB_attendees)
print(only_one_event)
# ---

# ### **5. Check Subset**

# **Problem:**
# A student’s eligibility is determined by whether they have completed all required courses.
# Check if the student has completed all the required courses.

# **Input (example values):**

# ```python
# required_courses = {"Math", "Physics", "Chemistry"}
# student_courses = {"Math", "Physics", "Chemistry", "Biology"}
# ```

# **Expected Output:**

# * `"Eligible"` if all required courses are in `student_courses`.
# * `"Not Eligible"` otherwise.
required_courses = {"Math", "Physics", "Chemistry"}
student_courses = {"Math",  "Chemistry", "Biology"}
if required_courses.issubset(student_courses):
    print("Eligible")
else:
    print("Not Eligible")
# ---

# ### **1. Common Hobbies Finder**

# **Problem:**
# Two friends list their hobbies. You need to print the hobbies they both have in common.

# **Input:**

# ```python
# friend1_hobbies = {"Reading", "Cycling", "Cooking"}
# friend2_hobbies = {"Cooking", "Swimming", "Reading"}
# ```

# **Output:**

# ```
# {'Reading', 'Cooking'}
# ```
friend1_hobbies = {"Reading", "Cycling", "Cooking"}
friend2_hobbies = {"Cooking", "Swimming", "Reading"}
common_hobbies=friend1_hobbies.intersection(friend2_hobbies)
print(common_hobbies)
# ---

# ### **2. Conference Unique Attendees**

# **Problem:**
# You’re managing two conferences. Find the attendees who attended **only one** of them.

# **Input:**

# ```python
# conferenceA = {"Alice", "Bob", "Charlie"}
# conferenceB = {"Bob", "David", "Eve"}
# ```

# **Output:**

# ```
# {'Charlie', 'David', 'Eve', 'Alice'}
# ```
conferenceA = {"Alice", "Bob", "Charlie"}
conferenceB = {"Bob", "David", "Eve"}
commom=conferenceA.symmetric_difference(conferenceB)
print(commom)
# ---

# ### **3. Country Membership Check**

# **Problem:**
# You have a list of countries where your company operates.
# Check if a user’s input country is in the list.

# **Input:**

# ```python
# countries = {"USA", "Canada", "Germany", "Japan"}
# country_name = input("Enter your country: ")
# ```

# **Output:**
# If `country_name` is in the set:

# ```
# We operate in your country.
# ```

# Otherwise:

# ```
# Sorry, we do not operate in your country.
# ```
countries = {"USA", "Canada", "Germany", "Japan"}
country_name = input("Enter your country: ").strip()
if country_name in  countries:
    print("We operate in your country.")
else:
    print("Sorry, we do not operate in your country.")

# ---

# ### **4. Students in All Clubs**

# **Problem:**
# Find students who are in **all three clubs**.

# **Input:**

# ```python
# art_club = {"Tom", "Jerry", "Alice", "Bob"}
# science_club = {"Alice", "Bob", "David"}
# sports_club = {"Bob", "Alice", "Eve"}
# ```

# **Output:**

# ```
# {'Bob', 'Alice'}
# ```
art_club = {"Tom", "Jerry", "Alice", "Bob"}
science_club = {"Alice", "Bob", "David"}
sports_club = {"Bob", "Alice", "Eve"}
all_clubs=art_club.intersection(science_club)
all_clubs.intersection(sports_club)
print(all_clubs)
# ---

# ### **5. Remove Duplicates from a List**

# **Problem:**
# Given a list with repeated values, print the list without duplicates using a set.

# **Input:**

# ```python
# numbers = [1, 2, 2, 3, 4, 4, 5]
# ```

# **Output:**

# ```
# {1, 2, 3, 4, 5}
# ```
numbers = [1, 2, 2, 3, 4, 4, 5]
print(set(numbers))


# ## **1. Unique Visitors Counter**

# **Problem:**
# You are tracking website visitors over two days.
# Find the **total number of unique visitors** across both days.

# **Input:**

# * Two sets:

#   * `day1_visitors`
#   * `day2_visitors`

# **Output:**

# * Integer: total number of unique visitors.

# **Example Input:**

# ```python
# day1_visitors = {"Alice", "Bob", "Charlie"}
# day2_visitors = {"Bob", "David", "Emma"}
# ```

# **Example Output:**

# ```
# 5
# ```
day1_visitors = {"Alice", "Bob", "Charlie"}
day2_visitors = {"Bob", "David", "Emma"}
unique_visitors=day1_visitors.union(day2_visitors)
print(unique_visitors)
print(len(unique_visitors))
# ---

# ## **2. Missing Students in Class**

# **Problem:**
# You have a set of enrolled students and a set of students who attended class today.
# Print the names of students who **did not attend**.

# **Input:**

# * `enrolled_students`
# * `attended_students`

# **Output:**

# * Set of students who missed the class.

# **Example Input:**

# ```python
# enrolled_students = {"John", "Sara", "Mike", "Nina"}
# attended_students = {"John", "Mike"}
# ```

# **Example Output:**

# ```
# {'Sara', 'Nina'}
# ```
enrolled_students = {"John", "Sara", "Mike", "Nina"}
attended_students = {"John", "Mike"}
missing_students=enrolled_students.difference(attended_students)
print(missing_students)
# ---

# ## **3. Common Courses Between Students**

# **Problem:**
# Two students have chosen their courses.
# Find the courses that **both students** are taking.

# **Input:**

# * `student1_courses`
# * `student2_courses`

# **Output:**

# * Set of common courses.

# **Example Input:**

# ```python
# student1_courses = {"Math", "Science", "History"}
# student2_courses = {"Art", "Science", "History"}
# ```

# **Example Output:**

# ```
# {'Science', 'History'}
# ```
student1_courses = {"Math", "Science", "History"}
student2_courses = {"Art", "Science", "History"}
common_courses=student1_courses.intersection(student2_courses)
print(common_courses)
# ---

# ## **4. Remove Duplicate Words from a Sentence**

# **Problem:**
# Given a sentence, remove all duplicate words and print the unique words.

# **Input:**

# * String: `sentence`

# **Output:**

# * Set of unique words from the sentence.

# **Example Input:**

# ```
# I love coding and I love Python
# ```

# **Example Output:**

# ```
# {'I', 'love', 'coding', 'and', 'Python'}
# ```
sentence = "I love coding and I love Python"
unique_words = set(sentence.split())
print(unique_words)


# ---

# ## **5. Friends Who Are Not Common**

# **Problem:**
# Two friends list the people they know.
# Find the people who are known to **only one of them**, not both.

# **Input:**

# * `friend1_known`
# * `friend2_known`

# **Output:**

# * Set of people unique to one friend.

# **Example Input:**

# ```python
# friend1_known = {"Alex", "Brian", "Cathy"}
# friend2_known = {"Brian", "Diana", "Eva"}
# ```

# **Example Output:**

# ```
# {'Alex', 'Cathy', 'Diana', 'Eva'}
# ```
friend1_known = {"Alex", "Brian", "Cathy"}
friend2_known = {"Brian", "Diana", "Eva"}
unique_frineds=friend1_known.symmetric_difference(friend2_known)
print(unique_frineds)
# ---
