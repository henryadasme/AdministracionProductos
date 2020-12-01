from flask import Flask, render_template, request, redirect, url_for
import mantenedorAdministracion
import clasesAdministracion

app = Flask(__name__)

@app.route('/mantenedorEmpleado')
def mantenedorEmpleado():
    return render_template('adminEmple.html')

@app.route('/mantenedorProducto')
def mantenedorProducto():
    return render_template('adminProd.html')

@app.route('/mantenedorProveedor')
def mantenedorProveedor():
    return render_template('adminProv.html')

@app.route('/mantenedorUsuarios')
def mantenedorUsuarios():
    #datos = mantenedorUsuario.consultar()
    return render_template('adminUsuarios.html')
    #return render_template('administracionUsuarios.html')

@app.route('/')
def Index():
    return render_template('inicio.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)