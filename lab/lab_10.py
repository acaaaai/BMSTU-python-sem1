#счетчик выражений
def count(current):
                        seq = []
                        seq2=[]
                        for k in range(len(current)):
                            if current[k] =='*' or current[k] =='/' :
                                seq.append(current[k])
                            if current[k]=='+' or current[k]=='-':
                                seq2.append(current[k])
                        # cчитаем все * и /
                        for g in range(len(seq)):
                                index = current.find(seq[g])
                                before = index-1
                                while (current[before].isdigit() or current[before]=='.')\
                                      and before>-1:
                                    before-=1
                                after = index+1
                                while after<len(current) and (current[after]=='.'\
                                      or  current[after].isdigit()):
                                    after+=1
                                before_number=current[(before+1):index]
                                after_number = current[(index+1):after]
                                if seq[g]=='/':
                                    part = float(before_number)/float(after_number)
                                elif seq[g]=='*':
                                    part = float(before_number)*float(after_number)
                                current = current[:(before+1)]+str(part)+current[after:]
                        # считаем все + и -
                        for g in range(len(seq2)):
                                index = current.find(seq2[g])
                                before = index-1
                                while (current[before].isdigit() or current[before]=='.')\
                                      and before>-1:
                                    before-=1
                                after = index+1
                                while after<len(current) and (current[after]=='.'\
                                      or  current[after].isdigit()):
                                    after+=1
                                before_number=current[(before+1):index]
                                after_number = current[(index+1):after]    
                                if seq2[g]=='+':
                                    part = float(before_number)+float(after_number)
                                elif seq2[g]=='-':
                                    part = float(before_number)-float(after_number)
                                current = current[:(before+1)]+str(part)+current[after:]
                        return(current)




