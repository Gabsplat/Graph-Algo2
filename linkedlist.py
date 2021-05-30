class LinkedList:
    head = None


class Node:
    value = None
    nextNode = None

# Función add
# Descripción: Agrega un elemento al comienzo de	L, siendo L una LinkedList que representa el TAD secuencia.
# Entrada:	La	Lista	sobre	la	cual	se	quiere	agregar	el	elemento (LinkedList)	y el valor del elemento (element) a		agregar.
# Salida:	No hay salida definida


def add(L, element):
    newNode = Node()
    newNode.value = element
    newNode.nextNode = L.head
    L.head = newNode
    return


# Función insert
# Descripción: Inserta un elemento en una posición determinada de la lista que representa el TAD secuencia.
# Entrada: la lista sobre el cual se quiere realizar la inserción (Linkedlist) y el valor del elemento (element) a insertar y la posición (position) donde se quiere insertar.
# Salida: Si pudo insertar con éxito devuelve la posición donde se inserta el elemento. En caso contrario devuelve None. Devuelve None si la posición a insertar es mayor que el número de elementos en la lista.

def insertLinked(L, element, position):
    newNode = Node()
    newNode.value = element

    if(position == 0):
        add(L, element)
        return position

    currentNode = getNode(L, position-1)
    if(currentNode == None):
        return None
    newNode.nextNode = currentNode.nextNode
    currentNode.nextNode = newNode
    return position


# Función delete
# Descripción: Elimina un elemento de la lista que representa el TAD secuencia.
# Poscondición: Se debe desvincular el Node a eliminar.
# Entrada:	la	lista	sobre	el	cual	se	quiere realizar la eliminación (Linkedlist) y el valor del elemento (element) a eliminar.
# Salida:	Devuelve	la	posición	donde	se	encuentra	el	elemento	a eliminar. Devuelve None si el elemento a eliminar no se encuentra.

def delete(L, element):
    newNode = Node()
    newNode.value = element
    position = search(L, element)
    if(position == None):
        return None
    if(position == 0):
        L.head = L.head.nextNode
        return position
    currentNode = getNode(L, position-1)
    currentNode.nextNode = currentNode.nextNode.nextNode
    return position


# Función search
# Descripción:	Busca	un	elemento	de	la	lista	que	representa	el	TAD secuencia.
# Entrada:	la	lista	sobre	el	cual	se	quiere	realizar	la	búsqueda (Linkedlist) y el valor del elemento (element) a buscar.
# Salida: Devuelve la posición donde se encuentra la primera instancia del elemento. Devuelve None si el elemento no se encuentra.

def search(L, element):
    currentNode = L.head
    counter = 0
    while(currentNode != None):
        if(currentNode.value == element):
            return counter
        counter += 1
        currentNode = currentNode.nextNode
    return None


# Función length
# Descripción: Calcula el número de elementos de la lista que representa el TAD secuencia.
# Entrada:	La	lista	sobre	la	cual	se	quiere	calcular	el	número	de elementos.
# Salida: Devuelve el número de elementos.

def length(L):
    currentNode = L.head
    counter = 0
    while(currentNode != None):
        counter += 1
        currentNode = currentNode.nextNode
    return counter


# Función access
# Descripción: Permite acceder a un elemento de la lista en una posición determinada.
# Entrada: La lista (LinkedList) y la position del elemento al cual se quiere acceder.
# Salida: Devuelve el valor de un elemento en una position de la lista, devuelve None si no existe elemento para dicha posición.

def access(L, position):
    node = getNode(L, position)
    if(node == None):
        return None
    else:
        return node.value

# Función que devuelve un nodo de una lista en la posición indicada


def getNode(L, position):
    currentNode = L.head
    counter = 0
    while(currentNode != None):
        if(counter == position):
            return currentNode
        counter += 1
        currentNode = currentNode.nextNode
    return None


# Función update
# Descripción: Permite cambiar el valor de un elemento de la lista en una posición determinada
# Entrada: La lista (LinkedList) y la position sobre la cual se quiere asignar el valor de	element.
# Salida: Devuelve None si no existe elemento para dicha posición. Caso contrario devuelve la posición donde pudo hacer el update.

def update(L, element, position):
    currentNode = getNode(L, position)
    if(currentNode == None):
        return None
    currentNode.value = element
    return position


# Función que agrega un valor al final de una lista

def append(L, value):
    newNode = Node()
    newNode.value = value

    if(L.head == None):
        L.head = newNode
        return
    currentNode = L.head
    while(currentNode.nextNode != None):
        currentNode = currentNode.nextNode

    currentNode.nextNode = newNode
    return
