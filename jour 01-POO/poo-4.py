class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
      print("bonjour, je m'appelle : " +self.nom+self.prenom)  

        
personne1 = Personne("John ", "Doe")
personne1.SePresenter()

personne1 = Personne("Jean ", "Dupond")
personne1.SePresenter()