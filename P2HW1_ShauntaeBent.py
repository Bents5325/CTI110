#calculates the expenses of a travel budget
#9/21/2022
#CTI-110 P1HW2 - Travel Expense
#Shauntae Bent

#Pseudocode
#input variables budget, location, gas, hotel, food
#Set balance = budget - (gas + hotel + food)
#Display "Destination:", location
#Display "Initial Budget:", budget
#Display "Fuel:", gas
#Display "Accomodation:", hotel
#Display "Food:", food
#Display "Remaining Balace:", balance

print('This program calculates and displays travel expenses\n')
budget = float(input('Enter your budget: '))
print()
location = input('Enter your travel destination: ')
print()
gas = float(input('How much do you think you will spend on gas? '))
print()
hotel = float(input('How much will you spend on accomodation/hotel? '))
print()
food = float(input('Finally, how much do you plan to spend on food? '))
print()

balance = budget - (gas + hotel + food)

print('These are your Travel Expenses')
print(f'Destination:             {location}')
print(f'Initial Budget:          ${budget}')
print(f'Fuel:                    ${gas}')
print(f'Accomodation:            ${hotel}')
print(f'Food:                    ${food}')
print()
print(f'Remaining Balance:       ${balance}')



