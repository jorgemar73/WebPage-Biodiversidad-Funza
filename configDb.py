#Importar librería sqlite para python
import sqlite3

def locbase():
    conexiones()
    try:
        conectar.execute("""create table formulario (
                                id_document integer primary key,
                                name1 text,
                                lastname text,
                                correoe text,
                                phone integer,
                                message text
                            )""")
        print("se creo la tabla formulario")                        
    except sqlite3.OperationalError:
        print("La tabla formulario ya existe")                    
    conectar.close()

def conexiones():
    global conectar
    conectar=sqlite3.connect("D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/db/contactos.db")
locbase()


