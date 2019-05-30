"""
||||||||||| ENUNCIADO |||||||||||

Implementar um programa para:

--> Dado um grafo, dizer se ele tem um ciclo Euleriano (Sim/Não), para isto devo:
     * Testar se o grafo é conexo (todos os vértices tem arestas que os ligam).
     * Testar se todos os vértices tem grau par.

--> Se positivo, mostrar este ciclo.

--> Dar a complexidade de cada função:
    * Teste de vértices grau par.
    * Teste de conectividade.
    * Teste de Ciclo Euleriano.

--> Observações:
     * Usar grafos simples não direcionados

"""

import csv


def main():


    lista_vertices = []
    lista_adj = []

    with open('grafo.csv', 'r') as g:
        lines = csv.reader(g)
        grafo = list(lines)

        for i in range(len(grafo)):  # Separa vértices
            for j in range(2):
                aux = int(grafo[i][j])
                if lista_vertices.count(aux) < 1:  # Pego somente a primeira posição de cada linha
                    lista_vertices.append(aux)  # lista de vértices

        lista_vertices = sorted(lista_vertices)

        print(f'\nGrafo: {grafo}\n')
        print(f'Vértices: {lista_vertices}\n')

        # Criando lista de adjacências
        for i in range(len(lista_vertices)):
            lista_adj.append(0)
            auxadj = []
            for j in range(len(grafo)):

                    if int(grafo[j][0]) == lista_vertices[i]:
                        auxadj.append(int(grafo[j][1]))
                    if int(grafo[j][1]) == lista_vertices[i]:
                        auxadj.append(int(grafo[j][0]))
            lista_adj[i] = sorted(auxadj)

        print(f'Lista de Adjacências: {lista_adj}\n')

        teste_graupar(lista_vertices, lista_adj)


def teste_graupar(lista_vertices, lista_adj):


    flag = 0

    print('\n---------- TESTE GRAU PAR ----------')
    for x in range(len(lista_vertices)):
        if (len(lista_adj[x]) % 2) == 0:
            print(f'Vértice {lista_vertices[x]} possui grau par!')
        else:
            print(f'Vértice {lista_vertices[x]} não possui grau par!')
            flag = flag + 1

    if flag > 0:
        print(f'\nESTE GRAFO NÃO POSSUI UM CICLO EULERIANO! *** Motivo: {flag} dos vértices não tem grau par!')
    else:

        teste_conexo(lista_vertices, lista_adj)


def teste_conexo(lista_vertices, lista_adj):


    vertice_inicial = lista_vertices[0]
    conexoes = []
    conexoes.append(vertice_inicial)

    busca_profundidade(vertice_inicial, conexoes,  lista_adj)

    print('\n\n-------- TESTE GRAFO CONEXO --------')
    if len(conexoes) == len(lista_vertices):
        print('O grafo inserido é conexo!')
        print(f'Resultado profundidade: {conexoes}')
        imprime_ciclo(lista_vertices, lista_adj)

    else:
        print('ESTE GRAFO NÃO POSSUI UM CICLO EULERIANO! *** Motivo: O grafo inserido não é conexo!')


def busca_profundidade(vertice, conexoes, lista_adj):


    for i in lista_adj[vertice]:

        if conexoes.count(i) == 0:
            conexoes.append(i)
            busca_profundidade(i, conexoes, lista_adj)


def imprime_ciclo(lista_vertices, lista_adj):


    inicio = lista_vertices[0]
    ciclo_euler = [inicio]

    print('\n\n-------- ALGORITMO DE FLEURY --------')
    fleury(inicio, inicio, ciclo_euler, lista_vertices, lista_adj)

    print('\n\n---------- CICLO EULERIANO ----------')
    print(f'Ciclo: {ciclo_euler}')


def fleury(inicio, i, ciclo_euler, lista_vertices, lista_adj):


    vazia = 0
    for y in lista_adj:
        if y == []:
            vazia +=1

    if i == inicio and vazia==len(lista_adj):  # lista_adj[i-1] A posição -1 não existe
        return True

    if (len(lista_adj[i])) > 0:
        for j in lista_adj[i]:

            lista_adj[j].remove(i)
            lista_adj[i].remove(j)

            print(f'LIsta adj: {lista_adj}')
            ciclo_euler.append(j)

            ciclo_completo = fleury(inicio, j, ciclo_euler, lista_vertices, lista_adj)

            if not ciclo_completo:
                aux = lista_adj[i][:]
                aux.append(j)
                lista_adj[i] = aux

                aux2 = lista_adj[j][:]
                aux2.append(i)
                lista_adj[j] = aux2

                ciclo_euler.pop()
            else:
                return True


main()

# Complexidade de tempo do algoritmo: O(|VA|) que é semelhante a O(|v3|)
