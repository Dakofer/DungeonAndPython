import json
from core.models.feat import feat_list
def Load_feat(feat_json):
     # 1. Leer un archivo JSON
    with open(feat_json, 'r', encoding='utf-8') as archivo:
        feat_json = json.load(archivo)
    feats=[]
    for r  in feat_json["feat"]:
        new_races = feat_list(
                         name=r["name"],
                         Requeriment=r["Requeriment"],
                         description=r["description"])
        feats.append(new_races)
    return feats