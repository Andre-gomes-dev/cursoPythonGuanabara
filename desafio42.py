import math
i = 1
ladosTriang = []
while i <=3:
   indice = input("digite o {}° valor: ".format(i))
   ladosTriang.append(indice)
   i +=1

if ladosTriang[0] == ladosTriang[1] and ladosTriang[1] == ladosTriang[2]:
  print("equilatero")
elif ladosTriang[0] == ladosTriang[1] or ladosTriang[1] == ladosTriang[2] or ladosTriang[0] == ladosTriang[2]:
  print("isosceles")
else:
   print("escaleno")

print(ladosTriang)   