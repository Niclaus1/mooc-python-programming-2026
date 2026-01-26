# Write your solution here
list = []
count = 0
while True:
    print(f'The list is now {list}')            
    menu = input('a(d)d, (r)emove or e(x)it:')

    if menu.lower() == 'd':
        count += 1
        list.append(count)
        
    elif menu.lower() == 'r':
        if len(list) > 0:
            list.pop()
            count -= 1
        else:
            continue
        
    elif menu.lower() == 'x':
        print('Bye!')
        break