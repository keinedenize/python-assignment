#1.The volume of a sphere with radius r is (4/3)* pie * r**2
#What is the volume of the sphere with radius 5
#Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places
# SOLUTION
radius= int(input("Enter the radius of the sphere:"))
pie= 3.14
volume=(4/3)*pie*radius**2
print(f"The volume of the sphere with{radius} is: {volume:.2f}")


#2. Create a program to calculate the area of a triangle (1/2 * base * height).
#Base and height should be entered using the keyboard.
base = int(input("Enter base:"))
height = int(input("Enter height:"))
area = 1/2* base * height
print(f"The area of a triangle is {area}")


#3. Witi has asked you to automate a simple grading system.
#As a python student, write a program using to display the grades that 
# the students will be receiving based on the mark scored in a subject.
# the grades are :
# 90%-100% Grade is A
# 80%-89% Grade is B
# 70%-79% Grade is C 
# 60%-69% Grade is D 
# 50&-59% Grade s E 
# < 50% Fail.
marks = int(input("Enter the marks"))
if marks >=90 and marks<=100:
    print("Grade is A")
elif marks >=80 and marks <=89:
    print("Grade is B")
elif marks >=70 and marks <=79:
    print("Grade is C ") 
elif marks >=60 and marks <=69:
    print("Grade is D")
elif marks >=50 and marks <=59:
    print("Grade is E")
else: 
    print("Fail")
                   
#4. Witi Academy is proposing a Sacco to help students save their money .
# Desighn a plantform that will do the following.
# Welcome to, WITI Academy SACCO
#1. Despoit Money
#2. Withdraw Money
#3. Check balance
# Ensure if the student selects 1, money is deposited and the mininum deposit should be 1000.
# If the student selects 2, money should be withdrawn and a minimum withdraw is 500.
# If the student selects 3, the account balance should be displayed.
account_balance = 0  
print("Welcome to, WITI Academy SACCO")
print("1. Deposit money")
print("2. Withdraw money")   
print("3. Check balance") x
student_option = int(input("Enter the selection(1,2,3):"))
if student_option ==1:
    deposit_amount = int(input("Enter amount to be deposited: "))
    if deposit_amount < 1000:
        print("minimum deposit is 1000")
    else:
     account_balance += deposit_amount
     print(f'Dear student you have deposited {deposit_amount:,} and your new account balance is {account_balance:,}')
                
elif student_option ==2:
    withdraw_amount = int(input("Enter amount to be withdrawn:"))
    if account_balance ==0:
       print("Your balance is 0")
    elif withdraw_amount < 500:
       print("Minimum withdraw should be more than 500")
    elif withdraw_amount > account_balance:
       print(f' Withdraw failed insufficient funds')
    else: 
       account_balance -= withdraw_amount 
       print(f"Dear student you have withdrawn {withdraw_amount:,} and your new account balance is {account_balance:,} ")
    
            
elif student_option ==3:
    print(f'Your account_balance is{account_balance:,}')
else:
    print("You entered a wrong choice!! Please select 1,2 or 3") 
    

    
              