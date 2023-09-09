Maior_idade = 18
Idade_especial = 16

idade = int(input("informe sua idade: "))
if idade >= Maior_idade:
    print("Maior idade, pode tirar a CNH. ")

if idade < Maior_idade:
    print('ainda não pode tirar a CNH')


if idade >= Maior_idade:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar CNH. ")


if idade >= Maior_idade:
    print("Maior de idade, pode tirar CNH.")
elif idade == Idade_especial:
    print ("pode fazer aulas teoricas, mas não pode fazer as aulas práticas")
else:
    print("Ainda não pode tirar CNH. ")


