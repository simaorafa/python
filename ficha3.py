lista = [1,2,3,4,5,6,7,8,9,10]
Listapalavras = ["python", "programacao", "muamba", "seila", "nao"]
listanumeros = [1,3,5,7,9,2,112]
Listamaiusculo = ["maRCelO AmorIM"]
listamultiplodetres = [1, 3, 6, 9, 12, 2,5,7]
listanomeA =["ana,amelia,almeida,anabelle"]
# pares = []
# for num in lista:
#   if num % 2 == 0:
#       pares.append(num+1)
#   else:
#       pares.append(num)

#pares = [num+1 if num <5 else num for num in lista if num % 2 == 0]



pares = [num for num in lista if num % 2 == 0]
listaquadrados = [ num * num for num in lista]
print(listaquadrados)



tamanhos = []
for palavra in Listapalavras:
    tamanhos.append(len(palavra))
print(tamanhos)



numeros = [num for num in listanumeros if num >=5]
print (numeros)



maiusculas = [letra for letra in Listamaiusculo if letra.isupper()]
print(maiusculas)

multiplos = [num*2 if num % 3 == 0 else num for num in listamultiplodetres]
print(maiusculas)

nomesA = [letra.isupper if letra in listanomeA = a in listamultiplodetres]
