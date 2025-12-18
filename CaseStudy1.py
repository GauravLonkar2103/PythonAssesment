FILE_NAME = "students.txt"
 
# 1. Create file and write student records
def create_and_write():
 n = int(input("Enter number of students: "))
 with open(FILE_NAME, "w") as f:
   for i in range(n):
     name = input("Enter name: ")
     roll = input("Enter roll no: ")
     marks = input("Enter marks: ")
     f.write(f"{name},{roll},{marks}\n")
 print("Student records written successfully.\n")
 
 
# 2. Read and display all records
def read_and_display():
 try:
   with open(FILE_NAME, "r") as f:
     print("\n--- Student Records ---")
     for line in f:
       name, roll, marks = line.strip().split(",")
       print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
except FileNotFoundError:
  print("File not found.\n")
 
 
# 3. Append a new student record
def append_record():
 with open(FILE_NAME, "a") as f:
   name = input("Enter name: ")
   roll = input("Enter roll no: ")
   marks = input("Enter marks: ")
   f.write(f"{name},{roll},{marks}\n")
 print("Student record appended successfully.\n")
 
 
# 4. Count total number of records
def count_records():
 try:
   with open(FILE_NAME, "r") as f:
     count = len(f.readlines())
   print("Total number of student records:", count)
 except FileNotFoundError:
   print("File not found.\n")
   
 
# 5. Search for a student by name
def search_student():
 search_name = input("Enter student name to search: ")
 found = False
 try:
   with open(FILE_NAME, "r") as f:
     for line in f:
     name, roll, marks = line.strip().split(",")
     if name.lower() == search_name.lower():
       print(f"Record Found → Name: {name}, Roll: {roll}, Marks: {marks}")
       found = True
       break
     if not found:
     print("Student not found.")
 except FileNotFoundError:
   print("File not found.\n")
 
 
# -------- MENU --------
while True:
 print("""
1. Create & Write Student Records
2. Read & Display Records
3. Append Student Record
4. Count Student Records
5. Search Student by Name
6. Exit
""")
 choice = int(input("Enter choice: "))
 
 if choice == 1:
   create_and_write()
 elif choice == 2:
   read_and_display()
 elif choice == 3:
   append_record()
 elif choice == 4:
   count_records()
 elif choice == 5:
   search_student()
 elif choice == 6:
   print("Exiting program.")
   break
 else:
   print("Invalid choice.")
 
