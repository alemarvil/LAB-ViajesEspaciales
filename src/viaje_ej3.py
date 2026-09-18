

edad = int(input("introduce tu edad: "))
nivel_fisico = int(input("introduce tu nivel fisico del 0 al 10: "))

if nivel_fisico < 5 or edad < 18:

    if nivel_fisico < 5:
        print("Debes estar en mejor forma.")
    if edad < 18:
        print("Debes ser mayor de edad.")
else: 
    print("¡Listo para despegar!")

