from flask import Flask, render_template, request, redirect
import controlador_cliente
lista_busqueda=[]
app = Flask(__name__)


#home

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/formulario_agregar_cliente')
def formulario_agregar_cliente():
    return render_template('agregar_cliente.html')

@app.route('/guardar_clientes', methods=['POST'])
def guardar_cliente():
    try:
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        saldocuenta = request.form['number']
        tipocuenta= request.form['tipocuenta']
        if tipocuenta=='1':
            saldocuenta=saldocuenta
        elif tipocuenta=='2':
            saldocuenta=float(saldocuenta)-(float(saldocuenta)*2)
        elif tipocuenta=='3':
            saldocuenta=float(saldocuenta)*(0)
        controlador_cliente.agregar_clientes(
            nombre, apellido, telefono,saldocuenta)
        return redirect('/clientes')
    except Exception:
        return redirect ('/ex')
        
@app.route('/ex')
def re():
    return redirect ('/guardar_clientes')


@app.route('/clientes')
def clientes():
    clientes = controlador_cliente.obtener_cliente()
    return render_template('clientes.html', clientes=clientes)


@app.route('/eliminar_cliente', methods=['POST'])
def eliminar_cliente():
    controlador_cliente.eliminar_cliente(request.form['codigocliente'])
    return redirect('/clientes')


@app.route('/formulario_editar_cliente/<int:codigocliente>')
def editar_cliente(codigocliente):
    cliente = controlador_cliente.obtener_cliente_por_id(codigocliente)
    return render_template('editar_cliente.html', cliente=cliente)


@app.route('/actualizar_cliente', methods=['POST'])
def actualizar_cliente():
    try:
        codigocliente = request.form['codigocliente']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        global cuenta
        cuenta = request.form['number']
        tipocuenta= request.form['tipocuenta']
        saldo=controlador_cliente.Gestionar_cuenta(codigocliente)
        global saldo2,saldocuenta
        for i in saldo:
            saldo2=i
        if tipocuenta=='1':
            saldocuenta=float(saldo2)+(float(cuenta))
        elif tipocuenta=='2':
            saldocuenta=float(saldo2)-(float(cuenta))
        elif tipocuenta=='3':
            saldocuenta=float(saldo2)+(float(cuenta))
        controlador_cliente.actualizar_cliente(
            nombre, apellido, telefono, saldocuenta,codigocliente)
        return redirect('/clientes')
    except Exception:
        return redirect ('/formulario_editar_cliente')


@app.route('/inicio_sesion', methods=['POST'])
def inicio_sesion ():
    email = request.form["correo"]
    password= request.form["password"]
    login=controlador_cliente.inicio_sesion(email)
    try:
        if password == login[1]:
            return redirect ("clientes")
        else:
            return redirect ("login")
    except Exception:
        return redirect ("/")

@app.route('/buscar_cliente' , methods=['POST'])
def Buscar ():
    telefono = request.form["telefono"]
    clientes = controlador_cliente.buscar_cliente(telefono)
    return render_template ('clientes.html',clientes=clientes)

@app.route('/busqueda')
def busqueda():
    return render_template('buscar.html')


if __name__ == "__main__":
    app.run( port=5000, debug=True)
