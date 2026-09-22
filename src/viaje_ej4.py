import random 

distancia = 225000000
op = range(10000,50000,10000)
velocidad = random.choice(op)

tiempohoras = distancia/velocidad
tiempo = tiempohoras/24
print(f"Velocidad: {velocidad} -> Tiempo: {tiempo}días")







