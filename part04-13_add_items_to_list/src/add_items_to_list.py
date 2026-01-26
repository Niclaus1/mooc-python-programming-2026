# Write your solution here
items = int(input('How many items:'))
list = []
count = 0

while count < items:
    item = int(input(f'Item {count + 1}:'))
    list.append(item)
    count += 1
print(list)