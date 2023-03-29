class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print("J'ai", self.age, "ans.")
    
    def bonjour(self):
        print("Hello!")
    
    def modifierAge(self, age):
        self.age = age
        
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours.")
        
    def affichageAge(self):
        print("J'ai", self.age, "ans.")
        
class Professeur(Personne):
    def __init__(self, age, MatierENseigner):
        super().__init__(age)
        self.MatierENseigner = MatierENseigner
        
    def enseigner(self):
        print("Le cours va commencer.")
# Instanciation d'un objet Personne
personne = Personne()

# Instanciation d'un objet Eleve
eleve = Eleve()

# Afficher l'age par défaut de l'élève
eleve.afficherAge()

# Redéfinir l'age de l'élève à 15 ans
eleve.modifierAge(15)

# Faire dire bonjour à l'élève et lui faire dire qu'il va en cours
eleve.bonjour()
eleve.allerEnCours()

# Instanciation d'un objet Professeur
professeur = Professeur(age=40, MatierENseigner="Mathématiques")