def sum(arr, val):
    arrA = []
    l = len(arr)
    if (isinstance(val, list)):
        for i in range(l):
            arrA.append(arr[i] + val[i])
    else:
        for i in range(l):
            arrA.append(arr[i] + val)
    return arrA

def mult(arr, val):
    arrA = []
    l = len(arr)
    if (isinstance(val, list)):
        for i in range(l):
            arrA.append(arr[i] * val[i])
    else:
        for i in range(l):
            arrA.append(arr[i] * val)
    return arrA

def res(arr, val):
    arrA = []
    l = len(arr)
    if (isinstance(val, list)):
        for i in range(l):
            arrA.append(arr[i] - val[i])
    else:
        for i in range(l):
            arrA.append(arr[i] - val)
    return arrA

def div(arr, val):
    arrA = []
    l = len(arr)
    if (isinstance(val, list)):
        for i in range(l):
            arrA.append(arr[i] / val[i])
    else:
        for i in range(l):
            arrA.append(arr[i] / val)
    return arrA

def getColumn(arr, col):
    lista = []
    l = len(arr)
    for i in range(l):
        lista.append(arr[i][col])
    return lista