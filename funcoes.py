import numpy as np

def q1():
    v1 = np.random.randint(low=0, high=100, size=9)
    v2 = np.random.randint(low=0, high=100, size=9)
    v3 = v1 + v2
    return v3

def q2(v3):
    v3 = np.reshape(v3, (3, 3))
    v3 = np.float64(v3)
    v3 = np.transpose(v3)

    return v3


def q3(v3):
    v4 = np.random.randint(low=0, high=100, size=(3, 3))
    
    v4 = v4 @ v3

    return v4

def q4():
    v5 = np.random.randint(low=0, high=10, size=9)
    v6 = np.random.randint(low=0, high=10, size=9)

    interseccao = set(v5) & set(v6)
    print(interseccao)

    print("Indices do v5")
    for i, x in enumerate(v5):
        if x in interseccao:
            print(i, end=" ")

    print()

    print("Indices do v6")
    for i, x in enumerate(v6):
        if x in interseccao:
            print(i, end=" ")

    diferenca = set(v5)-set(v6)
    print(diferenca)

    return(v5, v6)

def q5(v5, v6):
    v7 = np.hstack((v5, v6))

    print(np.mean(v7))
    print(np.std(v7))
    print(np.var(v7))

    impar_par = lambda x: 1-(x%2)*2
    new_v7 = impar_par(v7)

    print(v7)

def q6():
    A = np.array([1, 3, 5])
    B = np.array([7, 5, 8])

    print(np.cross(A, B))

def q7():
    v8 = np.random.randint(low=0, high=100, size=(3, 3))
    ID_3 = np.identity(3)

    print(v4)
    print(ID_3)

    det_v8 = np.linalg.det(v8)
    print(det_v8)

    inv_v8 = np.linalg.inv(v8)
    print(inv_v8)

    #testando
    print(np.round(inv_v8 @ v8))