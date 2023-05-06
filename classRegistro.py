class Registro:
    __temp = 0
    __hum = 0
    __pres = 0

    def __init__(self, temp=0, hum=0, pres=0):
        self.__temp = temp
        self.__hum = hum
        self.__pres = pres

    def getPres(self):
        return self.__pres
    
    def getTemp (self):
        return self.__temp
    
    def getHum (self):
        return self.__hum