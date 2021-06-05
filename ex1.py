#start

class Soldato():
    def __init__(self, nome, matricola, reparto):
        self.nome = nome
        self.matricola = matricola
        self.reparto = reparto
        if self.matricola[0]== "A":
            self.reparto="Furieri"

    def __str__(self):
        return f"Soldato {self.nome},\nMatricola: {self.matricola},\nassegnato al Reparto: {self.reparto}"
    def __repr__(self):
        return f"classe Soldato:\nself.nome:{self.nome}\nself.matricola:{self.matricola}\nself.reparto:{self.reparto}"

        
sold1 = Soldato("Mario Rossi","A23232", "Granatieri")

print(sold1)
print(sold1.__repr__())
