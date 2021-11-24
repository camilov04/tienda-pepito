
#creamos la clase cliente


class Cliente:


    #comenzamos con el metodo constructor


    def __init__(self,nombre,numero_telefono, cuenta):

        self.nombre=nombre
        self.numero_telefono=numero_telefono
        self.cuenta=cuenta
        

    def modificar(self,nombre,numero_telefono,cuenta):
        self.nombre=nombre
        self.numero_telefono=numero_telefono
        self.cuenta=cuenta

    #con la funcion de pasar a cadena lo que haremos es mostrar los atributos de los anteriormente creados
    #en una cadena de caracteres

    def PasarAcadena(self):
        print("")
        return print("--Nombre--",self.nombre,"--Número de teléfono--",self.numero_telefono,"--valor de la deuda--",self.cuenta)
