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
            print('aqui bien')
            conexion.commit()
            print('como voy')
            conexion.close()
            """ with sql.connect("D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/db/contactos.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO formulario (id_document,name1,lastname,correoe,phone,message) VALUES (?,?,?,?,?,?)",(id_document,name1,lastname,correoe,phone,message) )
                print('vamos bien')
                con.commit() """
            print('la ca')
                #msg = "Record successfully added"
        except:
            print('poseemos problema')
            conexion.rollback()
            msg = "error in insert operation"
        finally:
            #return render_template("D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/templates/datos.html",msg = msg)
            conexion.close()

@app.route('/list')
def list():
    con = sql.connect("D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/db/contactos.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from formulario")

    rows = cur.fetchall();
    return render_template("D:/BOOTCAMP/PAGINA_WEB_BIODIVERSIDAD_FUNZA_V3/templates/datos.html",rows = rows)

if __name__ == '__main__':
    app.run(debug = True)