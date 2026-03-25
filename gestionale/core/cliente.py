from dataclasses import dataclass
#quando uso dao, se ho una tabella cliente devo creare una classe cliente con solo la sua definizione
#e i metodi hash, eq e str

@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    #devo avere per forza la funzione di hash
    def __hash__(self):
        return hash(self.mail)   #la faccio solo di mail
    #delego la funzione di hash del cliente record alla funzione di hash della stringa

    #devo anche avere la funzione __eq__
    def __eq__(self, other):
        return self.mail == other.mail


    def __str__(self):
        return f"{self.nome} -- {self.mail} ({self.categoria})"