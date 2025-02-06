a = input()
p =0
v = 0
for i in range(6):
    if i>2:
        p+=int(a[i])
    else:
        v+=int(a[i])
if p==v:
    print('Счастливый')
else:
    print('Обычный')