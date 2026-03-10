from textual.app import App, ComposeResult
from textual.widgets import ListView, ListItem, Label
from textual.screen import Screen


class MainMenu(Screen):

    def compose(self) -> ComposeResult:
        yield Label("=== RPG TERMINAL ===\n")

        yield ListView(
            ListItem(Label("Crear personaje"), id="create"),
            ListItem(Label("Cargar personaje"), id="load"),
            ListItem(Label("Modo combate"), id="combat"),
            ListItem(Label("Salir"), id="exit"),
            id="menu"
        )

    def on_list_view_selected(self, event: ListView.Selected):

        option = event.item.id

        if option == "create":
            self.app.push_screen("create_character")

        elif option == "load":
            self.app.push_screen("load_character")

        elif option == "combat":
            self.app.push_screen("combat_mode")

        elif option == "exit":
            self.app.exit()


class RPGApp(App):

    SCREENS = {
        "main_menu": MainMenu,
    }

    def on_mount(self):
        self.push_screen("main_menu")


if __name__ == "__main__":
    app = RPGApp()
    app.run()
