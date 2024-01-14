livros = {"terror": "sexta13", "Aventura": "Cronicas de narnia", "numero": 30}
#print(livros.items())

for key in livros.items():
    print(key)
print("=-"*10)
for key, val, in livros.items():
        print(f"{key} = {val}")


comidas = []
saudavel = {"tamanho: ": "pequeno", "nome": "acerola"}
tipica = {"tamanho: ": "medio", "nome": "tapioca"}
fastFood = {}        