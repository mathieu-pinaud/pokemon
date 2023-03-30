import mes_types.feu as feu
import mes_types.terre as terre
import mes_types.eau as eau
import mes_types.normal as normal
import pokemon

class Type(pokemon.Pokemon, feu.Feu, eau.Eau, terre.Terre, normal.Normal):
    def __init__(self, mon_type, nom):
        pokemon.Pokemon.__init__(self, nom)
        self.listeType = [('feu', feu.Feu), ('eau', eau.Eau), ('terre', terre.Terre), ('normal', normal.Normal)]
        self.Gettype(mon_type)
        self.SetPv(self.GetPv() + self.typePv)
        self.attaque = self.typeAttaque
        self.deffense = self.typeDeffense
    
    def Gettype(self, mon_type):
        for type in self.listeType:
            if type[0] == mon_type:
                type[1].__init__(self)
    
    def pokeprint(self):
        print('Nom:', self.GetNom(), '\nType:', self.typeNom, '\nVie:', self.GetPv(), '\nAttaque', self.attaque, '\nDeffense', self.deffense) 