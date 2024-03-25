from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('empresa.html')
def WriteFile(usuario, Age, Password, Email, Empresa): #Funcion para escribir en un fichero
    with open(r"C:\Users\anass\OneDrive\Desktop\Formulario de empresa\BBDD\BASE DE DATOS.txt", mode="a") as fichero:
        fichero.write("\n --------------------------------- \n USER:" + usuario + "\n AGE: " + Age + "\n PASSWORD: " + Password + "\n EMAIL: " + Email + "\n EMPRESA: " + Empresa)
def registrarDatos(usuario, Age, Password, Email, Empresa): #Funcion para registrar datos en base de datos
    conexion1=mysql.connector.connect(host="localhost",
                                  user="root",
                                  passwd="",
                                  database="empresa")
    cursor1=conexion1.cursor()
    sql="INSERT INTO `trabajadores`(`ID`, `Nombre`, `EDAD`, `PASSWORD`, `EMAIL`, `EMPRESA`)" + "VALUES (NULL,%s,%s,%s,%s,%s)"
    datos=(usuario, Age, Password, Email, Empresa)
    cursor1.execute(sql, datos)
    conexion1.commit()
    conexion1.close()

@app.route('/usuario', methods=['GET'])
def datos_usuario():
    usuario = request.args.get('usuario')
    Age = request.args.get('edad')
    Password = request.args.get('Password')
    Email = request.args.get('Email')
    Empresa = request.args.get('Empresa')
    WriteFile(usuario, Age, Password, Email, Empresa)
    registrarDatos(usuario, Age, Password, Email, Empresa)
    return render_template('Confirmation.html', usuario=usuario, Age=Age, Password=Password, Email=Email, Empresa=Empresa)

app.run(host='localhost', port=5000, debug=True)