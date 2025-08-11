# ### **Beginner Set Questions**

# 1. **Create a Set**

#    * Create a set containing the numbers `{1, 2, 3, 4, 5}` and print it.
a={1, 2, 3, 4, 5}
print(a)
print(type(a))

# 2. **Add an Element**

#    * Start with a set `{1, 2, 3}` and add the number `4` to it.
b={1, 2, 3}
b.add(4)
print(b)

# 3. **Remove an Element**

#    * From the set `{10, 20, 30}`, remove `20`.
c={10, 20, 30}
c.remove(20)
print(c)
# 4. **Check Membership**

#    * Given `{apple, banana, orange}`, check if `"banana"` is in the set.
d={"apple", "banana", "orange"}
if 'banana' in d:
    print("OK")
else:
    print("NOT OK")
# 5. **Length of Set**

#    * Find the length of `{5, 10, 15, 20}`.
e={5, 10, 15, 20}
print(len(e))
# 6. **Union of Sets**

#    * Find the union of `{1, 2, 3}` and `{3, 4, 5}`.
f={1, 2, 3}
g={3, 4, 5}
print(g.union(f))
# 7. **Intersection of Sets**

#    * Find the intersection of `{a, b, c}` and `{b, c, d}`.
h={"a","b","c"}
i={"b", "c", "d"}
i.intersection(h)
print(i)

# 8. **Difference of Sets**

#    * Find the difference between `{1, 2, 3, 4}` and `{3, 4, 5, 6}`.
j={1, 2, 3, 4}
k={3, 4, 5, 6}
k.difference(j)
print(k)
# 9. **Clear a Set**

#    * Clear all elements from the set `{100, 200, 300}`.
l={100, 200, 300}
print(l.clear())
# 10. **Convert List to Set**

#     * Convert the list `[1, 2, 2, 3, 4, 4]` into a set.
m=set([1, 2, 2, 3, 4, 4])
print(m)


### **More Basic Set Questions**

# 11. **Frozen Set**

#     * Create a `frozenset` from `{1, 2, 3}` and print it.
n=frozenset({1, 2, 3}) #frozen set is immutable other than set
print(n)

# 12. **Set from String**

#     * Create a set from the string `"banana"` and print it.
o={"banana"}
print(o)
# 13. **Pop an Element**

#     * Use `.pop()` to remove an arbitrary element from `{10, 20, 30}` and print the set.
p={10, 20, 30}
print(p.pop())
print(p)
# 14. **Discard an Element**

#     * Use `.discard()` to remove `5` from `{1, 3, 5, 7}`.
q={1, 3, 5, 7}
q.discard(5)
print(q)
# 15. **Symmetric Difference**

#     * Find the symmetric difference between `{1, 2, 3}` and `{3, 4, 5}`.
r={1, 2, 3}
s={3, 4, 5}
print(s.difference(r))
# 16. **isdisjoint() Check**

#     * Check if `{1, 2, 3}` is disjoint from `{4, 5, 6}`.
t={1, 2, 3}
u={4, 5, 6}
print(t.isdisjoint(u))
# 17. **issubset() Check**

#     * Check if `{1, 2}` is a subset of `{1, 2, 3}`.
v={1, 2}
w={1, 2,3 }
print(v.issubset(w))
# 18. **issuperset() Check**

#     * Check if `{1, 2, 3}` is a superset of `{1, 2}`.
x={1, 2, 3}
y={1, 2}
print(x.issuperset(y))
# 19. **Copy a Set**

#     * Create a copy of `{a, b, c}` into a new set and print it.
z={"a", "b", "c"}
ab=z.copy()
print(ab)
# 20. **Update a Set**

#     * Use `.update()` to add elements from `{4, 5, 6}` into `{1, 2, 3}`.
ac={1, 2, 3}
ad={4,5,6}
ac.update(ad)
print(ac)
