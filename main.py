#importamos la clase cliente para poder crear los objetos cliente
from agregar_cliente import Cliente 
lista_Cliente=[]


def crear_cliente():
    #funcion para crear un cliente en el sistema
        global cliente_t
        print("""
         ------------------------------
        ******Menú crear cliente******
        ------------------------------""")
        print("*")
        nombre=input("Ingrese el nombre del cliente: ")
        print("*")
        telefono=input("Ingrese el numero telefonico del cliente: ")
        print("*")
        print("1-Abono ** 2-Deuda ** 3-inicia en (0)")
        print("*")
        tipo_cuenta=int(input("Para crear la cuenta debe confirmar si inicia con un abono, deusa o en cero: "))
        print("*")
        if(tipo_cuenta==1):
            cuenta_f=float(input("Ingrese el valor del abono en el que inicia la cuenta: "))
            print("*")
            cuenta=cuenta_f*(-1)
        elif(tipo_cuenta==2):
            cuenta=float(input("Ingrese el valor de la deuda en la que inicia la cuenta: "))
            print("*")
        elif(tipo_cuenta==3):
            cuenta=0.0
        else:
            print("Datos invalidos")
            print("*")
            #Creacion del objeto cliente
        cliente_t=Cliente(nombre,telefono,cuenta)
        lista_Cliente.append(cliente_t)
        s=input("Desea segir creando clientes si/no : ")
        if(s=="si"):
            crear_cliente()
        else:
            print("fin")



def listar():
    #funcion para listar los clientes del siste
    print("")
    print("*******Lista de los clientes*******")
    print("")
    for i in lista_Cliente:
        i.PasarAcadena()



def buscar():
    #funcion para buscar y mostrar en pamtalla un cliente en especifico
    print("Se habilita la opcion de buscar")
    print("")
    tel=input("Ingrese el numero telefonico del cliente: ")
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if tel==lista_Cliente[longitud].numero_telefono:
            print("Nombre:",lista_Cliente[longitud].nombre,"telefono:",lista_Cliente[longitud].numero_telefono,"deuda:",lista_Cliente[longitud].cuenta)
            break
        longitud=longitud-1
    
    if longitud==-1:
        print("el cliente no existe")



def modificar():
    print()
    print("***************se habilito la opcion de modificar*************")
    print("Lista de los clientes")
    for objeto in lista_Cliente:
        objeto.PasarAcadena()
    print()
    celular=input("ingrese el numero telefonico del cliente que desea modificar: ")
    print("")
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if celular==lista_Cliente[longitud].numero_telefono:
            nombreCliente=input("ingrese el nuevo nombre del Cliente")
            
            print("")
            celular=input("ingrese nuevo numero telefonico: ")
            
            print("")
            cuenta=lista_Cliente[longitud].cuenta

            lista_Cliente[longitud].modificar(nombreCliente,celular,cuenta)
            cliente_t.PasarAcadena()
            
            break
        else:
            print("El cliente no existe")
        
        
def eliminar():
    #funcion para eliminar un cliente seleccionado
    print("")
    print("***Se habilito la opcion de eliminar clientes***")
    print("")
    print(lista_Cliente)
    print("")
    tel=input("Ingrese el numero telefonico del cliente a eliminar: ")
    print("")
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if tel ==lista_Cliente[longitud].numero_telefono:
            lista_Cliente.pop(longitud)
            break
        

def cuenta():
    print()
    print("***************se habilito la opcion de gestion de cuentas*************")
    print("Lista de los clientes")
    for objeto in lista_Cliente:
        objeto.PasarAcadena()
    print()
    celular=input("ingrese el numero telefonico del cliente que desea gestionar la cuenta: ")
    
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if celular==lista_Cliente[longitud].numero_telefono:
            des=int(input("la transaccion de la cuenta es un abono o es fiado  1=Abono * 2=Fiado"))
            nombreCliente=lista_Cliente[longitud].nombre
            cuenta=lista_Cliente[longitud].cuenta
            telefono=lista_Cliente[longitud].numero_telefono
            if des==1:
                abono=float(input("De cuanto es el valor del abono: "))
                abono1=abono*-1
                cuenta=cuenta+abono1
                lista_Cliente[longitud].modificar(nombreCliente,telefono,cuenta)
                print("el nuevo valor de la cuenta es")
                cliente_t.PasarAcadena()
            elif des==2:
                abono=float(input("de cuanto es el valor de lo fiado: "))
                cuenta=cuenta+abono
                lista_Cliente[longitud].modificar(nombreCliente,telefono,cuenta)
                print("el nuevo valor de la cuenta es")
                cliente_t.PasarAcadena()
            else:
                print("deccion no valida")
        


crear_cliente()
listar()
cuenta()
listar()
eliminar()
listar()
