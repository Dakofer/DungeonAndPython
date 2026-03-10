from loaders.Races_loader import Load_race
from textual.screen import Screen
from textual.widgets import ListView, ListItem, Label
from textual.containers import Vertical
import os
import json

#---Clases---
#Barbaro
#Bardo
#Brujo
#Clerigo
#Druida
#Explorador (ranger)
#Guerrero
#Hechizero
#Mago
#Monje
#Paladín
#Picaro

#--path Json--
races_path = "data/razas.json"
races = Load_race(races_path)

class CreateCharacter(Screen):
    def compose(self):
        yield Label("=== Crear Personaje ===\n")
        yield ListView(
            *[ListItem(Label(r.name), id=r.name) for r in races],
            ListItem(Label("Salir"), id="exit"),
            id="menu"
        )
    def on_list_view_selected(self, event: ListView.Selected):
        option = event.item.id
        if option == "exit":
            self.app.exit()

    def on_button_pressed(self, event):
        if event.button.id == "back":
            self.app.pop_screen()



