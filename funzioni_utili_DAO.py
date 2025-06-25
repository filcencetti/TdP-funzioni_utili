#funzione del DAO per prendere parametri dal database
@staticmethod
    def getYears(se serve mettere un parametro. es. year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(row["..."])

        cursor.close()
        conn.close()
        return result

# funzione del DAO per prendere NODI dal database
@staticmethod
    def getYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ """

        cursor.execute(query)

        for row in cursor:
            result.append(Oggetto(**row))

        cursor.close()
        conn.close()
        return result


#funzione del DAO per prendere ARCHI dal database
@staticmethod
    def getYears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ """

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(row["nodo1"], row["nodo2"], row["peso"]))

        cursor.close()
        conn.close()
        return result