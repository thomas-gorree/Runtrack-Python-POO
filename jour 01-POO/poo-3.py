class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(resultat)

op = Operation(nombre1=12, nombre2=3)

print("nombre1 :", op.nombre1)
print("nombre2 :", op.nombre2)
"le calcule des deux somme est : ",op.addition()
