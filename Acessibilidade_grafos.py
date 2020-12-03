from copy import deepcopy

#Variaveis globais
lista_de_no = []
matriz = []
matriz_adjacente = []
lista_origem = []
lista_destino = []
produto_resultado = []

#Função para cadastro de nós
def no(origem, destino):
    lista_de_no.append([origem, destino])
    return

#Função retorna quantidade de arestas do grafo
def qtd_arestas(lista_de_no):
    qtd_arestas = len(lista_de_no)
    return qtd_arestas

#Função retorna a quantidade de nós do grafo
def qtd_no(lista_de_no):
    list = []
    for i in lista_de_no:
        for a in i:
            if a not in list:
                list.append(a)
    qtd_no = len(list)
    return qtd_no

#Função ordena todos os elementos do grafo
def no_ordenado(lista_de_no):
    lista_ordenada = []
    for i in lista_de_no:
        for a in i:
            if a not in lista_ordenada:
                lista_ordenada.append(a)
    lista_ordenada.sort()
    return lista_ordenada


def matriz_bool(lista_ordenada):
    for m in lista_ordenada:
        for z in lista_ordenada:
            for n in lista_de_no:
                if m == n == z:
                    matriz = []
                    matriz.append(1)
                else:
                    matriz.append(0)
    return matriz


# Nós do grafo cadastrado
'''no(0, 2)
no(0, 4)
no(1, 3)
no(2, 7)
no(3, 6)
no(4, 5)
no(4, 7)
no(5, 1)
no(5, 4)
no(6, 0)
no(6, 2)
no(6, 4)
no(7, 3)
no(7, 5)
'''
no('Q', 'W')
no('Q', 'V')
no('R', 'Q')
no('R', 'V')
no('R', 'X')
no('S', 'R')
no('S', 'T')
no('T', 'X')
no('W', 'V')
no('W', 'X')
no('X', 'Y')
no('Y', 'U')
no('Y', 'Z')
no('Z', 'T')
no('Z', 'U')




# Gera as lista da origem e destino de cada nó
for a in lista_de_no:
    lista_origem.append(a[0])
    lista_destino.append(a[1])

# Gera matriz lista base
lista_base = []
for m in no_ordenado(lista_de_no):
    for n in no_ordenado(lista_de_no):
        lista_base.append([m, n])

# Gera matriz de adjacencia
for ellb in lista_base:
        if ellb in lista_de_no:
            matriz.append(1)
        else:
            matriz.append(0)
n = len(no_ordenado(lista_de_no))
len_l = len(matriz)
for i in range(n):
    start = int(i*len_l/n)
    end = int((i+1)*len_l/n)
    matriz_adjacente.append(matriz[start:end])



def gera_matriz(matriz_adjacente):
    for m in range(len(matriz_adjacente)):
        for n in range(len(matriz_adjacente[0])):
            print(f' {matriz_adjacente[m][n]:^3} ', end='')
        print()
    print()

def produto_matriz(matriz_alpha, matriz_beta):
    produto_resultado = []
    temp = []
    for i in range(len(matriz_alpha)):
        produto_resultado.append([])
        for j in range(len(matriz_adjacente)):
            for k in range(len(matriz_adjacente)):
                temp.append(matriz_alpha[i][k] * matriz_beta[k][j])
            if sum(temp[:]) > 0:
                produto_resultado[i].append(1)
            else:
                produto_resultado[i].append(0)
            temp.clear()
    return produto_resultado

def matriz_acessibilidade(matriz_adjacente):
    matriz_acessibilidade = deepcopy(matriz_adjacente)
    temp = produto_matriz(matriz_adjacente, matriz_adjacente)
    for i in range(len(matriz_adjacente)-1):
        ordem = i
        produto_resultado = deepcopy(temp)
        for i in range(len(matriz_adjacente)):
            for j in range(len(matriz_adjacente)):
                if produto_resultado[i][j] == 1:
                    matriz_acessibilidade[i][j] = produto_resultado[i][j]
        temp.clear()
        temp = produto_matriz(produto_resultado, matriz_adjacente)
        produto_resultado.clear()
    print('Matriz de Acessibilidade: ')
    print(no_ordenado(lista_de_no))
    print('________________________________________________')
    gera_matriz(matriz_acessibilidade)



# Lista de prints para teste
print('Esta é a lista de todos os vertices: ', lista_de_no)
print('Tem ', qtd_arestas(lista_de_no), 'arestas neste grafo')
print('Tem ', qtd_no(lista_de_no), 'vertices neste grafo')
print('Esta é a lista ordenada dos nós: ', no_ordenado(lista_de_no))
print('Lista de origem: ', lista_origem)
print('Lista de destino: ', lista_destino)
print('Matriz boleana: ',matriz_adjacente)
print('Tamanho da matriz: ', len(matriz_adjacente))
print('Esta é a lista base: ', lista_base)
print('Esta e a quantidade da lista base: ', len(lista_base))
print('#' *100)
print('Matriz de adjacencia')
print(no_ordenado(lista_de_no))
print('________________________________________________')
gera_matriz(matriz_adjacente)
matriz_acessibilidade(matriz_adjacente)