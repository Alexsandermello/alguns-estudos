saldo = 3000
saque = 3500

status = "sucesso" if saldo >= saque else "falha"

print(f"{status} ao realizar saque!")