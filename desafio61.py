primeiroTermo = int(input("primeiro termo: "))
razao = int(input("razao: "))
decimoTerm = primeiroTermo + (10 -1) * razao

i = 1
while primeiroTermo < decimoTerm + razao:
    print(primeiroTermo)
    primeiroTermo += razao

