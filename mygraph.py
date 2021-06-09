from linkedlist import LinkedList, length, append, search
from algo import *


'''
def createGraph(List_vertice, List_aristas)
    Descripción: Implementa la operación crear grafo
    Entrada: LinkedList con la lista de vértices y LinkedList con la
    lista de aristas donde por cada par de elementos representa una
    conexión entre dos vértices.
    Salida: retorna el nuevo grafo
'''


def createDirectedGraph(listVertices, listAristas=LinkedList()):
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
            graphElement = Graph[i].head

            if(graphElement.value == currentArista.value):
                append(Graph[i], currentArista.nextNode.value)

            # Continuo con el siguiente par de vertices (arista)
            currentArista = currentArista.nextNode.nextNode

        # Continuo con el siguiente vértice
        currentVertice = currentVertice.nextNode

    return Graph


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
            graphElement = Graph[i].head

            if(graphElement.value == currentArista.value):
                append(Graph[i], currentArista.nextNode.value)
            elif(graphElement.value == currentArista.nextNode.value):
                append(Graph[i], currentArista.value)

            # Continuo con el siguiente par de vertices (arista)
            currentArista = currentArista.nextNode.nextNode

        # Continuo con el siguiente vértice
        currentVertice = currentVertice.nextNode

    return Graph


'''
def existPath(Grafo, v1, v2):
    Descripción: Implementa la operación existe camino que busca si
    existe un camino entre los vértices v1 y v2
    Entrada: Grafo con la representación de Lista de Adyacencia, v1 y
    v2 vértices en el grafo.
    Salida: retorna True si existe camino entre v1 y v2, False en
    caso contrario.
'''


def existPath(Graph, v1, v2):
    v1List = findListByElement(Graph, v1)
    v2List = findListByElement(Graph, v2)
    # Si no existe alguna de las listas, entonces el vértice no existe
    if(v1List == None or v2List == None):
        # Retorno None
        return None

    # Creo lista para verificar elementos ya revisados
    alreadyChecked = LinkedList()

    # Llamo a la función recursiva
    pathExists = existPathR(Graph, v1List, v2, alreadyChecked)

    if(pathExists == None):
        return False
    return pathExists


'''
def existPathR(Grafo, currentList, targetValue, alreadyChecked):
    Funcion recursiva de existPath que define si existe un camino entre 2 vertices de un grafo
'''


def existPathR(Graph, currentList, targetValue, alreadyChecked):
    returnValue = False
    listHead = currentList.head

    # Si la lista no tiene elementos, retorno False
    if(listHead == None):
        return False
    # Si el elemento del head es igual al valor buscado (vertice 2), retorno True
    elif(listHead.value == targetValue):
        return True

    # Agrego a la lista de los elementos ya verificados
    append(alreadyChecked, listHead.value)

    # Empiezo a recorrer por el segundo valor de la lista
    currentNode = listHead.nextNode
    while(currentNode != None):

        # Verifico si ya no se pasó por el nodo actual (buscando en la lista alreadyChecked)
        position = search(alreadyChecked, currentNode.value)

        # Si no se verificó
        if(position == None):
            # Busco la lista en el grafo con el value del nodo actual
            graphList = findListByElement(Graph, currentNode.value)
            # Llamada recursiva con la nueva lista
            returnValue = existPathR(
                Graph, graphList, targetValue, alreadyChecked)

        if(returnValue):
            return returnValue
        else:
            currentNode = currentNode.nextNode


'''
def findListByElement(Graph, value)
    Busca una lista por valor en un grafo
'''


def findListByElement(Graph, value):

    for i in range(0, len(Graph)):
        graphList = Graph[i]
        if(graphList.head.value == value):
            return graphList

    return None


'''
Ejercicio 3
def isConnected(Grafo):
    Descripción: Implementa la operación es conexo
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.

'''


def isConnected(Graph):
    firstGraphValue = Graph[0].head.value
    graphLength = len(Graph)
    # Recorro todos los vértices y verifico que haya camino con el primer vértice
    for i in range(1, graphLength):
        pathExists = existPath(Graph, firstGraphValue, Graph[i].head.value)
        # Si no hay camino, retorno false (no conexo)
        if(not pathExists):
            return False
    # Si nunca retorné False, significa que hay camino
    return True


'''
def isTree(Grafo):
    Descripción: Implementa la operación es árbol
    Entrada: Grafo con la representación de Lista de Adyacencia.
    Salida: retorna True si el grafo es un árbol.
'''


def isTree(Graph):
    # Si el grafo es no conexo, no es árbol
    if(not isConnected(Graph)):
        return False

    # Por cada elemento del grafo, verifico que no tenga ciclos
    for i in range(0, len(Graph)):
        currentValue = Graph[i].head.value

        currentNode = Graph[i].head.nextNode
        # Loop por los nodos del elemento del grafo actual
        while(currentNode != None):
            childList = findListByElement(
                Graph, currentNode.value)
            # Verifico por cada elemento, si existe un ciclo con el elemento parent
            cycle = formsCycle(Graph, currentValue, childList)
            # Si hay un ciclo, no es un árbol
            if(cycle):
                return False
            currentNode = currentNode.nextNode
    return True


'''
def formsCycle(Graph, vertice, childList):
    Función que verifica si existe un ciclo desde un vértice y uno camino desde uno de sus children
'''


def formsCycle(Graph, vertice, childList):
    alreadyChecked = LinkedList()
    cycle = formsCycleR(
        Graph, childList, childList.head.value, vertice, alreadyChecked)
    if(cycle == None):
        return False
    return cycle


'''
def formsCycleR(Graph, currentList, firstValue, targetValue, alreadyChecked):
    Función recursiva de theresCycle
'''


def formsCycleR(Graph, currentList, firstValue, targetValue, alreadyChecked):
    returnValue = False
    listHead = currentList.head

    # Si la lista no tiene elementos, retorno False
    if(listHead == None):
        return False
    # Si el elemento del head es igual al valor buscado (vertice 2), retorno True
    elif(listHead.value == targetValue):
        return True

    # Agrego a la lista de los elementos ya verificados
    append(alreadyChecked, listHead.value)

    # Empiezo a recorrer por el segundo valor de la lista
    currentNode = listHead.nextNode
    while(currentNode != None):

        # Verifico si ya no se pasó por el nodo actual (buscando en la lista alreadyChecked)
        position = search(alreadyChecked, currentNode.value)

        # Si no se verificó
        if(position == None):
            # Busco la lista en el grafo con el value del nodo actual
            # Si estamos ubicados en la primer lista
            if(listHead.value == firstValue):
                # Y el valor por el que pasamos es el target (significa que hay conexión no dirigida, pero no ciclo)
                if(currentNode.value != targetValue):
                    graphList = findListByElement(Graph, currentNode.value)
                    # Llamada recursiva con la nueva lista
                    returnValue = formsCycleR(
                        Graph, graphList, firstValue, targetValue, alreadyChecked)
            else:
                graphList = findListByElement(Graph, currentNode.value)
                # Llamada recursiva con la nueva lista
                returnValue = formsCycleR(
                    Graph, graphList, firstValue, targetValue, alreadyChecked)

        if(returnValue):
            return returnValue
        else:
            currentNode = currentNode.nextNode


def printList(list):
    currentNode = list.head
    while(currentNode != None):
        print(currentNode.value, end=" ")
        currentNode = currentNode.nextNode
    print("")
