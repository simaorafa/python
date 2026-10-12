nums = [2,5,8,11,7,9,13]

# Imprimir a lista
print (nums) # [2,5,8,11,7,9,13]
# Imprimir um elemento da lista
print (nums[2]) # 8
#inserir um novo elemento no final da lista
nums.append(17) # [2,5,8,11,7,9,13,17]
#Inserir varios elementos no final da lista
nums.extend([12,16]) # [2,5,8,11,7,9,13,17,12,16]
# Inserir em posiçao especifica
nums.insert(3,29) ## [2,5,8,11,7,9,13,17,12,16]

#remover o elemento no final da lista
nums.pop() # [2,5,8,11,7,9,13,17,12]
#remover o elemento de uma posiçao especifica da lista pelo indiçe 
nums.pop(2) # [2,5,8,11,7,9,13,17,12]
# remover um elemento de uma posiçao especifica da lista pelo valor 
nums.insert(17) ## [2,5,8,11,7,9,13,17,12]
# nº de elementos da lista 
total = len (nums) # 8

for n in nums: # para cada elemento da minha lista
 if n <=10:
    print (n, end=" ")

for indice in range (len(num)):
    if nums [indice] <= 10:
        print (nums[indice],end = "")