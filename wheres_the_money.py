### 
### Author: Jasur.Jiasuer
### Description:This is a program that prints out  
###             a form about your financial records
###             and their percentages!!! 
import math
from os import _exit as exit
print('-----------------------------')
print('''----- WHERE'S THE MONEY -----''')
print('-----------------------------')
annual_salary = input('What is your annual salary?\n')
if annual_salary.isnumeric() != True or int(annual_salary) < 0 :
    print('Must enter positive integer number.')
    exit(0)
monthly_rent = input('How much is your monthly mortgage/rent?\n')
if monthly_rent.isnumeric() != True or int(monthly_rent) < 0 :
    print('Must enter positive integer number.')
    exit(0)
monthly_bill = input('What do you spend on bills monthly?\n')
if monthly_bill.isnumeric() != True or int(monthly_bill) < 0 :
    print('Must enter positive integer number.')
    exit(0)
food_expenses = input('What are your weekly grocery/food expenses?\n')
if food_expenses.isnumeric() != True or int(food_expenses) < 0 :
    print('Must enter positive integer number.')
    exit(0)
travel = input('How much do you spend on travel annually?\n')
if travel.isnumeric() != True or int(travel) < 0 :
    print('Must enter positive integer number.')
    exit(0)
tax_percentage = input('Tax percentage?\n')
if tax_percentage.isnumeric() != True :
    print('Must enter positive integer number.')
    exit(0)
elif int(tax_percentage) < 0 or int(tax_percentage) >100:
    print('Tax must be between 0% and 100%.')
    exit(0)

annual_salary = int(annual_salary)
monthly_rent = int(monthly_rent)
monthly_bill = int(monthly_bill)
food_expenses = int(food_expenses)
travel = int(travel)
tax_percentage = int(tax_percentage)
rent = monthly_rent*12
bills = monthly_bill*12
food = food_expenses*52
tax = annual_salary * ( tax_percentage / 100.0)
extra = annual_salary - (rent + bills + food + tax + travel)
rent_percentage = (rent/annual_salary)*100
bill_percentage = (bills/annual_salary)*100
food_percentage = (food/annual_salary)*100
travel_percentage = (travel/annual_salary)*100
extra_percentage = (extra/annual_salary)*100
max_percentage = int(max(rent_percentage,bill_percentage,food_percentage,travel_percentage,extra_percentage,tax_percentage))
space_rent = int(rent_percentage)
space_bill = int(bill_percentage)
space_food = int(food_percentage)
space_travel = int(travel_percentage)
space_tax = int(tax_percentage)
space_extra = int(extra_percentage)
print('\n-----------------------------------------'+'-'*max_percentage)
print('See the financial breakdown below, based on a salary of $'+str(annual_salary))
print('-----------------------------------------'+'-'*max_percentage)
print('| mortgage/rent | $'+str(format(rent, '10,'))+' |'+str(format(rent_percentage, '6,.1f'))+'% | '+'#'*space_rent)
print('|         bills | $'+str(format(bills, '10,'))+' |'+str(format(bill_percentage, '6,.1f'))+'% | '+'#'*space_bill)
print('|          food | $'+str(format(food, '10,'))+' |'+str(format(food_percentage, '6,.1f'))+'% | '+'#'*space_food)
print('|        travel | $'+str(format(travel, '10,'))+' |'+str(format(travel_percentage, '6,.1f'))+'% | '+'#'*space_travel)
print('|           tax | $'+str(format(tax, '10,.1f'))+' |'+str(format(tax_percentage, '6,.1f'))+'% | '+'#'*space_tax)
print('|         extra | $'+str(format(extra, '10,.1f'))+' |'+str(format(extra_percentage, '6,.1f'))+'% | '+'#'*space_extra)
print('-----------------------------------------'+'-'*max_percentage)