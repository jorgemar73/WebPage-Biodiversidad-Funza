#Importar librería sqlite para python
import sqlite3

def locbase():  # Definimos la función locbase, que se encargará de crear la tabla formulario en la base de datos.
    conexiones() # Llamamos a la función conexiones para establecer la conexión con la base de datos.
    try:
        # Intentamos ejecutar una sentencia SQL que crea la tabla formulario con las columnas especificadas.
        # Aquí cada columna tiene un tipo de dato asignado
        conectar.execute("""create table formulario (
                                id_document integer primary key,
                                name1 text,
                                lastname text,
                                correoe text,
                                phone integer,
                                message text
                            )""")
        print("se creo la tabla formulario")
    # Capturamos el error OperationalError que se produce si la tabla formulario ya existe y mostramos
    # un mensaje indicando que la tabla ya existe.                    
    except sqlite3.OperationalError:
        print("La tabla formulario ya existe")                    
    conectar.close() # Cerramos la conexión con la base de datos después de la operación.


def conexiones(): # Definimos la función conexiones que se encargará de conectar con la base de datos.
    global conectar # Declaramos la variable conectar como global para poder usarla en otras funciones del módulo.
    # Establecemos la conexión con la base de datos ubicada en la ruta especificada y asignamos esta conexión a la variable global conectar.
    conectar=sqlite3.connect("D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/db/contactos.db")
# Llamamos a la función locbase para que se ejecute automáticamente al importar el módulo. Esto asegura que la tabla formulario se cree (si no existe) cuando se inicie la aplicación.
locbase()


