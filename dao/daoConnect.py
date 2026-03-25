import mysql

#così non devi riscrivere sta parte ogni volta nel dao
#noi creiamo una connessione una sola volta e la usiamo per tutti metodi della classe dao
@classmethod
class DBConnect:
    def getConnection(cls):   #i classmethod non hanno self ma cls

      try:
        cnx = mysql.connector.connect(
            user ="root",
        password = "rootroot",
        host ="127.0.0.1",
        database = "sw_gestionale")
        return cnx
      except mysql.connector.Error as err:
          print("non riesco a collegare il db")
