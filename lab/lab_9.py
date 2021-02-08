#Фролова иу7-16б
# лаб9

choice = None # выбор команды
string = ''
key = ''
new_string = ''
while choice!='0': # меню
    print(
    '''
                               Меню
    1-Ввод строки
    2-Настройка шифрующего алгоритма
    3-Шифрование строки, используя шифр Виженера
    4-Расшифровывание строки
    ''')
    choice = input('Выбор: ')
    if choice=='0': 
        print('Выход')

    elif choice=='1':
        string = input('Введите строку: ')
        string_number = [] # коды символов слова
        for i in range(len(string)):
            string_number.append(ord(string[i]))
            
    elif choice=='2':
        key = input('Введите ключ шифра: ')
        key_number = [] # сдвиги символов
        for i in range(len(key)):
            key_number.append(ord(key[i]))
        
    elif choice=='3':
        if len(key)==0 or len(string)==0:
            print('Невозможно зашифровать')
        else:
            new_string =''
            # находим новый код символа
            for i in range(len(string)):
                    current = chr((string_number[i]+key_number[i%len(key)]+1)%1104)
                    new_string +=current
                    #print(string_number[i]+key_number[i%len(key)]+1)%1104)
            new_string_number = []
            for i in range(len(new_string)):
                new_string_number.append(ord(new_string[i]))
            print('Закодированная строка:',new_string)
            

    elif choice=='4':
        if len(new_string)==0:
            print('Невозможно расшифровать')
        else:
            decryp = ''
            # находим старый код символа
            for i in range(len(new_string)):
                if key_number[i%len(key)]>new_string_number[i]:
                    current = chr(1104-(key_number[i%len(key)]-(new_string_number[i]-1)))
                    decryp += current
                else:
                    current = chr(new_string_number[i]-1-key_number[i%len(key)])
                    decryp += current
            print('Расшифрованная строка:',decryp)
          
    else:
        print('Введённого номера нет')




