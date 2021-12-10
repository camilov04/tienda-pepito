from bd import obtener_conexion


def agregar_clientes(nombre, apellido,  telefono,):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('INSERT INTO cliente(cedula, nombre, apellido, fechanacimiento, telefono) VALUES (%s,%s,%s)',
                       (nombre, apellido, telefono))
    conexion.commit()
    conexion.close()


def obtener_cliente():
    conexion = obtener_conexion()
    clientes = []
    with conexion.cursor() as cursor:
        cursor.execute('SELECT cliente.codigocliente as codigocliente, cliente.nombre as nombre, cliente.apellido as apellido, cliente.telefono as telefono FROM tiendaPepito.cliente')
        clientes = cursor.fetchall()
        conexion.close()
        return clientes


def eliminar_cliente(codigocliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            'DELETE FROM  cliente USING cliente WHERE cliente.codigocliente = %s', (codigocliente))
    conexion.commit()
    conexion.close()


def actualizar_cliente(nombre, apellido, telefono, codigoclinte):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('UPDATE cliente SET nombre = %s, apellido =  %s, telefono = %s WHERE codigocliente = %s',
                       (nombre, apellido, telefono, codigoclinte))
    conexion.commit()
    conexion.close()

# funcion que permite ver los datos de un cliente cuando este se va a editar


def obtener_cliente_por_id(codigocliente):
    conexion = obtener_conexion()
    clientes = None
    with conexion.cursor() as cursor:
        cursor.execute('SELECT cliente.codigocliente as codigocliente, cliente.nombre as nombre, cliente.apellido as apellido, cliente.telefono as telefono FROM tiendaPepito.cliente WHERE codigocliente = %s', (codigocliente,))
        clientes = cursor.fetchone()
    conexion.close()
    return clientes

#Inicio sesion 
def inicio_sesion(email, password):
    conexion = obtener_conexion()
    administrador=None
    with conexion.cursor() as cursor:
        cursor.execute('SELECT  login.correo as correo, login.password as password FROM tiendaPepito.login WHERE correo = %s and password=%s', (email)(password) )
        administrador = cursor.fetchone()
    conexion.close()
    return administrador


#buscar cliente
def buscar_cliente (telefono):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT cliente.codigocliente as codigocliente, cliente.nombre as nombre, cliente.apellido as apellido, cliente.telefono as telefono FROM tiendaPepito.cliente WHERE telefono =  %s',(telefono)  )
        cliente = cursor.fetchall()
        conexion.close()
        return cliente


    
