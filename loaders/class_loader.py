import json
from core.models.Class import Class_list
def Load_class(class_json):
     # 1. Leer un archivo JSON
    with open(class_json, 'r', encoding='utf-8') as archivo:
        class_data = json.load(archivo)
    classes=[]
    for r  in class_data["clase"]:
        new_races = Class_list(name=r["name"],
                         HP=r["HP"],
                         HPLevelUp=r["HPLevelUp"],
                         Weapons=r["Weapons"],
                         Armor=r["Armor"],
                         Save_throws=r["Save_throws"],
                         abilities=r["abilities"])
        classes.append(new_races)
    return classes