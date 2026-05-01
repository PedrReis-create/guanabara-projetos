from math import sqrt

caop = float(input('Digite o comprimento do cateto oposto : '))
caad = float(input('Digite o comprimento do cateto adjacente : '))
hip = sqrt(caop**2 + caad**2)
print(f'A hipotenusa tem comprimento de : {hip}')