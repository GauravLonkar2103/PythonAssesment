import csv
 
TXT_FILE = "sales.txt"
CSV_FILE = "sales.csv"
 
# 1. Create sales.txt and store sales
def create_sales_txt():
  n = int(input("Enter number of sales records: "))
  with open(TXT_FILE, "w") as f:
    for i in range(n):
      date = input("Date: ")
      product = input("Product: ")
      amount = float(input("Amount: "))
      f.write(f"{date},{product},{amount}\n")
  print("sales.txt created.\n")
 
 
# 2. Append sales data
def append_sales():
  with open(TXT_FILE, "a") as f:
    date = input("Date: ")
    product = input("Product: ")
    amount = float(input("Amount: "))
    f.write(f"{date},{product},{amount}\n")
  print("Sales data appended.\n")
 
 
# 3. Convert sales.txt to sales.csv
def convert_to_csv():
  with open(TXT_FILE, "r") as txt, open(CSV_FILE, "w", newline="") as csvf:
    writer = csv.writer(csvf)
    writer.writerow(["Date", "Product", "Amount"])
    for line in txt:
      writer.writerow(line.strip().split(","))
  print("Converted to sales.csv\n")
 
 
# 4. Read and display sales.csv
def read_csv():
with open(CSV_FILE, "r") as f:
reader = csv.reader(f)
print("\n--- Sales Records ---")
for row in reader:
print(row)
 
 
# 5. Calculate total sales
def total_sales():
  total = 0
  with open(CSV_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
      total += float(row["Amount"])
  print("Total Sales Amount:", total)
 
 
# MENU
while True:
  print("""
  1. Create sales.txt
  2. Append sales data
  3. Convert sales.txt to sales.csv
  4. Display sales.csv
  5. Calculate total sales
  6. Exit
  """)
  ch = int(input("Enter choice: "))
 
if ch == 1:
  create_sales_txt()
elif ch == 2:
  append_sales()
elif ch == 3:
  convert_to_csv()
elif ch == 4:
  read_csv()
elif ch == 5:
  total_sales()
elif ch == 6:
  break
else:
  print("Invalid choice")
