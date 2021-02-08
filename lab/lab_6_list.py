# Фролова ИУ7-16Б

from math import*
#проверка на float
def check_float(x):
    znaki = ['1','2','3','4','5','6','7','8','9','-','+','0','e','.']
    line = str(x)
    num = len(line)

    flag = True
    for i in line: #проверка на допустимые знаки 
        if not (i in znaki):
            flag = False
    if flag:
        num_e = 0
        for i in line: #подсчет количества 'e' 
            if i == 'e':
                num_e += 1
        if num_e > 1: #если количество 'e' больше 1, то это строка
            flag = False
        if flag:
            num_t = 0
            for i in line: #подсчет количества '.' внутри строки
                if i == '.':
                    num_t += 1
            if num_t > 1: #если количество '.' больше 1, то это строка
                flag = False
            if num_t==1 and line.find('.')==0:
                flag = False
            if flag: #если в строке есть 'e' делю ее на две, иначе не делю
                #если 'e' в строке нет
                # если строка равна 1
                if len(line) == 1 and (line[0] == '+' or line[0] == '-' or line[0] == '.'):
                    flag = False
                if flag:
                    if num_e == 0: #+ или - только на первом месте
                        for i in range(1,len(line)):
                            if line[i] == '+' or line[i] == '-':
                                flag = False
                    #если 'e' в строке есть
                    elif num_e == 1:
                        if line.index('e') == 0 or line.index('e') == len(line)-1: #если "е" находится на краях строки
                            flag = False
                        if flag:
                            #если длина строки до или после "е" равна 1 и там находятся только символы "+","-","."
                            if (line.index('e') == 1 and (line[0] == '+' or line[0] == '-' or line[0] == '.'))\
                            or (line.index('e') == len(line) - 2 and (line[len(line) - 1] == '+' or line[len(line) - 1] == '-' or line[len(line) - 1] == '.')):
                                flag = False
                            if flag:
                                for i in range (line.index('e')): #проверка числа перед "е"
                                    #знаки "+","-" могут стоять только на первой позиции строки, точка - где угодно
                                    if i != 0 and (line[i] == '+' or line[i] == '-'):
                                        flag = False
                                    if flag:
                                        #в строкe справа от "е" точек быть не может,
                                        #знаки "+","-" могут находится только на первой позиции в строке 
                                        for i in range (line.index('e')+1, len(line)):
                                            if line[i] == '.' or (i>=line.index('e')+2 and(line[i] == '+' or line[i] == '-')):
                                                flag = False
                    else:
                        flag = False         
    return flag

def simple(element_seq): # проверка простое ли число
    mark = True
    for i in range(2,int(sqrt(abs(element_seq)))+1):
         if element_seq%i==0:
             mark = False # флаг
             break
    return mark
    


