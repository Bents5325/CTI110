#CTI-110
#P2HW2 - List
#Shauntae Bent
#10/5/2022

#Pseudocode
#Input 6 module grade variables.
#Store the variables in a list
#Display the lowest grade, highest grade, sum, and average
#Format the results to be nicely aligned

module1 = float(input('Enter Grade for Module 1: '))
module2 = float(input('Enter Grade for Module 2: '))
module3 = float(input('Enter Grade for Module 3: '))
module4 = float(input('Enter Grade for Module 4: '))
module5 = float(input('Enter Grade for Module 5: '))
module6 = float(input('Enter Grade for Module 6: '))

module_grades = [module1, module2, module3, module4, module5, module6]

print()
print('             Results')
print(f'Lowest Grade:         {min(module_grades)}')
print(f'Highest Grade:        {max(module_grades)}')
print(f'Sum of Grades:        {sum(module_grades)}')
print(f'Average:              {sum(module_grades)/len(module_grades):.2f}')
