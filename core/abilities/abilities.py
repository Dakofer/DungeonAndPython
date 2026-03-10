from loaders.Abilities_loader import Load_abilities

class Abilities_races:
    def DarkVision():
        races_path = "data/razas.json"
        Abilities = Load_abilities(races_path)
        print(Abilities["Vision Nocturna"])