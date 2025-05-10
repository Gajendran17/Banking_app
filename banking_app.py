

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


    with open("customer.txt",'w') as file :
        file.write(f"{customer_nic}\t{customer_name}\t {customer_address}\n")
    
    admin_list()
#=====================================================================================================

#================= creat account number for customer ======================================================

import random

def generate_unique_account_number():
    return str(random.randint(10000000, 99999999))

def account_number():
    nic = input("Enter your NIC: ").strip()
    found = False
    customer_name = ""

    # Check if NIC exists in customer.txt
    with open("customer.txt", 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if parts[0] == nic:
                found = True
                customer_name = parts[1].strip()
                break

    if not found:
        print("NIC not found. Please create a customer first.\n")
        return

    acc_number = generate_unique_account_number()

    # Prompt for password
    account_password = input("Set a password for this account: ").strip()

    # Save to file
    with open("account_number.txt", 'w') as f:
        f.write(f"{acc_number}\t{nic}\t{customer_name}\t{account_password}\n")

    print("\nAccount successfully created!")
    print(f"Account Number: {acc_number}\n")

#=====================================================================================================

# ==================== To creat a first admin ==============================================================

def admin_login():
    import os


    if not os.path.exists("admin.txt") or os.path.getsize("admin.txt") == 0:
        with open("admin.txt", 'w') as file:
            file.write("admin1\tadmin10")


    with open("admin.txt", 'r') as file:
        data = file.read().strip()
        if "\t" in data:
            stored_uname, stored_pword = data.split("\t")
        else:
            print("Admin file is corrupted. Resetting to default credentials.")
            stored_uname = "admin1"
            stored_pword = "admin10"
            with open("admin.txt", 'w') as file:
                file.write(f"{stored_uname}\t{stored_pword}")


    print("\nWelcome to our banking system.\n")


    admin_name = input("Enter admin user name: ").strip()
    admin_word = input("Enter admin password: ").strip()


    with open("admin.txt", 'r') as file:
        stored_uname, stored_pword = file.read().strip().split("\t")


    if admin_name == stored_uname and admin_word == stored_pword:
        print("Admin login successful \n")
        admin_list()

    else:
        print("Admin not found.\n")
        admin_login()


admin_login()


# #=========================================================================================================

#=============================================================================================================

