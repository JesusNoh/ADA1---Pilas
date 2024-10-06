class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop() if not self.esta_vacia() else None

def mover_disco(origen, destino):
    destino.apilar(origen.desapilar())

def resolver_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        mover_disco(origen, destino)
    else:
        resolver_hanoi(n - 1, origen, destino, auxiliar)
        mover_disco(origen, destino)
        resolver_hanoi(n - 1, auxiliar, origen, destino)

# Función para inicializar la pila origen con la cantidad de discos deseada
def inicializar_pila_origen(cantidad_discos):
    pila = Pila()
    for i in range(cantidad_discos, 0, -1):
        pila.apilar(i)
    return pila

# Pedir al usuario que ingrese la cantidad de discos
cantidad_discos = int(input("Ingrese la cantidad de discos: "))

# Inicializar las pilas
pila_origen = inicializar_pila_origen(cantidad_discos)
pila_auxiliar = Pila()
pila_destino = Pila()

# Resolver el problema de las Torres de Hanoi
resolver_hanoi(cantidad_discos, pila_origen, pila_auxiliar, pila_destino)

# Mostrar los contenidos de la pila destino
while not pila_destino.esta_vacia():
    print(pila_destino.desapilar())
