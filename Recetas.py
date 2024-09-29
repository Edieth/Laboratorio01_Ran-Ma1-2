from msilib.schema import Class


class Recetas:
    def __init__(self, v1=0, v2="", v3=""):
        self.__Cantidad = v1
        self.__Unidad = v2
        self.__Ingrediente = v3



    def getCantidad(self):
        return self.__Cantidad

    def getUnidad(self):
        return self.__Unidad

    def getIngrediente(self):
        return self.__Ingrediente


class Preparaciones(Recetas):
    __identi = 0
    __ModoPrepara = ''

    def __init__(self,):
