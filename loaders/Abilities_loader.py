import json
from core.models.Abilities import Abilities_list
def Load_abilities(abilities_json):
     # 1. Leer un archivo JSON
    with open(abilities_json, 'r', encoding='utf-8') as archivo:
        abilities_json = json.load(archivo)
    abilities=[]
    for r  in abilities_json["abilities"]:
        new_races = Abilities_list(
                         name=r["name"],
                         requisitoXnivel=r["requisitoXnivel"],
                         description=r["description"])
        abilities.append(new_races)
    return abilities

def Load_abilities_races(abilities_json):
     # 1. Leer un archivo JSON
    with open(abilities_json, 'r', encoding='utf-8') as archivo:
        abilities_json = json.load(archivo)
    abilities=[]
    for r  in abilities_json["abilities_class"]:
        new_races = Abilities_list(
                         name=r["name"],
                         requisitoXnivel=r["requisitoXnivel"],
                         description=r["description"])
        abilities.append(new_races)
    return abilities