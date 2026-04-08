import json
from core.models.Character import Character_list
def Object_Character(character_Obj):
    character = Character_list(
        Race=character_Obj[0],
        Class=character_Obj[1],
        Feat=character_Obj[2],
        Stast=character_Obj[3],
        Spell=character_Obj[4],
        Name=character_Obj[5]
    )
    return character
