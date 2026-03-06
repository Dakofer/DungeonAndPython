import json

class Races_list:
    def __init__(self,name,size,description,stast):
        self.name = name
        self.size = size
        self.description = description
        self.stast = stast
        
    def __repr__(self):
        return f"<Race {self.name}>"




    
