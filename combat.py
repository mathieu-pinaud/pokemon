import menu
import time

class Combat(menu.Menu):
    def __init__(self):
        menu.Menu.__init__(self)
        self.__type_dommage()

    def __verifier_vie(self):
        if self.mon_poke.GetPv() <= 0 and self.poke_adv.GetPv() <= 0:
            return(3)
        elif self.mon_poke.GetPv() <= 0:
            return(2)
        elif self.poke_adv.GetPv() <= 0:
            return(1)
        return(0)
    
    def __renvoie_gagnant(self):
        winner = self.__verifier_vie()
        if winner == 1:
            return(self.mon_poke.GetNom())
        elif winner == 2:
            return(self.poke_adv.GetNom())
        elif winner == 3:
            return("égalité")
        return(None)
    
    def __renvoie_perdant(self):
        winner = self.__verifier_vie()
        if winner == 1:
            return(self.poke_adv.GetNom())
        elif winner == 2:
            return(self.mon_poke.GetNom())
        elif winner == 3:
            return("égalité")
        return(None)
    
    def __type_dommage(self):
        for i in self.poke_adv.typeResistance:
            if i[0] == self.mon_poke.typeNom:
                self.mes_dommages = self.mon_poke.attaque * i[1]
        for i in self.mon_poke.typeResistance:
            if i[0] == self.poke_adv.typeNom:
                self.dommages_adv = self.poke_adv.attaque * i[1]
    
    def __enleve_pv(self):
        if self.dommages_adv - self.mon_poke.deffense > 0:
            self.mon_poke.SetPv(self.mon_poke.GetPv() - (self.dommages_adv - self.mon_poke.deffense))
        else:
           self.mon_poke.SetPv(self.mon_poke.GetPv() + (self.dommages_adv - self.mon_poke.deffense))
        if self.mes_dommages - self.poke_adv.deffense > 0:
            self.poke_adv.SetPv(self.poke_adv.GetPv() - (self.mes_dommages - self.poke_adv.deffense))
        else:
            self.poke_adv.SetPv(self.poke_adv.GetPv() + (self.mes_dommages - self.poke_adv.deffense))
        if self.mon_poke.GetPv() < 0:
            self.mon_poke.SetPv(0)
        if self.poke_adv.GetPv() < 0:
            self.poke_adv.SetPv(0)

    def __soin(self):
        self.mon_poke.SetPv(100 + self.mon_poke.typePv)
        self.poke_adv.SetPv(100 + self.poke_adv.typePv)
    
    def combat(self):
        i = 1
        while (self.__verifier_vie() ==  0):
            print('\nTour', i)
            i +=1
            self.__enleve_pv()
            self.mon_poke.pokeprint()
            print()
            self.poke_adv.pokeprint()
            print()
            time.sleep(1.5)
        if (self.__verifier_vie() == 3):
            print('Egalité')
        else:
            print('Le gagnant est', self.__renvoie_gagnant())
            print('Le perdant est', self.__renvoie_perdant())
        self.__soin()