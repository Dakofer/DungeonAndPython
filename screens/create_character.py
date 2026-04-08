from loaders.Races_loader import Load_race
from loaders.class_loader import Load_class
from loaders.feat_loader import Load_feat
from core.character.character import Object_Character
from services.json_service import ExportCharacter

import os
import json
import time

#--path Json--
races_path = "data/razas.json"
races = Load_race(races_path)

class_path = "data/clases.json"
classes = Load_class(class_path)

feat_path = "data/dotes.json"
feats = Load_feat(feat_path)

#buypoint values test
BP = 15 # cambiar a 15

class CreateCharacter():
    def Stast(raza_stast):
        Str,Dex,Con,Int,Wis,Cha= 10,10,10,10,10,10
        buypoint = BP  
        stast=[]
        for rs in raza_stast.values():
            stast.append(rs)
        
        while True:
            os.system("cls")

            if buypoint == 0:
                print("=== Crear Personaje ===\n")
                print("=== Asignacion de estadisticas ===\n")
                print("1 Str: ",Str + stast[0])
                print("2 Dex: ",Dex + stast[1])
                print("3 Con: ",Con + stast[2])
                print("4 Int: ",Int + stast[3])
                print("5 Wis: ",Wis + stast[4])
                print("6 Cha: ",Cha + stast[5])
                confirmto = input("Estas sastifecho con tu resultado (si o no): ").lower()

                if confirmto == "si":
                    return [Str+stast[0],Dex+stast[1],Con+stast[2],Int+stast[3],Wis+stast[4],Cha+stast[5]]                
                    break
                elif confirmto == "no":
                    Str,Dex,Con,Int,Wis,Cha= 10,10,10,10,10,10
                    buypoint = BP
                else:
                    print("no existe esa opcion...") 
                    
            print("=== Crear Personaje ===\n")
            print("=== Asignacion de estadisticas ===\n")
            print("1 Str: ",Str," + ",stast[0])
            print("2 Dex: ",Dex," + ",stast[1])
            print("3 Con: ",Con," + ",stast[2])
            print("4 Int: ",Int," + ",stast[3])
            print("5 Wis: ",Wis," + ",stast[4])
            print("6 Cha: ",Cha," + ",stast[5])
            print("puntos restantes ",buypoint)
            select = input("selecciona: ")
            plusminus= input("+ o - ")
                    
            match select:
                case "1": # Fuerza
                    if plusminus == "+" and Str < 15:
                        if Str >= 13:
                            Str += 1
                            buypoint -= 2
                        else:
                            Str += 1
                            buypoint -= 1
                        os.system("cls")

                    elif plusminus == "-" and Str > 8:
                        if Str >= 13:
                            Str -= 1
                            buypoint += 2
                        else:
                            Str -= 1
                            buypoint += 1
                        os.system("cls")

                case "2": # Destreza
                    if plusminus == "+" and Dex < 15:
                        if Dex >= 13:
                            Dex += 1
                            buypoint -= 2
                        else:
                            Dex += 1
                            buypoint -= 1

                    elif plusminus == "-" and Dex > 8:
                        if Dex >= 13:
                            Dex -= 1
                            buypoint += 2
                        else:
                            Dex -= 1
                            buypoint += 1
                        os.system("cls")

                case "3": # Contitucion
                    if plusminus == "+" and Con < 15:
                        if Con >= 13:
                            Con += 1
                            buypoint -= 2
                        else:
                            Con += 1
                            buypoint -= 1
                        os.system("cls")

                    elif plusminus == "-" and Con > 8:
                        if Con >= 13:
                            Con -= 1
                            buypoint += 2
                        else:
                            Con -= 1
                            buypoint += 1
                        os.system("cls")

                case "4": # Inteligencia
                    if plusminus == "+" and Int < 15:
                        if Int >= 13:
                            Int += 1
                            buypoint -= 2
                        else:
                            Int += 1
                            buypoint -= 1
                        os.system("cls")

                    elif plusminus == "-" and Int > 8:
                        if Int >= 13:
                            Int -= 1
                            buypoint += 2
                        else:
                            Int -= 1
                            buypoint += 1
                        os.system("cls")
                    
                case "5": # Sabiduria
                    if plusminus == "+" and Wis < 15:
                        if Wis >= 13:
                            Wis += 1
                            buypoint -= 2
                        else:
                            Wis += 1
                            buypoint -= 1
                        os.system("cls")

                    elif plusminus == "-" and Wis > 8:
                        if Wis >= 13:
                            Wis -= 1
                            buypoint += 2
                        else:
                            Wis -= 1
                            buypoint += 1
                        os.system("cls")

                case "6": # Carisma
                    if plusminus == "+" and Cha < 15:
                        if Cha >= 13:
                            Cha += 1
                            buypoint -= 2
                        else:
                            Cha += 1
                            buypoint -= 1
                        os.system("cls")

                    elif plusminus == "-" and Cha > 8:
                        if Cha >= 13:
                            Str -= 1
                            buypoint += 2
                        else:
                            Cha -= 1
                            buypoint += 1
                        os.system("cls")
    def SaveCharacter(character):
        objCharacter = Object_Character(character)

        obj_dict = vars(objCharacter)  # convierte a diccionario

        ExportCharacter(obj_dict)

    def compose():
        character=[]
        while True:
            os.system("cls")

            print("=== Crear Personaje ===\n")
            print("=== Selector de raza ===\n")

            race_dict = {r.name.lower(): r for r in races}
            for  r in race_dict:
                print(r)
            
            raza_select=input("Selecciona una raza: ").lower()

            if raza_select == "exit":
                break
            else:
                if raza_select  in race_dict:
                    character.append(raza_select)
                    raza_stast = race_dict[raza_select]
                    stast_race = raza_stast.stast
                    print("Haz decidido ser un ",raza_select)
                    time.sleep(0.5)
                    os.system("cls")

                    print("=== Crear Personaje ===\n")
                    print("=== Selector de clases ===\n")
                    
                    class_dict = {c.name.lower(): c for c in classes}
                    for  r in class_dict:
                        print(r)
                    class_select = input("Selecciona: ")
                    if raza_select == "exit":
                        break
                    else:
                        if class_select in class_dict:
                            character.append(class_select)
                            print("Tu clase es ",class_select)
                            time.sleep(0.5)

                            if class_select == "Spell_caster":
                                character.append(None)
                            else:
                                character.append(None)

                            if raza_select == "humano":
                                os.system("cls")
                                feat_dict = {f.name.lower():f for f in feats}
                                for f in feat_dict:
                                    print(f)
                                feat_select=input("Selecciona tu dote: ")
                                if feat_select in feat_dict:
                                    character.append(feat_select)
                            else:
                                character.append(None)

                            #aqui va la funcion para asignar estadisticas
                            Stasdistic = CreateCharacter.Stast(stast_race)

                            character.append(Stasdistic)
                            #agregar la capacidad de elegir hechizos y condicional para determinar si la clase posse la habilidad de "SpellCasting"
                            os.system("cls")
                            Nombre=input("Como se llamara tu personaje: ")
                            character.append(Nombre)

                            os.system("cls")
                            for i in character:
                                print(i)
                            input("quieres guardar (preciona cualquier tecla)") 

                            CreateCharacter.SaveCharacter(character)
                            break 
                                    
                else:
                    print("Error: no exite esta raza")
                    time.sleep(0.5)
        

        
    
        


