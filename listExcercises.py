def uno():
    lista = ["blue", "white", "green", "red", "pink", "yellow"]
    return lista

def dos(lista):
    print (len(lista))

def tres(lista):
    print ("true" if "blue" in lista else "false", "true" if "purple" in lista else "false")

def cuatro(lista):
    print (lista.index("white"))
    try:
        print (lista.index("black"))
    except ValueError:
        print (-1)

def cinco(lista):
    lista.append("violet")
    lista.append("gray")

def seis(lista):
    lista.append(["black", "brown"])

def siete(lista):
    newL = ["cyan"] + lista[3:]
    return newL

def ocho(lista):
    lista[6].append("orange")

def nueve(lista):
    del lista[2:]

def diez():
    matriz = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]

def once():
    numbers = [[1,2],[3,4],[5,6],[7,8,9]]
    print (len(numbers[3]))

def doce():
    oddSquare = [x * x for x in range (1, 10) if x & 1]
    print (oddSquare)

def trece():
    table = [[3, x, 3*x] for x in range(1, 11)]
    print(table)

def catorce():
    matriz = [[['?' for i in range(0, 2)] for i in range(0, 3)] for i in range(0, 4)]
    print (matriz)

l = uno()

print (l)
dos(l)
tres(l)
cuatro(l)
cinco(l)
print (l)
seis(l)
print (l)
l = siete(l)
print (l)
ocho(l)
print (l)
nueve(l)
print (l)
diez()
once()
doce()
trece()
catorce()
