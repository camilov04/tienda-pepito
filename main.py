#importamos la clase cliente para poder crear los objetos cliente
from agregar_cliente import Cliente 
lista_Cliente=[]


def crear_cliente():
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
        tipo_cuenta=int(input("Para crear la cuenta debe confirmar si inicia con un abono, de una o en cero: "))
        print("*")
        if(tipo_cuenta==1):
            cuenta_f=float(input("Ingrese el valor del abono en el que inicia la cuenta: "))
            print("*")
            cuenta=cuenta_f*(-1)
        elif(tipo_cuenta==2):
            cuenta=float(input("Ingrese el valor del la deuda en la que inicia la cuenta: "))
            print("*")
        elif(tipo_cuenta==3):
            cuenta=0.0
        else:
            print("Datos invalidos")
            print("*")
        cliente_t=Cliente(nombre,telefono,cuenta)
        lista_Cliente.append(cliente_t)
        s=input("Desea segir creando clientes si/no : ")
        if(s=="si"):
            crear_cliente()
        else:
            print("fin")





        

                    

  
