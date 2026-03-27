
import mysql.connector

from dao.daoConnect import DBConnect
from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
#metodi che usiamo per interagire con il database
#ce li scriviamo nel dao e poi li usiamo nel modello (gestore ordini)

#tutti i metodi del dao saranno scritti così
class DAO:

    def getAllProdotti(self):
        #cnx = mysql.connector.connect(
            #user = "root",
            #password = "rootroot",
            #host = "127.0.0.1",
           # database = "sw_gestionale"
        #)
        cnx= DBConnect.getConnection()     #devi fare così per tutti i metodi che avevi riscritto uguali
        cursor = cnx.cursor(dictionary = True)
        cursor.execute("Select * from prodotti")
        row = cursor.fetchall()  #lista di dizionari
        res = []
        for p in row:
            res.append(ProdottoRecord(p["nome"],p["prezzo"]))  #creo i dto associati a questa tabella

        cursor.close()
        cnx.close()
        return res

    #facciamo stessa cosa per i clienti
    def getAllClienti(self):
       # cnx = mysql.connector.connect(
       #     user = "root",
       #     password = "rootroot",
        #    host = "127.0.0.1",
        #    database = "sw_gestionale"
       # )
        cnx = DBConnect.getConnection()
        cursor = cnx.cursor(dictionary = True)
        cursor.execute("Select * from prodotti")
        row = cursor.fetchall()  #lista di dizionari
        res = []
        for p in row:
            res.append(ClienteRecord(p["nome"],p["mail"],p["categoria"]))  #creo i dto associati a questa tabella

        cursor.close()
        cnx.close()
        return res

    def addProdotto(self,prodotto):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #    host = "127.0.0.1",
        #    database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query="""insert into prodotti (nome,prezzo) value(%s,%s)"""
        cursor.execute(query, (prodotto.name, prodotto.prezzo_unitario))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def addCliente(self,cliente):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #    host = "127.0.0.1",
        #    database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor()
        query="""insert into clienti (nome,mail,categoria) value(%s,%s)"""
        cursor.execute(query, (cliente.nome, cliente.mail, cliente.categoria))

        cnx.commit()
        cursor.close()
        cnx.close()
        return

    def hasCliente(self, cliente):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #    host = "127.0.0.1",
        #    database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)

        cursor.execute("select * from clienti where mail=%s", (cliente.mail))
        row = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        return len(row)>0  #restituisce true se la dimensione della riga è > 0

    def hasProdotto(self, prodotto):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #    host = "127.0.0.1",
        #    database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)

        cursor.execute("select * from prodotti where name=%s", (prodotto.name))
        row = cursor.fetchall()
        cnx.commit()
        cursor.close()
        cnx.close()
        return len(row)>0

if __name__ == "__main__":
    mydao = DAO()
    mydao.getAllProdotti()