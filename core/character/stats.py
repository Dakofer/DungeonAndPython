
class Estadisticas():
    def __init__(self,Str,Dex,Con,Int,Wis,Cha):
        self.Str = Str #Strength
        self.Dex = Dex #Dexterity
        self.Con = Con #Contitution
        self.Int = Int #Intelligence
        self.Wis = Wis #Wisdom
        self.Cha = Cha #Charisma

    def StastInicial(self):
        self.Str = 8
        self.Dex = 8 
        self.Con = 8 
        self.Int = 8 
        self.Wis = 8 
        self.Cha = 8
        return Estadisticas[self.Str,self.Dex,self.Con,self.Int,self.Wis,self.Cha] 