class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def add(self, longueur, largeur):
      return longueur + largeur + longueur + largeur

    def multiply(self, longueur, largeur):
        return longueur * largeur

rec = Rectangle(10,4)
print(rec.add(10,4))
print(rec.multiply(10,4))