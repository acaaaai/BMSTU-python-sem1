# Фролова ИУ7-16Б
# метод буля
# метод левых прямоугольников

# функция
def f(x):
    return x+5

# подсчёт интеграла методом левых прямоугольников
def method_left_rect(left_rect_amount, start, end):
    h = (end-start) / left_rect_amount
    current_value = 0
    x = start
    for i in range(left_rect_amount):
        current_value += f(x)
        x += h
    return current_value*h

# подсчёт интеграла методом буля
def method_boole(boole_amount, start, end):
    h = (end-start)/ boole_amount
    value = 0
    x = start
    for i in range(round(boole_amount/4)):
        current_value=0
        current_value += 7 * f(x) + 32 * f(x + h)
        current_value += 12 * f(x + 2 * h)
        current_value += 32 * f(x + 3 * h) + 7 * f(x + 4 * h)
        current_value = current_value *2 / 45
        value += current_value
        x += 4*h
    return (value*h)


# вывод значений интегралов и нахождение отклонений
def integral_output(line,integral1, integral2, integral):
    print(line,'{:15.7f}'.format(integral1), end ='|')
    print('{:15.7f}'.format(integral2),'|')
    delta1 = integral1-integral
    delta2 = integral2-integral
    if delta2>delta1:
        return abs(integral2-integral)
    else:
        return abs(integral1-integral)

# подсчёт количества разбиений и интеграла для неточного метода
def count_inexact_method(number,eps,start,end,integral_f):
    amount_new = 1
    if number == 0:
        integral_new = method_left_rect(amount_new, start, end)
    else:
        integral_new = method_boole(amount_new, start, end)
    while abs(integral_new-integral_f) > eps:
        amount_new *= 2
        if number == 0:
            integral_new = method_left_rect(amount_new, start, end)
        else:
            integral_new = method_boole(amount_new, start, end)
    return amount_new, integral_new

#вывод относительной и абсолютной ошибки
def output_error(s,integral_f, integral1,integral2,amount_first, amount_second):
    abs_f1 = abs(integral_f-integral1)
    otn_f1 = abs((integral_f-integral1)/integral_f)
    abs_f2 = abs(integral_f-integral2)
    otn_f2 = abs((integral_f-integral2)/integral_f)
    print('Метод',s,':\n'
          'Абсолютная ошибка = {0:^9.7f} при {1} разбиениях, '
          '{2:^9.7f} при {3} разбиениях\n'
          'Относительная ошибка = {4:^9.7f} при {1} разбиениях, '
          '{5:^9.7f} при {3} разбиениях\n'
          .format(abs_f1,amount_first,abs_f2,amount_second,otn_f1,otn_f2))
    return 0 
            
        
# ввод данных
start,end = map(float,input('Введите начальное и конечное значения : ').split())
amount_first = int(input('Введите первое количество разбиений: '))
amount_second = int(input('Введите второе количество разбиений: '))
print()

# проверка введённых данных
if amount_first<1 or amount_second<1 or start>=end :
    print("Введены некорректные исходные данные")
else:

    #интеграл f(x)
    integral_f = (end**2) / 2 + 5*end - (start**2) / 2 - 5*start
    print('|  Метод  |    n1 = {}     |    n2 = {}     |'.format(amount_first,amount_second))    
    print('---------------------------------------------')

    # подсчёт интегралов
    integral_left_num1 = method_left_rect(amount_first, start, end)
    integral_left_num2 = method_left_rect(amount_second, start, end)
    integral_boole_num1 = method_boole(amount_first, start, end);
    integral_boole_num2 = method_boole(amount_second, start, end)


    # cписок с отклонениями от интеграла
    deviation = []
    deviation.append(integral_output('|   Буля  |', integral_boole_num1, integral_boole_num2, integral_f ))
    deviation.append(integral_output('|  Лев.пр |', integral_left_num1, integral_left_num2, integral_f))

    # выбор неточного метода и нахождение интеграла с заданной для него точностью
    if deviation[0]>deviation[1]:
        s = 'Буля'
        print('Вычисление интеграла с заданной точность epsilon по методу Буля')
        eps = float(input('Введите точность eps : '))
        amount_eps, integral_eps = count_inexact_method(1,eps,start,end,integral_f)
    else:
        s = 'левыx прямоугольникoв'
        print('\nВычисление интеграла с заданной точность epsilon по методу \n\
левых прямоугольников')
        eps = float(input('Введите точность eps : '))
        amount_eps, integral_eps = count_inexact_method(0,eps,start,end,integral_f)

    print()
    print('Интеграл, вычисленный с точностью {0} равен {1:^10.7f}\n\
Данное значение интеграла вычислено за {2} шагов'.format(eps,integral_eps,amount_eps))
    print('Точное значение интеграла =','{:10.7f}'.format(integral_f))
    print()
    
    abs_error = abs(integral_f - integral_eps)
    otn_error= abs((integral_f - integral_eps)/integral_f)
    print('Метод ',s,' c заданной точностью : \n\
Абсолютная ошибка = {0:.7f} \n\
Относительная ошибка = {1:.7f} \n'.format(abs_error, otn_error))

    # нахождение относительной и аболютной ошибки для всех методов
    s='Буля'
    flag = output_error(s,integral_f,integral_boole_num1 ,integral_boole_num2,amount_first, amount_second)
    print()
    s='левых прямоугольников'
    flag = output_error(s,integral_f,integral_left_num1, integral_left_num2,amount_first, amount_second)

            
        
