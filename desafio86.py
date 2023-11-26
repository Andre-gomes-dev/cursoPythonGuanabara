matriz = [[0,0,0], [0,0,0], [0,0,0]]

for cont in range(0, 3):
    for cont2 in range(0, 3):
        matriz[cont] [cont2] = int(input("adcione um valor na matriz [{},{}]: ".format(cont, cont2))) 
        
        #adcionar na matriz
for cont in range(0, 3):
    for cont2 in range(0, 3):
        #print("{}" ,end="".format(matriz[cont] [cont2]))
        print(f"[{matriz[cont] [cont2]:^5}]", end=" ")
    print()