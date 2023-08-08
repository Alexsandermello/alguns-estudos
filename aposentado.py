#aposentei
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2023 - ano_nascimento
print("sua idade é de " , idade, "anos")
if idade >= 65:
    print("Vai aposentar!!!")
else:
    print("Infelizmente não vai aposentar")