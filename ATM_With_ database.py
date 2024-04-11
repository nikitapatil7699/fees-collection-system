import sqlite3


conn = sqlite3.connect("ATM.db")
print("Connection is created")

with conn:
    atm = conn.cursor()

    # atm.execute("create Table ATM_Account(id int primary key, Name varchar(30), Balance int)")
    # print("Table is Created..")

    # conn.commit()
  

    # Balance = 5000
    while True:

        
        # Balance = 5000
        User_Choice =int(input('''
        ⭐⭐⭐ Enter Your Choice ⭐⭐⭐
    1 Create Account
    2 Deposite
    3 Withdraw
    4 Check Balance
    5 Exit
                            '''))
        
        if User_Choice == 1:
            id = int(input("Enter Your Id : "))
            Name = input("Enter Your Name :")
            Address = input("Enter Your Address :")
            umobile = int(input("Enter Your Mobile Number :"))
            Balance = int(input("Add Balance :"))

            atm.execute("insert into ATM_Account(id, Name, Balance ) values(?,?,?)", (id, Name, Balance))
            conn.commit()
            # conn.close()

            print("Account Create....".center(60,"_"))
            conn.commit()
        elif User_Choice == 2:
            id = int(input("Enter Your Id : "))
            Deposite = int(input("Enter Amount To Deposite :"))
                        
            atm.execute("select Balance from ATM_Account where id = ?",(id,))
            bal = atm.fetchone()
            print("Availale Balance :", Balance)

            if bal: 
                bal = bal[0]
               
                New_Balance = bal + Deposite
                print("New Balance is = ", New_Balance)

                atm.execute("Update ATM_Account set Balance = ? where id = ? ", (New_Balance, id))
                conn.commit()

        elif User_Choice == 3:
            id = int(input("Enter Your Id : "))
            withdraw = int(input("Enter Amount to Withdraw :"))
            
            atm.execute("select Balance from ATM_Account where id = ?", (id,))
            bal = atm.fetchone()
            print("Availale Balance :", bal)

            if bal: 
                bal = bal[0]
                
                if bal >= withdraw:
                    New_Balance = bal - withdraw
                    print("New Balance is = ", New_Balance)

                    atm.execute("Update ATM_Account set Balance = ? where id = ? ", (New_Balance, id))
                    conn.commit()
            else:
                print("Invalid Id.")

        elif User_Choice == 4:
            # Balance = Balance

            print("Total Balance : ",Balance)
        else:
            print("Thank You🙏🙏🙏")
            break
atm.close()
conn.close()























# import sqlite3

# conn = sqlite3.connect("ATM_db.db")
# print("Connection is created")

# atm = conn.cursor()

# # atm.execute("create Table ATM_Account(id int primary key, Name varchar(30), Balance int)")
# print("Table is Created..")

# # Initialize Balance outside the loop
# Balance = 0

# while True:
#     User_Choice = int(input('''
#     ⭐⭐⭐ Enter Your Choice ⭐⭐⭐
# 1 Create Account
# 2 Deposit
# 3 Withdraw
# 4 Check Balance
# 5 Exit
#                            '''))

#     if User_Choice == 1:
#         id = int(input("Enter Your Id : "))
#         Name = input("Enter Your Name :")
#         Address = input("Enter Your Address :")
#         umobile = int(input("Enter Your Mobile Number :"))
#         Balance = int(input("Add Balance :"))

#         atm.execute("insert into ATM_Account(id, Name, Balance) values(?,?,?)", (id, Name, Balance))
#         conn.commit()
#         print("Account Created....".center(60, "_"))

#     elif User_Choice == 2:
#         deposit = int(input("Enter Amount To Deposit :"))
#         Balance += deposit
#         print("Available Balance:", Balance)

#     elif User_Choice == 3:
#         withdraw = int(input("Enter Amount to Withdraw :"))
#         if withdraw > Balance:
#             print("Insufficient funds!")
#         else:
#             Balance -= withdraw
#             print("Available Balance:", Balance)

#     elif User_Choice == 4:
#         print("Total Balance:", Balance)

#     elif User_Choice == 5:
#         print("Exiting...")
#         break

# # Close the cursor and connection after the loop is finished
# atm.close()
# conn.close()

