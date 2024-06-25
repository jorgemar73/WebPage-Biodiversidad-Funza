# Importar flask como microframework; render para las plantillas html y request para manejo de datos de solicitudes http
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd
from configDb import *
from graficaDf import final_df
# Importamos la biblioteca sqlite3 para interactuar con la base de datos SQLite y la renombramos como sql
import sqlite3 as sql
import seaborn as sns
from io import BytesIO
import base64


# Creamos una instancia de la clase Flask y la asignamos a la variable app. El argumento __name__ es una variable especial que define el nombre del módulo actual.
# Flask la usa para encontrar archivos estáticos y plantillas.
app = Flask(__name__)

# @app.route('/'): Un decorador que define la URL (ruta) que activará la función que sigue. En este caso, '/' corresponde a la página principal.


@app.route('/')
# Definimos la función index que será ejecutada cuando se acceda a la ruta '/'.
def index():
    # Renderiza y devuelve el archivo HTML index.html.
    return render_template('index.html')


@app.route('/submit_contact', methods=['POST', 'GET'])
# Define una ruta que puede manejar tanto solicitudes POST como GET. Las solicitudes POST se utilizan para enviar datos al servidor, mientras que las solicitudes
# GET se utilizan para solicitar datos.

# Definimos la función addrec que se ejecuta cuando se accede a la ruta /submit_contact.
def addrec():
    
    # Verificamos si la solicitud es de tipo POST.
    if request.method == 'POST':
        try:
            # Accedemos a los datos del formulario enviados a través de la solicitud POST.
            name1 = request.form['name1']
            lastname = request.form['lastname']
            id_document = request.form['id_document']
            correoe = request.form['correoe']
            phone = request.form['phone']
            message = request.form['message']
            conexion = sql.connect(
                "D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/db/contactos.db") # Establecemos una conexión con la base de datos SQLite.
            conexion.execute("insert into formulario (id_document,name1,lastname,correoe,phone,message) VALUES (?,?,?,?,?,?)",
                            (id_document, name1, lastname, correoe, phone, message)) # Ejecutamos una sentencia SQL para insertar los datos del formulario
            # en la tabla formulario.
            conexion.commit()  # Guardamos los cambios en la base de datos.

            return render_template('index.html') # Renderiza y devuelve el archivo HTML index.html.

        # Manejo de errores para diferentes tipos de excepciones que podrían ocurrir durante la operación de la base de datos.
        except sqlite3.OperationalError:
            print("Oops! This was an operational error. Try again...")

        except sqlite3.NameError:
            print("Name Error")

        except sqlite3.ValueError:
            print("value error")

        except sqlite3.IOError:
            print("IO error")

# Cerramos la conexión con la base de datos después de que se completa la operación.
    conexion.close()

# Generar gráfica en html
def upload():
    table_html = final_df.to_html(classes="table table-striped")
    #Crear el gráfico
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=final_df, x='Especie', y='Registro')
    plt.xlabel('2023')
    plt.ylabel('Cantidad de Registros')
    plt.title('Registros de Especies de Flora en el departamento de Cundinamarca')
    plt.tight_layout()
    #Guardar el gráfico en el buffer de memoria
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    #Codificar el gráfico en base64
    graph_encoded = base64.b64encode(buffer.getvalue()).decode('utf-8')
    graph_html = f'<img src="data:image/png;base64,{graph_encoded}" alt="Gráfico">'
    
    return render_template('D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/templates/contacto.html', table_html=table_html, graph_html=graph_html)

# Verifica si el archivo se está ejecutando directamente (no importado como un módulo).
if __name__ == '__main__':
    
    # Ejecuta la aplicación Flask en modo de depuración. Esto proporciona información detallada
    # sobre los errores y permite reiniciar automáticamente el servidor cuando se hacen cambios en el código.
    app.run(debug=True)
