from loaders.Races_loader import Load_race
from loaders.Abilities_loader import Load_abilities
from textual.app import App
from textual.screen import Screen
from textual.widgets import ListView, ListItem, Label,Static
from textual.containers import Horizontal, Vertical
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

abilites_path = "data/habilidades.json"
abilities = Load_abilities(abilites_path)

class CreateCharacter(Screen):
    def compose(self):
        yield Label("=== Crear Personaje ===\n")
        with Horizontal():
            yield ListView(
                *[ListItem(Label(r.name), id=r.name) for r in races],
                ListItem(Label("<-- Back"), id="back"),
                id="race_list"
            )

            yield Static(
                "Selecciona una raza...",
                id="race_info"
            )
    def on_list_view_highlighted(self, event: ListView.Highlighted):

        option = event.item.id

        if option == "back":
            self.query_one("#race_info").update("Volver al menú")
            return
        
        race = races[event.list_view.index]
        #race_abilities = abilities[event.list_view.index]

        info= f""" 
        Nombre: {race.name}
        Tamaño: {race.size}
        Velocidad: {race.speed}

        STR: {race.stast["STR"]}
        DEX: {race.stast["DEX"]}
        CON: {race.stast["CON"]}
        WIS: {race.stast["WIS"]}
        CHA: {race.stast["CHA"]}

        Raza: {race.description}
        """
        self.query_one("#race_info").update(info)

    def on_list_view_selected(self, event: ListView.Selected):
        race = races[event.list_view.index]
        option = event.item.id
        if race.name == "Humano":
            estasdisticas=[race.stast["STR"],
                           race.stast["DEX"],
                           race.stast["CON"],
                           race.stast["WIS"],
                           race.stast["CHA"]]
            return estasdisticas
        if option == "back":
            self.app.pop_screen()

    
        


