
class Recetas:
    def __init__(self, v1=0, v2="", v3=""):
        self.__Cantidad = v1
        self.__Unidades = v2
        self.__Ingrediente = v3

    def setCantidad(self, cant):
        self.__Cantidad = cant

    def getCantidad(self):
        return self.__Cantidad

    def setUnidad(self, unidad):
        self.__Unidades = unidad

    def getUnidad(self):
        return self.__Unidades

    def setCantidad(self, Ing):
        self.__Ingrediente = Ing

    def getIngrediente(self):
        return self.__Ingrediente




