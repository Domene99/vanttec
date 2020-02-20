def uno():
    d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
    return d;

def dos(d):
   print ("true" if 4 in d else "false", "true" if 7 in d else "false") 

def tres(d):
    print ("true" if 'a' in d.values() else "false", "true" if 'z' in d.values() else "false")

def cuatro(d):
    d[6] = 'f'

def cinco(d):
    del d[2]

def seis(d):
    dictNum = {'x':700, 'y':56874, 'z': 990}
    print ("Max: ", max(dictNum.values()), "\nMax: ", min(dictNum.values()))

d = uno()
dos(d)
tres(d)
cuatro(d)
print (d)
cinco(d)
print (d)
seis(d)
