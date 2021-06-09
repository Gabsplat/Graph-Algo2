from mygraph import *


'''
def printList(Linked):
    Función que recibe una LinkedList e imprime los elementos de la lista
'''


def printList(Linked):

    currentNode = Linked.head
    while(currentNode != None):
        print(currentNode.value, end=" ")
        currentNode = currentNode.nextNode
    print("")


'''
EJERCICIO 1
'''
print("")
print("Ejercicio 1 - Crear Grafo:")
print("")

listVertices = LinkedList()
# append(listVertices, 1)
# append(listVertices, 2)
# append(listVertices, 3)
# append(listVertices, 4)
append(listVertices, 1)
append(listVertices, 2)
append(listVertices, 3)
append(listVertices, 4)
append(listVertices, 5)
append(listVertices, 6)
append(listVertices, 7)
append(listVertices, 8)

listAristas = LinkedList()
append(listAristas, 1)
append(listAristas, 2)
append(listAristas, 2)
append(listAristas, 3)
append(listAristas, 3)
append(listAristas, 7)
append(listAristas, 3)
append(listAristas, 4)
append(listAristas, 4)
append(listAristas, 8)
append(listAristas, 4)
append(listAristas, 5)
append(listAristas, 5)
append(listAristas, 6)
append(listAristas, 8)
append(listAristas, 7)
# append(listAristas, 5)
# append(listAristas, 1)


Graph1 = createGraph(listVertices, listAristas)
DirectedGraph1 = createDirectedGraph(listVertices, listAristas)
print("Grafo 1:")
for i in range(0, len(Graph1)):
    printList(Graph1[i])

print("")
print("Grafo 1 (Dirigido)")

for i in range(0, len(DirectedGraph1)):
    printList(DirectedGraph1[i])


print("")
print("EJERCICIO 2:")
print("")

print("¿Existe un camino entre 1 y 7?: ", existPath(Graph1, 1, 7))
print("¿Existe un camino entre 1 y 6?: ", existPath(Graph1, 1, 6))

print("")
print("EJERCICIO 3:")
print("")

print("Es conexo: ", isConnected(Graph1))

print("")
print("EJERCICIO 4:")
print("")

print("Es árbol: ", isTree(Graph1))
