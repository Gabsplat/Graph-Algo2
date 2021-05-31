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
append(listVertices, 12)
append(listVertices, 9)
append(listVertices, 8)
append(listVertices, 6)
append(listVertices, 5)
append(listVertices, 4)
append(listVertices, 3)
append(listVertices, 1)

listAristas = LinkedList()
# append(listAristas, 1)
# append(listAristas, 2)
# append(listAristas, 2)
# append(listAristas, 1)
# append(listAristas, 3)
# append(listAristas, 4)
# append(listAristas, 4)
# append(listAristas, 3)
append(listAristas, 9)
append(listAristas, 5)
append(listAristas, 3)
append(listAristas, 1)
append(listAristas, 12)
append(listAristas, 3)
append(listAristas, 8)
append(listAristas, 1)
append(listAristas, 3)
append(listAristas, 6)
append(listAristas, 5)
append(listAristas, 4)
append(listAristas, 9)
append(listAristas, 6)
append(listAristas, 1)
append(listAristas, 1)


Graph1 = createGraph(listVertices, listAristas)
print("Grafo 1:")
for i in range(0, len(Graph1)):
    printList(Graph1[i])
