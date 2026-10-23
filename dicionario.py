aluno = {
         "nome": "Carlos",
         "idade": 17, 
         "cidade":"famalicão",
         "disciplinas": ["Matematica","Programção","Ingles"],
         "notas": {"matematica":[17.5,12], "programação":[18,25,13],"ingles":[12.25,7.75]}
         }

#Media de todas as notas
soma = 0
no_notas = 0
for notas_disciplina in aluno["notas"].values():
    soma+= sum(notas_disciplina)
    no_notas+= len(notas_disciplina)

print (aluno["notas"]["programção"][1])
#print(aluno["nome"])
#altero valor de uma chave
aluno["idade"] = 18
#inserir uma  nova chave
aluno["estado_civil"]= "Solteiro"
#print(aluno)
#imprimir as caracteristicas do aluno
for chave in aluno.keys():
    print(F"{chave}", end =" ")
#imprimir somente os valores
for valor in aluno.values():
    print(F"{valor}" , end= "")
#imprimir a chave e o valor
for chave,valor in aluno.items():
    print(F"{chave}:{valor}") 