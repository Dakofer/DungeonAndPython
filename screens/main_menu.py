import os
class MainMenu():

    def compose():
        os.system("cls")
        print("=== RPG TERMINAL ===\n")

        print("Crear personaje")
        print("Cargar personaje")
        print("Salir")
        opcion = input("Selecciona: ")
        return opcion

