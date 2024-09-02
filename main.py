x = int(input('Здравствуйте пользователь, прошу запишите 3 целых числа: '))
z = int(input(': '))
y = int(input(': '))
#без or сделать
if x==z!=y or z==y!=x or x==y!=z:
    print('Есть пара одинаковых чисел')
elif int(x==z==y):
    print('Все  числа равны')
else:
    print('ни одно из чисел не равно другому')
#print(x,y,z)