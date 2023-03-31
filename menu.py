import type

class Menu(type.Type):
    def __init__(self):
        self.mon_poke = self.__menu_pokemon(0)
        self.poke_adv = self.__menu_pokemon(1)

    def __menu_pokemon(self, i):
        if i == 0:
            print('Vous allez choisir votre Pokemon')
        else:
            print('Vous allez choisir le Pokemon adverse')
        j = -1
        while j == -1:
            try:
                j = int(input('Tapez 1 pour choisir un pokemon existant ou 2 pour en créer un '))
            except ValueError:
                j = -1
            if j == 1:
                return(self.__choix_pokemon())
            elif j == 2:
                return(self.__creation_pokemon())
            else:
                j = -1
                print('saisie incorrecte')
    
    def __choix_pokemon(self):
        i =- 1
        l_pokemon = [type.Type('feu', 'Salamèche'), type.Type('eau', 'Carapuce'), type.Type('terre', 'Bulbizarre'), type.Type('normal', 'Ratatouille')]
        print('Tapez 1 pour choisir un Salameche (type feu)')
        print('Tapez 2 pour choisir un Carapuce (type eau)')
        print('Tapez 3 pour choisir un Bulbizzare (type terre)')
        print('Tapez 4 pour choisir un Ratatouille (type normal)')
        while i == -1:
            try:
                i = int(input())
            except ValueError:
                i = -1
            if i > 0 and i < 5:
                return(l_pokemon[i - 1])
            else:
                print('saisie incorrecte')
                i = -1

    def __creation_pokemon(self):
        i = 0
        l_types = ['feu', 'eau', 'terre', 'normal']
        nom = input('Donnez un nom ')
        print('Tapez 1 pour creer un pokemon de type feu')
        print('Tapez 2 pour creer un pokemon de type eau')
        print('Tapez 3 pour creer un pokemon de type terre')
        print('Tapez 4 pour creer un pokemon de type normal')
        while i == 0:
            try:
                i = int(input())
            except ValueError:
                i = 0
            if (i > 0 and i < 5):
                return(type.Type(l_types[i - 1], nom))
            else:
                print("Saisie incorecte")
                i = 0            