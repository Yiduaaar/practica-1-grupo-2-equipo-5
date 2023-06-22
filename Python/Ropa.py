#Autor Yiduar
class Ropa:
    def __init__(self, *args):
        if len(args) == 2:
            self.talla = args[0].talla
            self.color = args[0].color
            self.precio = args[0].precio
            self.nombre = args[0].nombre
            self.cantidad = args[1]
            self.supermercado = args[0].supermercado
        else:
            self.talla = args[0]
            self.color = args[1]
            self.precio = args[2]
            self.nombre = args[3]
            self.cantidad = args[4]
            self.supermercado = args[5]
            
