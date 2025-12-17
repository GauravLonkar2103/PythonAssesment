print("\n--- STRING QUESTIONS ---")
 
# 1. Count vowels, consonants, digits, special characters
s = input("Enter a string: ")
 
vowels = consonants = digits = special = 0
for ch in s:
  if ch.lower() in "aeiou":
    vowels += 1
  elif ch.isalpha():
    consonants += 1
  elif ch.isdigit():
    digits += 1
  else:
    special += 1
 
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)
 
# 2. Reverse each word without changing order
words = s.split()
print("Reversed words:", " ".join(word[::-1] for word in words))
 
# 3. Palindrome check
print("Palindrome" if s == s[::-1] else "Not Palindrome")
 
# 4. Frequency of each character
freq = {}
for ch in s:
  freq[ch] = freq.get(ch, 0) + 1
    print("Character frequency:", freq)
 
# 5. String immutability
try:
  s[0] = 'X'
except TypeError as e:
  print("String immutability error:", e)
 
print("\n--- LIST QUESTIONS ---")
 
# 1. Remove duplicates without using set
lst = [1, 2, 2, 3, 4, 4]
unique = []
for i in lst:
  if i not in unique:
    unique.append(i)
print("Unique list:", unique)
 
# 2. Even numbers using list comprehension
nums = [1, 2, 3, 4, 5, 6]
even_nums = [x for x in nums if x % 2 == 0]
print("Even numbers:", even_nums)
 
# 3. Second largest element
lst = [10, 20, 4, 45, 99]
largest = second = float('-inf')
for n in lst:
  if n > largest:
    second = largest
    largest = n
  elif n > second and n != largest:
    second = n
print("Second largest:", second)
 
# 4. Nested list and sum of each inner list
nested = [[1, 2], [3, 4], [5, 6]]
for inner in nested:
print("Sum:", sum(inner))
 
# 5. Shallow copy and deep copy
import copy
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)
original[0][0] = 99
 
print("Original:", original)
print("Shallow copy:", shallow)
print("Deep copy:", deep)
 
print("\n--- TUPLE QUESTIONS ---")
 
# 1. Maximum and Minimum
t = (10, 5, 25, 3)
print("Maximum:", max(t))
print("Minimum:", min(t))
 
# 2. List of tuples to dictionary
lst = [("a", 1), ("b", 2)]
d = dict(lst)
print("Dictionary:", d)
 
# 3. Count occurrence without built-in methods
t = (1, 2, 3, 2, 2, 4)
count = 0
for i in t:
  if i == 2:
  count += 1
print("Count of 2:", count)
 
# 4. Tuple with mutable elements
t = ([1, 2], [3, 4])
t[0].append(99)
print("Modified tuple:", t)
 
# 5. Swap two tuples
t1 = (1, 2)
t2 = (3, 4)
t1, t2 = t2, t1
print("t1:", t1)
print("t2:", t2)
 
print("\n--- SET QUESTIONS ---")
 
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
 
# 1. Set operations
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Symmetric Difference:", A ^ B)
 
# 2. Remove common elements
common = A & B
A -= common
B -= common
print("A after removal:", A)
print("B after removal:", B)
 
# 3. Subset check
A = {1, 2}
B = {1, 2, 3, 4}
print("Is subset:", A.issubset(B))
 
# 4. Print elements greater than a given number
s = {5, 10, 15, 20}
n = 10
print("Elements greater than", n)
for i in s:
if i > n:
print(i)
 
# 5. List with duplicates → set → list
lst = [1, 2, 2, 3, 4, 4]
unique_list = list(set(lst))
print("Unique list:", unique_list)
