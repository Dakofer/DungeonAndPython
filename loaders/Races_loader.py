import json
from core.models.Races import Races_list
def Load_race(races_json):
     # 1. Leer un archivo JSON
    with open(races_json, 'r', encoding='utf-8') as archivo:
        race_data = json.load(archivo)
    races=[]
    for r  in race_data["razas"]:
        new_races = Races_list(name=r["name"],
                         size=r["size"],
                         description=r["description"],
                         speed=r["speed"],
                         stast=r["stast"])
        races.append(new_races)
    return races
