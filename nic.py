# name =input("name pls : ")
# age =input("age pls : ")
# address =input("address pls : ")
# nic =input("nic pls : ")

# with open("data.txt",'w') as file:
#     file.write(f"{name}\t{age}\t{address}\t{nic}")
    

# # Read each line into a list
# with open("data.txt",'r') as file:
#     data_list = [line.strip() for line in file]

# print(data_list[0])

# in_nic = input("enter ur nic : ")
# found = any(row[3] == in_nic for row in data_list)

# if found:
#     print("hii da")
# else:
#     print("NIC not found.")

# with open("customer.txt",'r') as file :
#     name = file.read()
 

#  nic =input("enter your nic : ")
#  if nic in name :
#     print("fine")
# else :
#     print("gajan")

# nic = input("Enter your NIC: ")

# found = False

# nic = input("Enter your NIC: ")
# found = False
# line_number = 1  # Start counting from line 1

nic = input("Enter your NIC: ")
found = False
line_number = 1

file = open("customer.txt", 'r')

for line in file:
    parts = line.split('\t')  # Split line by tab
    if parts[0] == nic:
        print("NIC found at line", line_number)
        print("Details:", line.strip[1])
        found = True
        break
    line_number = line_number + 1

file.close()

if not found:
    print("NIC not found.")

