# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 13:04:54 2022

@author: anand
"""

# bank management system
import random

l1 = []
l2 = []
balance = 0
account_no = 0
otp = 0
verify = 0
start_amount = 0


def account_open():
    global account_no
    global start_amount
    global balance
    h_name = input('Enter account holder name: ')
    l1.append(h_name)
    h_address = input('Enter account holder address: ')
    l1.append(h_address)
    h_email = input('Enter account holder email_id: ')
    l1.append(h_email)
    h_mob = input('Enter account holder Mobile name: ')
    l1.append(h_mob)
    a_type = input('Enter account type c or s: ')
    l1.append(a_type)
    start_amount = int(input('Enter Starting Amount>=3000:'))
    if start_amount >= 3000:
        balance = balance + start_amount
        print('Welcome to Python Bank')
        account_no = ''.join([str(random.randint(0, 9)) for i in range(12)])
        print('your account number is:', account_no)
    else:
        print("Error: Can't Open Account")
        print('Deposit Amount: 3000 or greater')
        l1.clear()




def deposit():
    if l1 == []:
        print('Error: No Account Found')
    else:
        global balance
        dp = int(input('Enter amount:'))
        balance = balance + dp
        l2.append(dp)
        l2.append('cr')
        print('Amount Deposited successfully')


def withdrawl():
    global balance
    global otp
    global verify
    if l1 == []:
        print('Error: No Account Found')
    else:
        otp = ''.join([str(random.randint(0, 9)) for i in range(4)])
        print('Your otp is:', otp)
        verify = input('Enter OTP:')
        if verify == otp:
            wd = int(input('Enter amount:'))
            if wd > 20000 and l1[4] == 's':
                print("Error: Can't Withdraw amount")
                print("You have Saving Account")
                print("Withdraw amount should be less than 20000")
            else:
                if wd < balance:
                    balance = balance - wd
                    l2.append(wd)
                    print('Amount withdraw successfully')
                else:
                    print('Insufficient Balance')
        else:
            print('Invalid OTP')


def balance_check():
    global balance
    if l1 == []:
        print('Error: No Account Found')
    else:
        if balance > 0:
            print('Current balance is:', balance)
        else:
            print('Insufficient Balance')


def holder_details():
    global account_no
    if l1 == []:
        print('Error: Account Not Found')
    else:
        print('Account Holder Name is:', l1[0])
        print('Account Holder address:', l1[1])
        print('Account Holder email', l1[2])
        print('Account Holder mobile', l1[3])
        print('Account type is:', l1[4])
        print('Account No. is:', account_no)


def mini_st():
    if l2 == []:
        print('Insufficient balance')
    else:
        print(l2)


def main():
    print('********Anand BANK*********')
    print('1. Account Opening')
    print('2. Deposit Amount')
    print('3. Amount Withdrawl')
    print('4. Balance Enquiry')
    print('5. Account Holder')
    print('6. Mini Statement')
    choice = int(input('Enter a choice:'))
    if choice == 1:
        account_open()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdrawl()
    elif choice == 4:
        balance_check()
    elif choice == 5:
        holder_details()
    elif choice == 6:
        mini_st()
    else:
        print('ERROR : Invalid choice')
    main()


main()

