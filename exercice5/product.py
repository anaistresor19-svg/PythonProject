class Product:
    def __init__(self, name, prix, quantite):
        self.name = name
        self.prix = prix
        self.quantite = quantite

    def total_value(self):
        return self.prix * self.quantite

p1 = Product("Laptop", 899.99, 5)
print(p1.name)
print("valeur totale du stock:",  p1.total_value(), "$")