''' Type your code here. '''
miles_per_gallon = float(input())
cost_per_gallon = float(input())

cost_20 = (20 / miles_per_gallon) * cost_per_gallon
cost_75 = (75 / miles_per_gallon) * cost_per_gallon
cost_500 = (500 / miles_per_gallon) * cost_per_gallon

print(f'{cost_20:.2f} {cost_75:.2f} {cost_500:.2f}')