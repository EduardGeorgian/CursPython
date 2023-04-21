# cerinta 1
lista = [7,8,9,2,3,1,4,10,5,6]
listaOrdonataAscendent = list(lista)
listaOrdonataAscendent.sort()
print(listaOrdonataAscendent)
#cerinta2
listaOrdonataDescendent = list(lista)
listaOrdonataDescendent.sort(reverse=True)
print(listaOrdonataDescendent)

#cerinta3
listaSliced = lista[::2]
print(listaSliced)

#cerinta4
listaSlicedIndiciImpari = lista[1::2]
print(listaSlicedIndiciImpari)
#cerinta5
i=0

print("multiplii lui 3 din lista sunt: ")
for i in range(len(lista)):
    if lista[i] % 3 == 0:
        print(lista[i] , end="   ")
