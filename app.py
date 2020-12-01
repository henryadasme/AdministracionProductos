from flask import Flask, render_template, request, redirect, url_for
import mantenedorAdministracion
import clasesAdministracion

app = Flask(__name__)

@app.route('/')
def Index():
    datos = mantenedorUsuario.consultar()
    return render_template('administracionUsuarios.html', usuarios=datos)
    #return render_template('administracionUsuarios.html')

@app.route('/mantenedor', methods=['POST'])
def mantenedor():
    if request.method == 'POST':

        #Ingresar usuarios
        try:
            auxBotonInsertar = request.form['btoInsertar']
            if auxBotonInsertar == 'Insertar':
                auxNombre = request.form['txtNombre']
                auxContrasena = request.form['txtContrasena']
                auxRut = request.form['txtRut']
                auxCorreo = request.form['txtCorreo']
                auxUsuario = claseUsuario.usuario(auxNombre, auxContrasena, auxRut, auxCorreo)
                mantenedorUsuario.insertar(auxUsuario)
                print("Datos guardados correctamente")
                flash('datos guardados')
                
        except:
            print("Error al guardar")

        #Actualizar usuario
        try:
            auxBotonActualizar = request.form['btoActualizar']
            if auxBotonActualizar == 'Actualizar':
                auxNombre = request.form['txtNombre']
                auxContrasena = request.form['txtContrasena']
                auxRut = request.form['txtRut']
                auxCorreo = request.form['txtCorreo']
                auxUsuario = claseUsuario.usuario(auxNombre, auxContrasena, auxRut, auxCorreo)
                mantenedorUsuario.actualizar(auxUsuario)
                print("Datos actualizados")
                
        except:
            print("Error al actualizar")

        #Eliminar
        try:
            auxBotonEliminar = request.form['btoEliminar']
            if auxBotonEliminar == 'Eliminar':
                auxRut = request.form['txtRut']
                mantenedorUsuario.eliminar(auxRut)
                print("Usuario eliminado ")
                
        except:
            print("Error al Eliminar")

        return redirect(url_for('Index'))


if __name__ == '__main__':
    app.run(port=3000, debug=True)