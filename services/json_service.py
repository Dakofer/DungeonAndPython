import json
class ExportCharacter():
    def __init__(self, data):
        
        with open(f'Saves/{data['Name']}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        input("Archivo JSON generado exitosamente...")
        





