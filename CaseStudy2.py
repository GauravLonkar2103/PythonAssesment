import csv
 
FILE_NAME = "attendance.csv"
 
# 1. Create CSV and write attendance data
def create_csv():
  with open(FILE_NAME, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["EmpID", "Name", "Date", "Status"])
    n = int(input("Enter number of employees: "))
    for i in range(n):
      empid = input("Emp ID: ")
      name = input("Name: ")
      date = input("Date (DD-MM-YYYY): ")
      status = input("Status (Present/Absent): ")
      writer.writerow([empid, name, date, status])
  print("Attendance CSV created.\n")
 
 
# 2. Read and display all records
def read_csv():
  with open(FILE_NAME, "r") as f:
    reader = csv.reader(f)
    print("\n--- Attendance Records ---")
    for row in reader:
      print(row)
 
 
# 3. Append new attendance record
def append_record():
with open(FILE_NAME, "a", newline="") as f:
writer = csv.writer(f)
empid = input("Emp ID: ")
name = input("Name: ")
date = input("Date: ")
status = input("Status: ")
writer.writerow([empid, name, date, status])
print("Record appended.\n")
 
 
# 4. Count employees marked Absent
def count_absent():
  count = 0
  with open(FILE_NAME, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
      if row["Status"].lower() == "absent":
        count += 1
  print("Total Absent Employees:", count)
 
 
# 5. Search employee by ID
def search_employee():
search_id = input("Enter Employee ID: ")
found = False
  with open(FILE_NAME, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
      if row["EmpID"] == search_id:
        print("Employee Found:", row)
        found = True
        break
    if not found:
      print("Employee not found.")
 
 
# MENU
while True:
  print("""
  1. Create Attendance CSV
  2. Display Attendance Records
  3. Append Attendance Record
  4. Count Absent Employees
  5. Search Employee by ID
  6. Exit
  """)
  ch = int(input("Enter choice: "))
 
if ch == 1:
  create_csv()
elif ch == 2:
  read_csv()
elif ch == 3:
  append_record()
elif ch == 4:
  count_absent()
elif ch == 5:
  search_employee()
elif ch == 6:
  break
else:
  print("Invalid choice")
