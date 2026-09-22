import random

distancia = int(input("Introduzca la distancia en km: "))
valor = range(0,distancia,150000)
parada = random.choice(valor)

ls = list()
if distancia <= 150000:
    print("La nave no tendrá que parar a repostar")
else:

    for i in range(0,distancia,150000):
        print(f"parada en el km: {i}")
        ls.append(i)

    h = len(ls)
    print(f"Total de paradas para respostar: " + {h})


  











