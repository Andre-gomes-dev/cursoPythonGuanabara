palavra = input("digite uma palavra:")
reverso = ''.join(reversed(palavra))
print(reverso)

if palavra == reverso:
    print("palindromo")
else:
    print("não é")    
    