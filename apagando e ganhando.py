
def quicksort(arr):
    """
    Ordena um array usando o algoritmo Quicksort
    """
    # Caso base: o array tem tamanho 0 ou 1
    if len(arr) <= 1:
        return arr
    
    # Escolhe um pivô (neste caso, o último elemento do array)
    pivot = arr[-1]
    
    # Divide o array em dois sub-arrays menores
    left = []
    right = []
    for i in range(len(arr)-1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    # Ordena os sub-arrays menores recursivamente
    left_sorted = quicksort(left)
    right_sorted = quicksort(right)
    
    # Combina os sub-arrays menores ordenados com o pivô para formar o array ordenado final
    return left_sorted + [pivot] + right_sorted

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
SIZE = 10**5

while True:
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        break
    if n == SIZE:
        my_digitos_lousa = [0]*SIZE
    else:
        num = input()
        my_digitos_lousa = [0]*n
    
    for i in range(n):
        my_digitos_lousa[i] = (int(num[i]))
    
    #Ordena os numeros da lousa
    my_digitos_sorted = quicksort(my_digitos_lousa)


   
    max_digitos = []
    indice = []
    premio = []
    #os ultimos elementos da lista ordenada são os maiores, onde n-d que não serão apagados da lousa 
    for j  in range(n-d):
        max_digitos.append(my_digitos_sorted[-j+-1])#pegas os ultimos elementos da lista.
        indice.append(linear_search(my_digitos_lousa, max_digitos[j])) # faz uma busca binaria do inde onde o maior digito se encontra
        print(j)
        
    
    indice = quicksort(indice) #ordena o indice
     
    for i in range(n-d):
       premio.append(my_digitos_lousa[indice[i]])# Armazena o premio premio
    
    premio =  int(''.join(map(str, premio)))# juntar [2 ,6] ficaria 26
    print(premio)
    


