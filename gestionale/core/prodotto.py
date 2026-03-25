from dataclasses import dataclass
#ho una tabella prodotto, quindi anche un modulo solo con classe prodotto
@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"{self.name} -- {self.prezzo_unitario}"