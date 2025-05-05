
# #     account_num =(f"{customer_nic[5:12]}{account_auto_num}")
# #     account_auto_num += 1
# #     print(account_auto_num)
# #     #=====================================

    
# #     with open("account.txt",'a') as file :
    
# #     # with open("admin.txt",'r') as file :
# # #     new = file.read()

# # # admin_id =input ("Enter your user ID to continue : ")
# # # admin_pword =input ("Enter your password  : ") 

# # admin_uname = "admin1"
# # admin_pword = "admin10"

# import random

# def generate_random_account_number(length=10):
#     return ''.join(str(random.randint(0, 9)) for _ in range(length))

# # Example usage
# print(generate_random_account_number())  # e.g., 4829301283

import random

def generate_account_number(length=10):
    # Ensure the account number is a string of digits
    account_number = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return account_number

# Example usage
account_number = generate_account_number()
print(f"Generated Account Number: {account_number}")
