class Animal:
    def __init__(self, prenom):
        self.age = 0
        self.prenom = prenom

    def vieillir(self):
        self.age += 1
    def SePresenter(self):
      print("l'animal se nome :", self.prenom)        


animal1 = Animal("luna")
animal1.SePresenter()
print( "Age initial de l'animal :",  animal1.age)
animal1.vieillir()
print("Age de l'animal après vieillissement :", animal1.age)
