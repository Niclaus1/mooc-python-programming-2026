# Write your solution here
eat_lunch = int(input('How many times a week do you eat at the studen cafeteria?'))
cost_lunch = float(input('The price of a typical student lunch?'))
spent_groceries = float(input('How much money do you spend on groceries in a week?'))

spent_weekly = (eat_lunch * cost_lunch) + spent_groceries

print()
print('Average food expenditure:')
print(f'Daily: {spent_weekly / 7} euros')
print(f'Weekly: {spent_weekly} euros')