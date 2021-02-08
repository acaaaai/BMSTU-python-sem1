# ИУ7-16Б Фролова В.С
# Вычеркнуть строку с минимальным эл-ом
# Посчитать в каждом столбце кол-во эл-ов
# превышающих значение произведение эл-ов этого столбца

# поиск строки с минимальным эл-том
def minstr_number(matrix,row_count,column_count): 
    min_value = matrix[0][0]
    for i in range(row_count):
        for j in range(column_count):
            if matrix[i][j]<min_value:
                min_value=matrix[i][j]
                row_minvalue = i # номер искомой строки
    return(row_minvalue)

# ввод матрицы
matrix_q = []
row_count_q=int(input('Введите число <12: '))
column_count_q=int(input('Введите число <10: '))
for i in range(row_count_q): 
    matrix_q.append(list(map(int,input('Введите элементы строки: ').split())))

#вычеркивание строки и cдвиг матрицы
row_minvalue_matrixq = minstr_number(matrix_q,row_count_q,column_count_q)
row_count_q=(row_count_q)-1
for i in range(row_minvalue_matrixq,row_count_q):
    for j in range(column_count_q):
        matrix_q[i][j]=matrix_q[i+1][j]

print('Полученная матрица: ')

#вывод форматированной матрицы
for i in range(row_count_q):
    for j in range(column_count_q):
        print('{:^10.5g}'.format(matrix_q[i][j]),end='')
    print()
        
# поиск элементов
for j in range(column_count_q):
    count = 0 # количество искомых элементов 
    multi = 1 # произведение элементов столбца
    for i in range(row_count_q):# произведение
        multi*= matrix_q[i][j]
    for i in range(row_count_q): # поиск элементов
        if matrix_q[i][j]>multi:
            count+=1
    print('Количество искомых элементов в',j+1,'столбце =', count)
            
        
    
    
