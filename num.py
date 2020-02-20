import numpy as np

def uno():
    print (np.arange(20))

def dos():
    print (np.arange(30, 40))

def tres():
    print (np.zeros((6, 6)))

def cuatro():
    print (np.ones((4, 4)))

def cinco():
    sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
    print (sampleArray[:,2:])

def seis():
    a = np.array([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37])
    print (np.flip(a))

def siete(mat):
    print (mat[0:2,1:3])

def ocho(mat):
    print (mat[1:4,2:4])

def nueve(mat):
    x, y = mat[:4,:3], mat[:,3:]
    print (x, "\n", y)
    diez(x)

def diez(x):
    train, test = x[:3,:3], x[:,2:]
    print (train, "\n", test)

uno()
dos()
tres()
cuatro()
cinco()
seis()
mat = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
siete(mat)
ocho(mat)
nueve(mat)
