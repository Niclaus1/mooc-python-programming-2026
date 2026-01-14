# Write your solution here
hour_wage = float(input('Hourly wage:'))
hour_worked = float(input('Hours worked:'))
day_of_week = input('Day of the week:')

daily_wage = 0
if day_of_week == 'Sunday':
    daily_wage = (hour_wage * hour_worked) * 2
else:
    daily_wage = (hour_wage * hour_worked) 

print(f'Daily wages: {daily_wage} euros')
