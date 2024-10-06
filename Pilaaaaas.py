class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)
    return pila.desapilar()

def evaluar_expresion_prefija(expresion):
    pila = Pila()
    tokens = expresion.split()[::-1]
    for token in tokens:
        if token.isdigit():
            pila.apilar(int(token))
        else:
            operando1 = pila.desapilar()
            operando2 = pila.desapilar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)
    return pila.desapilar()

def convertir_a_posfija(expresion):
    def precedencia(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    
    salida = []
    pila = Pila()
    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():
            salida.append(token)
        elif token == '(':
            pila.apilar(token)
        elif token == ')':
            while not pila.esta_vacia() and pila.items[-1] != '(':
                salida.append(pila.desapilar())
            pila.desapilar()
        else:
            while (not pila.esta_vacia() and precedencia(pila.items[-1]) >= precedencia(token)):
                salida.append(pila.desapilar())
            pila.apilar(token)

    while not pila.esta_vacia():
        salida.append(pila.desapilar())

    return ' '.join(salida)

def convertir_a_prefija(expresion):
    def precedencia(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    
    salida = []
    pila = Pila()
    tokens = expresion.split()[::-1]

    for token in tokens:
        if token.isdigit():
            salida.append(token)
        elif token == ')':
            pila.apilar(token)
        elif token == '(':
            while not pila.esta_vacia() and pila.items[-1] != ')':
                salida.append(pila.desapilar())
            pila.desapilar()
        else:
            while (not pila.esta_vacia() and precedencia(pila.items[-1]) > precedencia(token)):
                salida.append(pila.desapilar())
            pila.apilar(token)

    while not pila.esta_vacia():
        salida.append(pila.desapilar())

    return ' '.join(salida[::-1])

# Ejemplo de uso:
expresion_infix = "3 + 4 * 2 / ( 1 - 5 )"

expresion_postfix = convertir_a_posfija(expresion_infix)
expresion_prefix = convertir_a_prefija(expresion_infix)

print(f"Notación Posfija: {expresion_postfix}")
print(f"Evaluación Posfija: {evaluar_expresion_posfija(expresion_postfix)}")

print(f"Notación Prefija: {expresion_prefix}")
print(f"Evaluación Prefija: {evaluar_expresion_prefija(expresion_prefix)}")