choice = None # выбор команды
num = 0 #количество нечисловых элементов
#array=list(map(str,[-3,-5,0,-5,-3,-5,-7,-9]))
array=[]
while choice!='0': # меню
    print(
    '''
                               Меню
    1-Проинициализировать список первыми N элементами заданного ряда
    2-Добавить элемент в произвольное место
    3-Удалить произвольный элемент из списка
    4-Очистить список
    5-Найти значение K-го экстремума в списке, если список численный
    6-Найти наиболее длинную убывающую последовательность отрицательных целых
    чисел, модуль которых является простым числом
    7-Найти последовательность, включающую в себя наибольшее количество
    строк, содержащих только гласные буквы
    0-Выход
    ''')
    choice = input('Выбор: ')

    if choice=='0': #выходим из меню
        print('Выход')

    elif choice=='1': # инициализруем список элементами ряда
        # ряд 1-x+x*x-x*x*x+x*x*x*x
        array=[]
        N = int(input('Введите количество N элементов: '))
        x = float(input('Введите значение переменной x: '))
        array_element = 1 # элементы последовательности
        eps = float(input('Введите точность: '))
        for i in range(N):
            if abs(array_element)>eps:
                array.append(str(array_element))
                array_element*=-x
            else:
                array.append('0')
        num = 0
        print('Получившийся список:',*array)

    elif choice=='2': # добавляем элемент в произвольное место
        length = len(array)
        element = input(('Введите значение нового элемента: '))
        if len(array)==0: # когда список пуст
            array.append(element)
        else:
            index = 0
            index = int(input('Введите место вставки элемента: '))
            while index>length:
                print('Введите индекс <=',length,': ',end='')
                index = int(input())
            array.insert(index,element)
        if not check_float(element): # является ли эл-т числом
            num += 1
        print('Получившийся список:',*array)

    elif choice=='3': # удаляем произвольный элемент
        if array==[]: # проверка пуст ли список
            print('Невозможно удалить элемент из списка,список пуст')
        else:
            index = 0
            index = int(input('Введите место удаления элемента: '))
            while index>len(array):
                print('Введите индекс <=',len(array)-1,': ',end='')
                index = int(input())
            element = str(array[index])
            if not check_float(element):#является ли эл-т числом
                num-=1
            del array[index]
            print('Получившийся список:',*array)
         

    elif choice=='4': # очищаем список
        array.clear()
        num = 0
        print('Список пуст')

    elif choice=='5':
        if array==[]: # проверка пуст ли список
            print('Невозможно найти такое значение, список пуст')
        else:
            if num==0: # проверка является ли список численным
                length = len(array)
                current_number = 0
                extremum_number =int(input('Введите номер экстремума: '))
                for i in range(1,length-1): # нахождение экстремумов
                    if (float(array[i-1])<float(array[i]) and float(array[i])>float(array[i+1])) or \
                    (float(array[i-1])>float(array[i]) and float(array[i])<float(array[i+1])):
                        current_number+=1
                    if current_number==extremum_number:
                        print('Значение K-го экстремума в списке = {:.5g} '.format(float(array[i])))
                        break
                if current_number!=extremum_number:
                    print('Невозможно найти такое значение')
            else:
                print('Невозможно найти такое значение, список не численный')

    elif choice=='6': # наиболее длинная убывающая пос-ть
        if len(array) == 0:
            print('Невозможно найти такую последовательность, список пуст')
        else:
            previous = i = count = 0
            sequence_length = [] #длины последовательностей
            first_ind = [] #индексы первых элементов последовательностей
            last_ind = [] #индексы последних элементов последовательностей
            while i != len(array):
                element = (str(array[i]))
                first = i
                #проверка, что элемент-число, целое, простое:
                while check_float(element) and (float(array[i]))<0 \
                and ((float(array[i])) %1==0 or (float(array[i]))%1==0.0) \
                and (int(float(array[i])))!=1 and simple(int(float(array[i]))) and (int(float(array[i]))) < previous:
                    previous = int(float(array[i]))
                    count += 1
                    i += 1
                    if i == len(array):
                        break
                if i != first:
                    last = i
                    if count!=1:
                        sequence_length.append(count)
                        first_ind.append(first)
                        last_ind.append(last)
                    count = 0
                    previous = 0
                    i -= 1
                i += 1
            if not sequence_length:
                print('Искомой последовательности не существует')
            else:
                max_s = sequence_length.index(max(sequence_length))
                print('Искомая последовательность : ', end='')
                print(', '.join(array[first_ind[max_s]:last_ind[max_s]]))
                         
    elif choice=='7':
        length=len(array)
        sequence = [] # максимальная последовательность
        first_ind = 0 # начальный индекс последовательности
        last_ind = 0 # конечный индекс последовательности
        max_length = 0 # максимальная длина последовательности
        current_length = 0 # текущая длина последовательности
        if length==0:
            print('Такой последовательности не существует, список пуст')
        else:   
            for i in range(len(array)):
                element = str(array[i])
                flag = True # проверка удовлетворяет ли эл-т условиям
                for j in range(len(element)):
                    if element[j]!='a' and element[j]!='e' and element[j]!='i' and element[j]!='o' \
                    and element[j]!='u' and element[j]!='y':
                        flag = False
                        break
                if flag: # добавление строки
                    if current_length==0: # начальный индекс последовательности
                        first_ind = i 
                    current_length+=1
                else:
                    if current_length>max_length: # изменение последовательности
                        sequence=array[first_ind:i]
                        max_length = current_length
                    current_length = 0
            if flag:
                if current_length>max_length:
                    sequence=array[first_ind:(i+1)]
            
            if sequence==[]:
                print('Такой последовательности не существует')
            else:    
                print('Искомая последовательность : ',*sequence)
                
    else:
        print('Введённого номера нет')

    
    

