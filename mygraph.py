from linkedlist import LinkedList, length, append
from algo import *


'''
def createGraph(List_vertice, List_aristas)
    Descripción: Implementa la operación crear grafo
    Entrada: LinkedList con la lista de vértices y LinkedList con la
    lista de aristas donde por cada par de elementos representa una
    conexión entre dos vértices.
    Salida: retorna el nuevo grafo
'''


def createGraph(listVertices, listAristas=LinkedList()):
    # NOTA: Si solo paso una lista de vértices, asumo que no hay aristas

    # Tamaño del Graph es la cantidad de vértices
    graphSize = length(listVertices)

    # Si no hay vertices, no creo un grafo
    if(graphSize == 0):
        return None

    Graph = Array(graphSize, LinkedList())

    currentVertice = listVertices.head

    # Inserto los vértices en el Graph
    for i in range(0, graphSize):

        # Creo LinkedList e inserto el elemento (vértice)
        verticeElement = LinkedList()
        append(verticeElement, currentVertice.value)
        Graph[i] = verticeElement

        # En cada iteración, vuelvo al principio de la lista de aristas
        currentArista = listAristas.head

        # Itero por todas las aristas (con "paso" 2)
        while(currentArista != None and currentArista.nextNode != None):
            # Si el elemento es el vertice del grafo, entonces el siguiente es la conexión (dirigido)
            if(Graph[i].head.value == currentArista.value):
                append(Graph[i], currentArista.nextNode.value)

            # Continuo con el siguiente par de vertices (arista)
            currentArista = currentArista.nextNode.nextNode

        # Continuo con el siguiente vértice
        currentVertice = currentVertice.nextNode

    return Graph
