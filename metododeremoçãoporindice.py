import time


size = 100000
def remove(premio):
    aux = []
    aux = list(premio)
    array = []
    for i in range(len(premio)):
        premio.pop(i)
        array.append(int(''.join(map(str, premio))))
        premio = list(aux)
    return list(array)
def maior(array):
    max = array[0]
    for i in range (len(array)):
        if array[i] > max: 
            max = array[i]
    return max

while 1:
    num = [0]*size
    n, d = map(int, input().split())
    if n==0 and d==0:
        break
    num = [0]*n    
    num = input()
    start_time = time.time()

    premio = []
    array = []
    for i in range(len(num)):
        premio.append(int(num[i]))

    if(n-1 >(n-d)):
        for i in range(n-(n-d)):
            array = remove(premio)
            maxpremio = maior(array)
            premio = list(str(maxpremio))
    else:
        array = remove(premio)
        maxpremio = maior(array)
    print(maxpremio)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Tempo de execução: ", elapsed_time, " segundos.")