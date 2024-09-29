from Recetas import Recetas

class Preparaciones(Recetas):
    __identi = 0
    __ModoPrepara = ''

    def __init__(self,id, modo):
        self.__identi = id
        self.__ModoPrepara = modo

    def getId(self):
        return self.__identi
    def getModoPre(self):
        return  self.__ModoPrepara

