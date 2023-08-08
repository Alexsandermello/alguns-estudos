# Função para calcular o IMC
def calcular_imc(peso, altura):
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)
    return imc

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Solicitar o peso e altura do usuário
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em cm): "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Classificar o IMC
classificacao = classificar_imc(imc)

# Imprimir o resultado
print("Seu IMC é:", imc)
print("Classificação:", classificacao)