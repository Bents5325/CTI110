# CTI-110
# P4HW2 - Salary Calculator
# Shauntae Bent
# 11/14/22

#Ask for input of employee name, number of hours worked, and pay rate.
#If employee worked overtime, calculate amount owed.
#Calculate amount paid for regular work hours and gross pay.
#Display output with appropriate text and formatting.
#Ask user for another employee name or to terminate.
#Display total number of employee's entered, total overtime
#Total regular pay and total gross.


employeeNum = 0
total_overtime = 0
total_regHour = 0
total_gross = 0

employeeName = input('Enter employee\'s name or "None" to terminate: ')
while employeeName != 'None':
    employeeHours = float(input(f'How many hours did {employeeName} work? '))
    pay_rate = float(input(f'What is {employeeName}\'s pay rate? '))
    if employeeHours > 40:
        overtime = employeeHours - 40
    else:
        overtime = 0
        
    reghour = employeeHours - overtime
    reghour_pay = reghour * pay_rate
    overtime_pay = overtime * 1.5 * pay_rate
    grosspay = overtime_pay + reghour_pay
    
    employeeNum = employeeNum + 1
    total_overtime = total_overtime + overtime_pay
    total_regHour = total_regHour + reghour_pay
    total_gross = total_gross + grosspay

    print()
    print("Employee name:", employeeName)
    print()
    print(f"Hours Worked     Pay Rate     Overtime      OverTime Pay     RegHour Pay     Gross Pay")
    print(f"--------------------------------------------------------------------------------------------")
    print(f"{employeeHours} {pay_rate:>16} {overtime:>11} {overtime_pay:>16.2f} {'$':>11}{reghour_pay:>1.2f} {'$':>10}{grosspay:>1.2f}")
    
    print()
    employeeName = input('Enter employee\'s name or "None" to terminate: ')
    
print()
print('Total number of employees entered:', employeeNum)
print(f'Total amount payed for overtime: ${total_overtime}')
print(f'Total amount payed for regular hours: ${total_regHour}')
print(f'Total amount payed in gross: ${total_gross}')


