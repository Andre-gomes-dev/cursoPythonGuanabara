nomeCompleto = input("digite seu nome completo")
nomePartido = nomeCompleto.split()

primeiroNome = nomePartido[0]
ultimoNome = nomePartido[-1]
print("o seu primeiro nome é: {} e o ultimo é: {}".format(primeiroNome, ultimoNome))