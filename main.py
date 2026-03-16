from textual.app import App

from screens.main_menu import MainMenu
from screens.create_character import CreateCharacter
from screens.load_character import LoadCharacter
from screens.combat_mode import CombatMode


class RPGApp(App):
    CSS_PATH = "styles/CreatorCharacter.tcss"

    SCREENS = {
        "main_menu": MainMenu,
        "create_character": CreateCharacter,
        "load_character": LoadCharacter,
        "combat_mode": CombatMode,
    }

    def on_mount(self):
        self.push_screen("main_menu")


if __name__ == "__main__":
    app = RPGApp()
    app.run()


