from flask import Flask, render_template, request
from configDb import *
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_contact',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            name1 = request.form['name1']
            lastname = request.form['lastname']
            id_document = request.form['id_document']
            correoe = request.form['correoe']
            phone = request.form['phone']
            message = request.form['message']
            conexion = sql.connect("D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/db/contactos.db")
            conexion.execute("insert into formulario (id_document,name1,lastname,correoe,phone,message) VALUES (?,?,?,?,?,?)",(id_document,name1,lastname,correoe,phone,message) )
            conexion.commit()

            return render_template('index.html')
            
        except sqlite3.OperationalError:
            print ("Oops! This was an operational error. Try again...")
            
        except sqlite3.NameError:
            print ("Name Error")

        except sqlite3.ValueError:
            print ("value error")

        except sqlite3.IOError:
            print ("IO error")
        
    conexion.close()


if __name__ == '__main__':
    app.run(debug = True)