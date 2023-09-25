#Merge Sort - Ordenação por intercalação(mistura)
#Complexidade: 0(n*log(n))

def merge_sort(lista):
    if len(lista)>1:
        #Encontrando o meio da lista
        meio = len(lista) // 2 #Parte inteira da lista
        #Dividindo a lista em duas = fatiamento de listas
        esquerda = lista[:meio] #Esquerdo do meio até a metade
        direita = lista[meio:] #Direito do meio para frente
        #Chamada recursiva, divisão das sublistas
        merge_sort(esquerda)#Ordena a primeira parte da lista (esquerda)
        merge_sort(direita)#Ordena a segunda parte da lista (direita)
        #variáveis de controle
        #i - fará o controle da lista esquerda
        #j - fará o controle da lista direita
        #k - fará o controle final da nova lista ordenada
        i=0; j=0; k=0
        while i <len(esquerda) and j<len(direita):
            if esquerda[i]<direita[j]:
                lista[k] = esquerda[i]
                i+=1
            else:
                lista[k] = direita[j]
                j+=1
                k+=1


        #verifiação dos elementos da lista esquerda
        while(i<len(esquerda)):
            lista[k]=esquerda[i]
            i+=1
            k += 1
            

        #verificação dos elementos da lista direita
        while(j<len(direita)):
            lista[k] = lista[j]
            j+=1
            k+=1


#programa principal
lista = [12, 11, 13, 5, 6, 7]
print(f'Lista Original: {lista}')
merge_sort(lista)
print(f'Lista Ordenada: {lista}')