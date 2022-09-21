#calculates the expenses of a travel budget
#9/14/2022
#CTI-110 P1HW2 - Travel Expense
#Shauntae Bent

#Pseudocode
#input budget
#input location
#input gas
#input hotel
#input food
#Set balance = budget - (gas + hotel + food)
#Display "Destination:", location
#Display "Initial Budget:", budget
#Display "Fuel:", gas
#Display "Accomodation:", hotel
#Display "Food:", food
#Display "Remaining Balace:", balance

print('This program calculates and displays travel expenses')
budget = int(input('Enter your budget: '))
location = input('Where are you headed? ')
gas = int(input('How much do you think you will spend on gas? '))
hotel = int(input('How much will you spend on accomodation/hotel? '))
food = int(input('Finally, how much do you plan to spend on food? '))
print()
balance = budget - (gas + hotel + food)
print('These are your Travel Expenses')
print('Destination:', location)
print('Initial Budget:', budget)
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print('Remaining Balance:', balance)



