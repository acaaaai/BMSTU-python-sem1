# Фролова В.С. ИУ7-16Б
# Вычислить таблицу значений функций
# f1 = x**3-14.5*(x**2)+60.7*x-71
# f2 = x-1.4**x
# f3 = f1+f2

minx,step,maxx = map(float,input('Введите начальное значение x, шаг, конечное значение: ').split())
print('-----------------------------------------------------')
print('|     x      |     f1     |     f2     |     f3     |')
print('-----------------------------------------------------')
a = [] # массив с значениями f1
x = minx 
while x <= maxx: # запись значений в таблицу
    f1 = x**3-14.5*x*x+60.7*x-71
    a.append(f1)
    f2 = x-1.4**x
    f3 = f1+f2
    print('|{:^12.5g}|{:^12.4g}|{:^12.4g}|{:^12.4g}|'.format(x,f1,f2,f3))
    print('-----------------------------------------------------')
    x+=step

kolvot = int(input('Введите количество засечек, от 4 до 8:'))
top = max(a)
down = min(a)
y = down # значение первой засечки
div = (top-down)/(kolvot-1) # равномерная разность засечек
print('         ',end='')
n=85//(kolvot-1)
for i in range(kolvot-1):
    print('{:<12.4g}'.format(y), end ='')
    print(' '*(n-12),end='')
    y += div
print('{:<12.4g}'.format(y), end ='')
print('y')
print('          ',end='')
for i in range(kolvot-1):
    print('|',end='')
    probel =(n-1)*'-' 
    print(probel, end='')
print('|----------->')# вывод оси оу

ch1=' '
div = (top-down)/(85)# вес 1 пробела
ox1 = 0
ox2 = 0
for i in range(len(a)): # проверка отрицательных значений f1
    if a[i]<0:
        ox1 = 1
        break
for i in range(len(a)): # проверка положительных значений f1
    if a[i]>0:
        ox2 = 1
        break

x = minx    
spacex1 = round((0-down)/div)+1 # кол-во пробелов для ох
if ox1==1 and ox2==1:   # вывод таблицы, если пересекает ох   
    for i in range(len(a)):
        space = round((a[i]-down)/div)+1 # кол-во пробелов для *
        probels = ch1*(space-1) # кол-во пробелов до *
        probelx1 = ch1*(spacex1-space-1) # кол-во пробелов до |
        probelx = ch1*(spacex1-1) # кол-во пробелов до |
        probels1 = ch1*(space-spacex1-1)  # кол-во пробелов до *
        if space==spacex1:
            print('{:>8.3g}'.format(x),'.',end='')
            print(probels,end='')
            print('*')
        elif a[i]<=0:
            print('{:>8.3g}'.format(x),'.',end='')
            print(probels,end='')
            print('*',end='')
            print(probelx1,end='')
            print('|')
        elif a[i]>0:
            print('{:>8.3g}'.format(x),'.',end='')
            print(probelx,end='')
            print('|',end='')
            print(probels1,end='')
            print('*')
        x+=step
    if spacex1==1:# если оx на 1 месте
        probelx = ch1*(spacex1-3)+ch1*9
        print(probelx,end='')
        print('x|')
    else:
        probelx = ch1*(spacex1-2)+ch1*10
        print(probelx,end='')
        print('x|')
    probelo = ch1*(spacex1-1)+ch1*10 #кол-во пробелов для оси
    print(probelo,end='')
    print('˅')
else:                   # вывод таблицы, если не пересекает ох
    for i in range(len(a)):
        space = round((a[i]-down)/div)+1
        probels = ch1*(space-1)
        print('{:>8.3g}'.format(x),'.',end='')
        print(probels,end='')
        print('*')
        x+=step

raznost = top-down
print('Разность между максимальным и минимальным значениями f1 = {:.5g}'.format(raznost))



             

    
