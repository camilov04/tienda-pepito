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
        print(" Para crear la cuenta debe confirmar si está inicia con saldo a favor del cliente, con una deuda o en cero  ")
        tipo_cuenta=int(input("1-Saldo a favor ** 2-Deuda ** 3-inicia en (0) : "))
        print("*")
        if(tipo_cuenta==1):
            cuenta_f=float(input("Ingrese el valor del Saldo en el que inicia la cuenta: "))
            print("Se creo el cliente con exicto")
            print("*")
            cuenta=cuenta_f*(-1)
        elif(tipo_cuenta==2):
            cuenta=float(input("Ingrese el valor de la deuda en la que inicia la cuenta: "))
            print("Se creo el cliente con exicto")
            print("*")
        elif(tipo_cuenta==3):
            cuenta=0.0
            print("Se creo el cliente con exicto")
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
            print("*")



def listar():
    #funcion para listar los clientes del siste
    print("")
    print("*******Lista de los clientes*******")
    print("")
    for i in lista_Cliente:
        i.PasarAcadena()
    print("*")



def buscar():
    #funcion para buscar y mostrar en pamtalla un cliente en especifico
    print("Se habilita la opcion de buscar Cliente")
    print("")
    tel=input("Ingrese el numero telefonico del cliente que desea buscar: ")
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if tel==lista_Cliente[longitud].numero_telefono:
            print("Nombre:",lista_Cliente[longitud].nombre,"telefono:",lista_Cliente[longitud].numero_telefono,"deuda:",lista_Cliente[longitud].cuenta)
            break
        longitud=longitud-1
    
    if longitud==-1:
        print("No hay ningun cliente con ese numero en el sistema",tel)



def modificar():
    print()
    print("***************Se habilito la opcion de modificar datos del Cliente*************")
    print("Lista de los clientes")
    for objeto in lista_Cliente:
        objeto.PasarAcadena()
    print("*")
    celular=input("Ingrese el numero telefonico del cliente que desea modificar: ")
    print("")
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if celular==lista_Cliente[longitud].numero_telefono:
            nombreCliente=input("Ingrese el nuevo nombre del Cliente")
            
            print("")
            celular=input("Ingrese el nuevo numero telefonico del Cliente ")
            
            print("")
            cuenta=lista_Cliente[longitud].cuenta

            lista_Cliente[longitud].modificar(nombreCliente,celular,cuenta)
            cliente_t.PasarAcadena()
            
            break
        else:
            print("No hay ningun cliente con ese numero en el sistema",celular)
            print("*")
        
        
def eliminar():
    #funcion para eliminar un cliente seleccionado
    print("")
    print("***Se habilito la opcion de eliminar clientes***")
    print("")
    listar()
    print("")
    tel=input("Ingrese el numero telefonico del cliente que desea eliminar: ")
    print("")
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if tel ==lista_Cliente[longitud].numero_telefono:
            lista_Cliente.pop(longitud)
            print("se elimino los datos del Cliente")
            print("*")
            break
        else:
            print("No hay ningun cliente con ese numero en el sistema",tel)
            print("*")
        

def cuenta():
    print()
    print("***************Se habilito la opcion de gestionar cuentas*************")
    print("Lista de los clientes")
    for objeto in lista_Cliente:
        objeto.PasarAcadena()
    print()
    celular=input("ingrese el numero telefonico del cliente que desea gestionar la cuenta: ")
    print("")
    longitud=len(lista_Cliente)-1
    while longitud >=0:
        if celular==lista_Cliente[longitud].numero_telefono:
            if celular==lista_Cliente[longitud].numero_telefono:
                nombreCliente=lista_Cliente[longitud].nombre
                cuenta=lista_Cliente[longitud].cuenta
                telefono=lista_Cliente[longitud].numero_telefono
                des=int(input("la transaccion de la cuenta es, pago de la  deuda o abono a ellá o aumento en la deuda de lo fiado  1=Abono * 2=Fiado: "))
                if des==1:
                    abono=float(input("De cuanto es el valor del abono: "))
                    abono1=abono*-1
                    cuenta=cuenta+abono1
                    lista_Cliente[longitud].modificar(nombreCliente,telefono,cuenta)
                    print("El nuevo valor de la cuenta es")
                    cliente_t.PasarAcadena()
                elif des==2:
                    abono=float(input("De cuanto es el valor de lo fiado: "))
                    cuenta=cuenta+abono
                    lista_Cliente[longitud].modificar(nombreCliente,telefono,cuenta)
                    print("El nuevo valor de la cuenta es")
                    cliente_t.PasarAcadena()
                else:
                    print("Opcion no valida")
            
            
            
            break
        else:
            print("El cliente no existe")
        

def menu():

    contador = "si"
    while contador == "si":
        print("*********")
        print("**     Menu      **")
        print("*********")
        print()
        print("Si la cueta aparece con numeros negatios es el saldo que tiene el cliente a favor ")
        print("Si el monto aperece con numeros positivos es el saldo ha pagar del cliente ")
        print()
        print("1. si desea agregar un cliente al sistema")
        print("2. si desea listar todos lo clientes  ")
        print("3. si desea buscar un cliente")
        print("4. si desea modificar los datos de un cliente")
        print("5. si desea gestionar las cuentas de los clientes  ")
        print("6. si desea eliminar los datos de un cliente ")
        print()
        print("ingrese la opcion que desea:")
        opcion = input()
        opcion = int(opcion)

        if opcion == 1:
            crear_cliente()
        elif opcion == 2:
            listar()
        elif opcion == 3:
            buscar()
        elif opcion == 4:
            modificar()
        elif opcion==5:
            cuenta()
        elif opcion==6:
            eliminar()
        else:
            print("La opcion ingresada es incorrecta")
        print("*")
        contador = input("Desea continuar con algun proceso  SI/NO:  ")


menu()


