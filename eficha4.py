aluno = {
         "nome": "Ana Silva",
         "idade": 17, 
         "cidade":"famalicão",
         "disciplinas": ["Matemática", "Física", "Informática"],
         "notas": {"matematica":18, "Informática": 19,"Física": 17}
         }

aluno["disciplinas"].append("portugues")
aluno["notas"]["Portugues"] = 16
aluno["idade"] = 18

for chave, valor in aluno["notas"].items():
    print (chave,": ", valor)


print (aluno)


texto = "Marcelo Vieira Amorim"

contagem = {}

for letra in texto:
    letra =letra.lower()
    if letra in contagem.keys():
        contagem[letra] += 1
    else:
        contagem[letra] += 1

print(contagem)
