temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
temp_updated = []
for i in temp:
    if i.isdigit():
        num = int(i)
        temp_updated.extend(['"' + f'{num:02d}' + '"'])
    elif i.startswith("+") and i[1:].isdigit():
        num = int(i[1:])
        temp_updated.extend(['"' + f'{i[0]}{num:02d}' + '"'])
    else:
        temp_updated.append(i)
print(*temp_updated)
