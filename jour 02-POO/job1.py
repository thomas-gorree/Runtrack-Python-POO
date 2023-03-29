class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est : ", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")
class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee  
personne1 = Personne()
personne1.afficherAge()  
p = Professeur("mathématiques")
personne1.bonjour() 

personne1.modifierAge(25)
personne1.afficherAge()

e = Eleve(age=16)


e.allerEnCours()  
e.affichageAge()  

p.enseigner()  

print("Matière enseignée :", p.getMatiereEnseignee())