from textual.screen import Screen
from textual.widgets import Static, Button
from textual.containers import Vertical

class CombatMode(Screen):
    def compose(self):
        yield Vertical(
            Static("=== Crear Personaje ==="),
            Static("Modo de combate"),
            Button("Volver", id="back")
        )

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.app.pop_screen()



