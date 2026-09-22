

distancia_km = int(input("Introduce la distancia en km: "))
velocidad_kmh = int(input("Introduce la velocidad en km/h: "))
tiempo_horas = distancia_km / velocidad_kmh
dias_enteros = int(tiempo_horas // 24)
semanas = dias_enteros // 7
dias = dias_enteros % 7
                   
print(f"Tardarías {semanas} semanas y, {dias} días en llegar.")
