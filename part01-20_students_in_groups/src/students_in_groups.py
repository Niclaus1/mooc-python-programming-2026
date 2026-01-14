# Write your solution here
count_student = int(input('How many students on the course?'))
group_size = int(input('Desired group size?'))


group_formed = 0
if count_student < group_size:
    group_formed = 1
elif (count_student / group_size) % 2 != 0:
    group_formed = (count_student / group_size) + 1
else:
    group_formed = (count_student / group_size)
    
print(f'Number of groups formed: {int(group_formed)}')