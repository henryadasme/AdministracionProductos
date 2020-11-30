from flask import Flask,render_template, request, flash, redirect, url_for, session
from flask_mysqldb import MySQL, MySQLdb
import bcrypt

#crear objeto flask
app = Flask(__name__)

#establezo llave secreta
app.secret_key="appLogin"

#configuro
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'carcastore'

#crea objeto mysql
mysql = MySQL(app)

#semilla para encriptamiento
semilla = bcrypt.gensalt()

#se rutean el  home
@app.route("/")
def index():
    return render_template('ingresar.html')
#define la funcion principal
def main():
    if 'nombre' in session:
        # Carga template main.html
        return render_template('inicio.html')
    else:
        #Carga template main.html
        return render_template('ingresa.html' )

#define la ruta index
@app.route("/inicio")

#definde la funcion principal
def inicio():
    #verificar que haya session
    if 'nombre' in session:
        #carga template main.html
        return render_template('inicio.html')
    else:
        return render_template('ingresar.html')

#define la ruta de registro
@app.route("/registrar", methods=["GET", "POST"])

#funcion registrar

def registrar():
    if(request.method=="GET"):

        if 'nombre' in session:
            return render_template('inicio.html')   
        else:
        # obtiene los datos
            return render_template('ingresar.html')
    else:
        #obtiene datos
        nombre     = request.form['nmNombreRegistro']
        correo     = request.form['nmCorreoRegistro']
        contraseña = request.form['nmContraseñaRegistro']
        contraseña_encode = contraseña.encode("utf-8")
        contraseña_encriptado = bcrypt.hashpw(contraseña_encode,semilla)

        #prepara el query para insercion
        sQuery = "INSERT INTO login (correo, contraseña, nombre) VALUES ( %s, %s, %s)"

        # crea cursor de ejecucion

        cur = mysql.connection.cursor()

        #ejecuta la sentencia
        cur.execute(sQuery,(correo,contraseña_encriptado,nombre))

        #ejecuta el comit
        mysql.connection.commit()

        #regiistra la session
        session['nombre'] = nombre
      

        #redirige a index
        return redirect(url_for('inicio'))
    
#define la ruta ingresar
@app.route("/ingresar", methods=["GET","POST"])


def ingresar():
    if(request.method=="GET"):
        if 'nombre' in session:
            return render_template('inicio.html')
        else:
            return render_template('ingresar.html')
    else:
        correo = request.form['nmCorreoLogin']
        contraseña = request.form['nmContraseñaLogin']
        contraseña_encode = contraseña.encode("utf-8") 

        #crear cursor para ejercucion
        cur = mysql.connection.cursor()

        #prepara query

        sQuery = "Select correo, contraseña, nombre From  login where correo = %s"

        #ejecuta la semilla
        cur.execute(sQuery,[correo])

        #obtengo dato
        usuario = cur.fetchone()

        #cierro la consulta
        cur.close()

        #verifico si obtuvo datos
        if (usuario !=None):
            #obtiene el password encriptado encode
            contraseña_encriptado_encode = usuario[1].encode()

            #Verifica contrasena
            if(bcrypt.checkpw(contraseña_encode,contraseña_encriptado_encode)):

                #Registra sesion
                session['nombre'] = usuario[2]
                #redirige la session
                return redirect(url_for('inicio'))
            else:
                flash("La contrasena no es correcta", "alert-warning")

                return render_template('ingresar.html')
        else:

            #mensaje flash
            flash("El correo no existe", "alert-warning")

            return render_template('ingresar.html')      

#define  ruta de salida

@app.route("/salir")

def salir():

    session.clear()

    return redirect(url_for('ingresar'))

#funcion principal
if __name__ == '__main__':
    app.run(debug=True, port=3250)