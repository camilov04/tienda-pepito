from flask import Flask, render_template, request, redirect
import controlador_cliente

app = Flask(__name__)


#home

@app.route('/')
def login():
    return render_template('login.html')




# cliente



@app.route('/agregar_cliente')
def formulario_agregar_cliente():
    return render_template('agregar_cliente.html')


@app.route('/guardar_clientes', methods=['POST'])
def guardar_cliente():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    controlador_cliente.agregar_clientes(
        nombre, apellido, telefono)
    return redirect('/home')



@app.route('/clientes')
def clientes():
    clientes = controlador_cliente.obtener_cliente()
    return render_template('clientes.html', clientes=clientes)


@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    controlador_cliente.eliminar_cliente(request.form['codigocliente'])
    return redirect('/home')


@app.route('/formulario_editar_cliente/<int:codigocliente>')
def editar_cliente(codigocliente):
    cliente = controlador_cliente.obtener_cliente_por_id(codigocliente)
    return render_template('editar_cliente.html', cliente=cliente)


@app.route('/actualizar_cliente', methods=['POST'])
def actualizar_cliente():
    codigocliente = request.form['codigocliente']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    controlador_cliente.actualizar_cliente(
        nombre, apellido, telefono, codigocliente)
    return redirect('/clientes')


@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion ():
    email = request.form["correo"]
    password = request.form["password"]
    login=[]=controlador_cliente.inicio_sesion(email, password)
    try:
        if email == login[0] and password == login[1]:
            return redirect ("clientes")
        else:
            return "Error dstos no corresponden"
    except Exception as error:
        return redirect ("login")

'''
@app.route('./buscar_cliente' , methods=['POST'])
def Buscar ():
    telefono = request.form["telefono"]
    telefono = controlador_cliente.buscar_cliente(telefono)

    if telefono == telefono[3]:
        return redirect ("buscar_cliente")

    else:
        return "registro no encontrado"
'''

if __name__ == "__main__":
    app.run( port=5000, debug=True)
