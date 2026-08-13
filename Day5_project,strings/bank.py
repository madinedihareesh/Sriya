'''
banking Oprations:
withdraw 
diposite
bal enq


Sign up
Sing in

logout
'''
name=None
username=None
password=None
cpassword=None
Balance=None
while True:
    print('''****Welcome to python Bank****
    1. Sing-up
    2. Sing-in
    3. Logout
''')
    choose=int(input('Enter you choise : '))
    match choose:
        case 1:
            name=input('Enter the name: ')
            username=input('Enter the username: ')
            password= input('Enter the password: ')
            cpassword=input('Enter your password again: ')
            if password==cpassword:
                Balance=int(input('Enter you Balance'))
                print('User regitered Successfull')
            else:
                print('The details you have submitted is wrong!') 
        case 2:
            uname=input('Enter your username: ')
            pword=input('Enter your password: ')
            if username==uname and pword==cpassword:
                while True:
                    print('''****Welcome to the oparations****
                    1. Withdeaw
                    2. Diposite
                    3. Check Bal
                    4. Logout
    ''')           
                    choice=int(input('Enter yout choice:'))
                    match choice:
                        case 1:
                            wamount=int(input('Enter amount to withdraw: '))
                            if wamount>0:
                                if wamount<Balance:
                                    Balance-=wamount
                                    print(wamount,'withdrawal successfull')
                                else:
                                    print('Inffussient funds')
                            else:
                                print('Please enter proper amount')
                        case 2:
                            damount=int(input('Enter  the amount: '))
                            if damount>0:
                                Balance+=damount
                                print('Diposite successfull') 
                            else:
                                print('Enter proper amount')
                        case 3:
                            print('Your current account balance is ',Balance)
                        case 4: 
                            print('Thank you for visiting python Bank')
                            break  ##pass and continue
        case 3:
            print('THnak you for visiting python Bank') 
            break                                                  
