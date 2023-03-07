# Programa que verifica se o sudoku é #válido
N = 9
matrix = []
flag = 0

#É sudoku
l = ['295743861','431865927','876192543',\
    '387459216','612387495','549216738','763524189'\
    ,'928671354','154938672']

#Não é sudoku    
# l = ['195743862','431865927','876192543',\
#      '387459216','612387495','549216738',\
#          '763524189','928671354','254938671']

try:
    for i in range(N):
        if flag == 1:
            break
        #l = input(f'Entre com os 9 nrs da {i+1}a linha: ')
        ln = []
        for char in l[i]:
            if not char.isspace():
                ln.append(char)
    
        for char in l:
            if ln.count(char) > 1:
                print(f'A {i+1}a linha não está no formato do sudoku!')
                flag = 1
                break
        matrix.append(ln)

    ln1 = []
    ln2 = []
    ln3 = []
    for u in range(3):
        for v in range(3):
            ln1.append(matrix[u][v])
            if ln1.count(matrix[u][v]) > 1:
                flag = 1
                break
        for v in range(3,6,1):
            ln2.append(matrix[u][v])
            if ln2.count(matrix[u][v]) > 1:
                flag = 1
                break
        for v in range(6,9,1):
            ln3.append(matrix[u][v])
            if ln3.count(matrix[u][v]) > 1:
                flag = 1
                break
    ln1 = []
    ln2 = []
    ln3 = []
              
    for u in range(3,6,1):
        for v in range(3):
            ln1.append(matrix[u][v])
            if ln1.count(matrix[u][v]) > 1:
                flag = 1
                break
        for v in range(3,6,1):
            ln2.append(matrix[u][v])
            if ln2.count(matrix[u][v]) > 1:
                flag = 1
                break
        for v in range(6,9,1):
            ln3.append(matrix[u][v])
            if ln3.count(matrix[u][v]) > 1:
                flag = 1
                break
    ln1 = []
    ln2 = []
    ln3 = []
                
    for u in range(6,9,1):
        for v in range(3):
            ln1.append(matrix[u][v])
            if ln1.count(matrix[u][v]) > 1:
                flag = 1
                break
        for v in range(3,6,1):
            ln2.append(matrix[u][v])
            if ln2.count(matrix[u][v]) > 1:
                flag = 1
                break
        for v in range(6,9,1):
            ln3.append(matrix[u][v])
            if ln3.count(matrix[u][v]) > 1:
                flag = 1
                break
            
    if flag == 1:
        print('Não é sudoku!')
    else:
        print('É sudoku!')
except Exception as e:
    print(e)
