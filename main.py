
from screens.main_menu import MainMenu
from screens.create_character import CreateCharacter
from screens.load_character import LoadCharacter




def main():
        estado="inicio"
        personaje=None

        while True:
            if estado == "inicio":
                opcion = MainMenu.compose()
                
                if opcion == "1":
                    estado = "crear_personaje"
                elif opcion == "2":
                    break

            elif estado == "crear_personaje":
                personaje = CreateCharacter.compose()
                estado = "inicio"


if __name__ == "__main__":
    main()



