

import os

def admin_list():
    while True :
        
        print("\n___MENU___")
        print("\n01.Edit admin user name and passwor")
        print("02. Creat a customer")
        print("03. Creat an account")
        print("04. withdraw money")
        print("05. Deposit money")
        print("06. Check balance")
        print("07. Check account history")
        print("08. Update an account ditails")
        print("09. delete an account")
        print("10. Check withdrawal history ")
        print("11. Check deposit history ")
        print("12. Exit\n")

            
        choice =int(input("\nEnter your choice (1 - 10) : "))

        if choice == 1 :
            edit_admin()

        elif choice == 2 :
            creat_customer()
            break
       
        elif choice == 3 :
            account_number()
            break


        elif choice == 12 :
            print("thank you")
            break

#=====================================================================================================
     
#====edit admin user name and password================================================================
     

def edit_admin():
    global admin_uname
    global admin_pword
    new_admin_name =input("Enter your new user name : ")
    new_admin_word =input("enter your new password : ")
    admin_uname = new_admin_name
    admin_pword = new_admin_word

    with open("admin.txt",'w') as file :
        file.write(f"{new_admin_name}\t{new_admin_word}")

#========================================================================================================

# #===============to create new user ==================================================================
     
            
def creat_customer():
    customer_name =input("Enter new customer name : ")
    customer_nic =(input("Enter custemer NIC : "))
    if len(customer_nic) != 12 :
        print("Invalid NIC number!")
        admin_list()
    customer_address =(input("Enter custemer address : "))


    with open("customer.txt",'a') as file :
        file.write(f"{customer_nic}\t{customer_name}\t {customer_address}\n")
    
    admin_list()
#=====================================================================================================

#================= creat account number for customer ======================================================

# import random
# def account_number():
#     nic = input("Enter your NIC: ")
#     found = False
#     line_number = 1

#     file = open("customer.txt", 'r')

#     for line in file:
#         parts = line.split('\t')  # Split line by tab
#         if parts[0] == nic:
#             def account_number():
#     nic = input("Enter your NIC: ").strip()
#     found = False
#     customer_name = ""

#     # Check if NIC exists in customer.txt
#     with open("customer.txt", 'r') as file:
#         for line in file:
#             parts = line.strip().split('\t')
#             if parts[0] == nic:
#                 found = True
#                 customer_name = parts[1].strip()
#                 break

#     if not found:
#         print("NIC not found. Please create a customer first.\n")
#         return

#     # Generate a unique account number
#     account_number = generate_unique_account_number()

#     # Prompt for password
#     account_password = input("Set a password for this account: ").strip()

#     # Save to file
#     with open("account_number.txt", 'a') as f:
#         f.write(f"{account_number}\t{nic}\t{customer_name}\t{account_password}\n")

#     print("\nAccount successfully created!")
#     print(f"Account Number: {account_number}\n")

#             found = True
#             break
#         line_number = line_number + 1

#     file.close()

#     if not found:
#         print("NIC not found.\n")
#=====================================================================================================

# ==================== mjkTo creat a first admin ==============================================================


import os

# Check if the admin file exists, if not, create it with default credentials
if not os.path.exists("admin.txt"):
    with open("admin.txt", 'w') as file:
        file.write("admin1\tadmin10")

# Welcome message
print("\nWelcome to our banking system.\n")

# Get admin credentials from input
admin_name = input("Enter admin user name: ").strip()
admin_word = input("Enter admin password: ").strip()

# Read the stored admin credentials
with open("admin.txt", 'r') as file:
    stored_uname, stored_pword = file.read().strip().split("\t")

# Check if the entered credentials match the stored ones
if admin_name == stored_uname and admin_word == stored_pword:
    print("Admin login successful \n")
else:
    print("Admin not found.\n")

# #=========================================================================================================

#=============================================================================================================

