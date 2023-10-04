import math
catOpos= float(input("qual o valor do cateto oposto: "))
catAdjc = float(input("qual o valor do cateto adjacente: "))

hipotenusa = math.hypot(catAdjc, catOpos) 
print("a hipotenusa é: {:.2f}".format(hipotenusa))


