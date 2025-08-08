# 🔤 Python String Practice Questions (Beginner Level)

This is a curated list of beginner-friendly string problems using **only** basic string functions and slicing. No loops, no lists, no functions — just pure string logic for revision and mastery.

---

## 🟣 Question 1 – Remove Extra Spaces

**📥 Input**: `" Hello World "`  
**🎯 Task**: Remove spaces from the beginning and end  
**📤 Output**: `"Hello World"`  
💡 `.strip()`

---

## 🟣 Question 2 – Convert to Uppercase

**📥 Input**: `"python is fun"`  
**🎯 Task**: Convert all letters to uppercase  
**📤 Output**: `"PYTHON IS FUN"`  
💡 `.upper()`

---

## 🟣 Question 3 – Replace a Word

**📥 Input**: `"I like java"`  
**🎯 Task**: Replace `"java"` with `"Python"`  
**📤 Output**: `"I like Python"`  
💡 `.replace()`

---

## 🟣 Question 4 – First 3 Letters

**📥 Input**: `"Elephant"`  
**🎯 Task**: Show first 3 letters  
**📤 Output**: `"Ele"`  
💡 `s[:3]`

---

## 🟣 Question 5 – Last 2 Letters

**📥 Input**: `"Notebook"`  
**🎯 Task**: Show last 2 letters  
**📤 Output**: `"ok"`  
💡 `s[-2:]`

---

## 🟣 Question 6 – Count Words

**📥 Input**: `"The sky is blue"`  
**🎯 Task**: Count words  
**📤 Output**: `4`  
💡 `.split()` and `len()`

---

## 🟣 Question 7 – Title Case Sentence

**📥 Input**: `"hElLo wORld, thIs is a tESt"`  
**🎯 Task**: Convert to title case  
**📤 Output**: `"Hello World, This Is A Test"`  
💡 `.title()`

---

## 🟣 Question 8 – Middle Character(s)

**📥 Input**: `"Python"`  
**🎯 Task**: Print middle character(s)  
- If length is **odd** → 1 character  
- If **even** → 2 characters  
**📤 Output**: `"th"`  
💡 `s[len(s)//2 - 1 : len(s)//2 + 1]`

---

## 🟣 Question 9 – Capitalize First Word

**📥 Input**: `"python is amazing"`  
**🎯 Task**: Capitalize only the first character  
**📤 Output**: `"Python is amazing"`  
💡 `.capitalize()`

---

## 🟣 Question 10 – Email Masking

**📥 Input**: `"mawiahqaiser@example.com"`  
**🎯 Task**: Mask part before `@`  
**📤 Output**: `"m********r@example.com"`  
💡 Use slicing, `find('@')`, and concatenation

---

> ✅ No need for loops or conditions — just use your string slicing and built-in functions.

---
