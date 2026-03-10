from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical
import json

class LoadCharacter(Screen):
    def compose(self):
        yield Vertical(
            Static("=== Crear Personaje ==="),
            Static("Aquí se carga de personaje"),
            Button("Volver", id="back")
        )

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.app.pop_screen()