choice = None # выбор команды
text = ['Анна не не ответила. Кондуктор и входившие (38-10+45-3)*3+8/2 не и заметили под вуалем',\
'ужаса на ее лице. Она вернулась в свой она угол угол',\
'и села. Чета села с противоположной стороны, внимательно, но',\
'скрытно оглядывая ее (49+35-15)/5+(15-5)*3 платье внимательно. И муж и жена',\
'казались Анне отвратительны Анне. Муж спросил: позволит',\
'ли',\
'она курить, очевидно девушку девушку не для того, чтобы курить, но чтобы заговорить с нею нею нею.']
##text = ['      На другой день поехал князь Андрей поехал 35+57-3*(96-39)/5 с визитами в некоторые дома, где он',\
##'еще не был. И в он том 45*9-33*(8-5) числе к Ростовым, с которыми он возобновил  знакомство',\
##'на последнем бале. Кроме законов учтивости, по которым ему нужно было быть',\
##'у Ростовых. Князю Андрею хотелось 48*9-35 Андрею видеть дома эту особенную, оживленную',\
##'девушку, которая оставила девушку ему приятное воспоминание.']
while choice!='0': # меню
    print(
    '''
                               Меню
    0-Выход
    1-Выравнивание текста по левому краю
    2-Выравнивание текста по правому краю
    3-Выравнивание текста по ширине
    4-Удаление заданного слова
    5-Замена одного слова другим во всем тексте
    6-Вычисление арифметического выражения
    7-Найти наиболее часто встречающееся слово'''\
    'в каждом предложении')

    choice = input('Выбор: ')
    length = len(text)

    # ищем строку наибольшей длины
    max_length = 0
    for i in range(length):
        text[i] = text[i].strip()
        if len(text[i])>max_length:
            max_length = len(text[i])

    if choice=='0': 
        print('Выход')

    elif choice=='1':
        for element in text:
            current = element.lstrip()            
            print(current)

    elif choice=='2':                              
        # выводим текст с нужным количеством пробелов
        for element in text:
            current = element.rstrip()
            space = ' '* (max_length-len(current))
            print(space,end='')
            print(current)

    elif choice == '3':             

        for element in text:
            # поиск количества пробелов в строке
            count_space = 0
            for j in range(len(element)):
                if element[j] == ' ':
                    count_space += 1
            # не хватает пробелов до макс строки
            remain = max_length-len(element)

            if count_space==0:
                need_space = 0
            else:
                # необходимое количество пробелов
                need_space = (remain// count_space)
                # остаток пробелов
                last_space = remain % count_space
            current_space = 0
            # количество пробелов для каждой строки
            for j in range(len(element)):
                if element[j]==' ':
                    current_space += 1
                    if current_space == count_space:
                        string = ' '*(need_space+last_space)
                    else:
                        string = ' '*(need_space)
                    print(string,end='')
                    print(element[j],end='')    

                else:
                    print(element[j],end='')
            print()

    elif choice == '4':                                                  
        word = input('Введите удаляемое слово: ')
        check = False
        number=0
        for element in text:
            element = ' ' + element + ' '
            # количество слов
            count_word = element.count(word)
            for k in range(count_word):
                if word in element:
                    i = element.find(word)-1
                    j = element.find(word)+len(word)
                    if element[i]==' ' and \
                      (element[j] == ' ' or \
                       element[j] == '.' or \
                       element[j] == ','):
                        check = True
                        element = (element[:i] + element[j:])
                    else:
                        element = element[:i+1]+'#'*len(word)+element[j:]
            element = element.replace('#'*len(word),word)
            element = element.strip()
            text[number] = element
            number+=1
            print(element)
        if not check:
            print()
            print('Данного слова нет в тексте')
                    
            
    elif choice == '5':                                          
        word = input('Введите заменяемое слово: ')
        replace = input('Введите заменяющее слово: ')
        check = False
        number = 0
        for element in text:
            element = ' ' + element + ' '
            #количество слов
            count_word = element.count(word)
            for i in range(count_word):
                if word in element:
                    i = element.find(word)-1
                    j = element.find(word)+len(word)
                    if element[i]==' ' and \
                       (element[j] == ' ' or \
                        element[j] == '.' or \
                        element[j] == ','):
                        check = True
                        element = (element[:(i+1)]+replace +element[j:])
                    else:
                        element = (element[:i+1]+'#'*len(word)+element[j:])
            element = element.replace('#'*len(word),word)
            element = element.strip()
            text[number] = element
            number+=1    
            print(element)
        if not check:
            print()
            print('Заменяемого слова нет в тексте')
                        
    elif choice == '6':
        signs = ['*','/','+','-']
        n= -1
        for element in text:
            n  +=1
            i = 0
            while i < len(element):
                if element[i].isdigit() or element[i]=='(' or element[i]==')':
                    j = i
                    while i<len(element)and element[i] !=' ':
                        i += 1
                    current = element[j:i]
                    flag = False
                    seq = []
                    seq2=[]
                    seq3 = []
                    # проверяем есть ли выражения
                    for h in range(len(current)):
                        if current[h] in signs:
                            flag = True
                            break
                    if flag:
                            first = 0
                            while first!=-1:
                                first = current.find('(')
                                finish = current.find(')')
                                if first!=-1:
                                    now = current[(first+1):finish]
                                    now=count(now)
                                    current = current[:first]+str(now)+current[finish+1:]
                            current = count(current)     
                            element = element[:j]+str(current)+element[i:]
                i+=1
            text[n]=element
            print(text[n])
                    
    elif choice == '7':                                                        
        all_words = []
        count_words = []
        calculator = 0
        for element in text:
            j = 0
            i=0
            while i<len(element):
                if element[i]==' ' or element[i] ==',' :
                    word = element[j:i]
                    if word not in all_words:
                        all_words.append(word)
                        count_words.append(0)
                    index = all_words.index(word)
                    count_words[index] += 1
                    if element[i]==' ':
                        j = i+1
                    else:
                        j = i+2
                        i+=1                
                elif element[i] =='.' and (not element[i-1].isdigit()):
                    calculator += 1
                    word = element[j:i]
                    if word not in all_words:
                        all_words.append(word)
                        count_words.append(0)
                    count_words[all_words.index(word)] += 1
                    print('Наиболее часто встречающееся слово в'\
                          , calculator, 'предложении:', \
                          all_words[count_words.index(max(count_words))])
                    j = i+2
                    i+=1                        
                    all_words = []
                    count_words = []
                elif i == (len(element)-1):
                    word = element[j:(i+1)]
                    if word not in all_words:
                        all_words.append(word)
                        count_words.append(0)
                    count_words[all_words.index(word)] += 1                    
                i+=1
                
    else:
        print('Введённого номера нет')    
