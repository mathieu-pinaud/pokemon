class Pokemon():
    def __init__(self, nom):
        self.__nom = nom
        self.__pv = 100
        self.niveau = 1
        self.attaque = 0
        self.deffense = 0

    def GetNom(self):
        return(self.__nom)
    def GetPv(self):
        return(self.__pv)
    
    def SetPv(self, pv):
        self.__pv = pv
