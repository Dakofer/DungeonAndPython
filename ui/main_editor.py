import tkinter as tk
from loaders.Races_loader import Load_race
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

#--Variables del jugador--
Name = ""
Race = 0
Class = 0
Feat = []
Money = 0.0
Equipment = []

#--variables globales--
op_race = 0

#--path Json--
races_path = "Races/razas.json"
class Creador_de_Personaje():
    def Selector_races():
        races = Load_race(races_path)
        print(races)

if __name__ == "__main__":
    Creador_de_Personaje.Selector_races()


