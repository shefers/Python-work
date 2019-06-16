#The purpose of this assignment to teach us how to use input and do simple math by using Python.
#This program would ask the users there name, there organization's name, and the length of cable to be installed, and print out a receipt
#Assignment: 2.1
#Shefers Sarkar
#
print ('Welcome')
Name = input("What is your name?") #Name, is the variable i have used for customer's name
print ("Hi",Name)
companyName = input("What is your, Organization's name?")
num1 = float(input("How Many feets of Fiber optic Cable to be installed:")) #I have used float beacuse of the total coset could be in decimal
num2 =float(0.87)
print() # kept this blank, just for the visual purpose, so the receipt output doesn't show right after customer's input
print("***Receipt***")
print('Organization:',companyName)
print("Customer Name:",Name)
print("Total feet of Fiber Optic Cable to be installed:", num1,"feets")
print("Total Cost of installation: $",format(num1*num2, ",.2f")) #use .2f format spacer to show the cost in legible format.
                                                                 #Though I believe I would learn better way of using format spacer in future.
