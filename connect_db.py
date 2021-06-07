from settings import DB_PATH, SQL_INIT_PATH
from os import path
import sqlite3


class ConnectDBSQLite:

    @classmethod
    def makeQuerys(self, db, query, params={}, many=False):
        """
            Metodo para ejecutar querys en la BD
        """
        id = 0
        data = []
        error = None
        try:
            cursor = db.cursor()

            if many:
                # Ejecutar querys con muchos parametros
                cursor.executemany(query, params)
            else:
                cursor.execute(query, params)  # Ejecutar querys con parametros

            id = cursor.lastrowid
            data = cursor.fetchall()
            db.commit()
        except Exception as e:
            error = f"Query fallo: {e}"

        return data, id, error

    @classmethod
    def getConnection(self):
        """
            Metodo conectarse a la BD, la crea sino existe
        """
        exists_db = True

        # Verificar existencia de archivo
        if not path.exists(DB_PATH):
            exists_db = False

        # Conectarse a BD
        db = sqlite3.connect(DB_PATH)

        # Crear la BD
        if not exists_db:
            sqlfile = open(SQL_INIT_PATH).read()
            db.cursor().executescript(sqlfile)
        return db

    @classmethod
    def closeDB(self, db):
        """
            Cierra la conexion a la BD
        """
        db.close()
