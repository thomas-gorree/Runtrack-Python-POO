class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    # Accesseurs et mutateurs pour les attributs privés
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def volume(self):
        return self.surface() * self.__hauteur
    
    # Accesseur et mutateur pour l'attribut privé
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur 



# Instanciation de la classe Rectangle
mon_rectangle = Rectangle(5, 3)

# Vérification des méthodes
print(mon_rectangle.perimetre())  # Output: 16
print(mon_rectangle.surface())  # Output: 15

# Utilisation des accesseurs et mutateurs pour modifier les attributs privés
mon_rectangle.set_longueur(8)
mon_rectangle.set_largeur(4)

# Vérification des méthodes avec les nouveaux attributs
print(mon_rectangle.perimetre())  # Output: 24
print(mon_rectangle.surface())  # Output: 32


# Instanciation de la classe Parallelepipede
mon_parallelepipede = Parallelepipede(5, 3, 2)

# Vérification des méthodes de la classe Rectangle héritées par la classe Parallelepipede
print(mon_parallelepipede.perimetre())  # Output: 16
print(mon_parallelepipede.surface())  # Output: 15

# Vérification de la méthode volume de la classe Parallelepipede
print(mon_parallelepipede.volume())  # Output: 30

# Utilisation des accesseurs et mutateurs pour modifier l'attribut privé de la classe Parallelepipede
mon_parallelepipede.set_hauteur(4)

# Vérification de la méthode volume avec le nouvel attribut
print(mon_parallelepipede.volume())  # Output: 60