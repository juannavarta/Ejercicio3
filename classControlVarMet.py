import csv
import os
from classRegistro import Registro

class controlVM:
    __filas: 0
    __columna: 0
    __listaVM = []

    def __init__(self, filas=30, columna=24):
        self.__filas = filas
        self.__columna = columna

    def mostrarDatos(self):
        for i in range (len(self.__listaVM)):
            for j in range (len(self.__listaVM[i])):
                print (self.__listaVM[i][j].getPres())

    def cargarDatos (self):
        for i in range (30):
            lista=[]
            for j in range (24):
                lista.append(0)
            self.__listaVM.append(lista)
        bandera = True
        archivo = open('Variables_Meteorologicas.csv', 'r')
        reader = csv.reader(archivo, delimiter =',')
        for fila in reader:
            dia = int(fila[0])
            hora = int(fila[1])
            temp = int(fila[2])
            hum = int(fila[3])
            pres = int(fila[4])
            xRegistro = Registro(temp, hum, pres)
            self.__listaVM[dia-1][hora] = xRegistro    
        print('Carga Lista!')
        os.system('pause')

    def mostrarMayoryMenor (self):
        os.system('cls')
        maxTemp = 0
        maxHum = 0
        maxPres = 0
        minTemp = 1000
        minHum = 1000
        minPres = 1000
        xi = 0
        xj = 0
        print ('*** VALORES MINIMOS ***')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getTemp() < minTemp):
                    minTemp = self.__listaVM[i][j].getTemp()
                    xi = i+1
                    xj = j
        print (f'->La temperatura minima es {minTemp}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getHum() < minHum):
                    minHum = self.__listaVM[i][j].getHum()
                    xi = i+1
                    xj = j
        print (f'->La humedad minima es {minTemp}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getPres() < minPres):
                    minPres = self.__listaVM[i][j].getPres()
                    xi = i+1
                    xj = j
        print (f'->La presion minima es {minTemp}. Del día: {xi} a la hora: {xj}')
        print ('*** VALORES MAXIMOS ***')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getTemp() > maxTemp):
                    maxTemp = self.__listaVM[i][j].getTemp()
                    xi = i+1
                    xj = j
        print (f'->La temperatura máxima es {maxTemp}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getHum() > maxHum):
                    maxHum = self.__listaVM[i][j].getHum()
                    xi = i+1
                    xj = j
        print (f'->La humedad máxima es {maxHum}. Del día: {xi} a la hora: {xj}')
        for i in range (len (self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                if (self.__listaVM[i][j].getPres() > maxPres):
                    maxPres = self.__listaVM[i][j].getPres()
                    xi = i+1
                    xj = j
        print (f'->La presion máxima es {maxPres}. Del día: {xi} a la hora: {xj}')

    def calcularPromedio (self):
        aux = 0
        cont = 0
        for i in range (len(self.__listaVM)):
            for j in range (len (self.__listaVM[i])):
                aux = aux + int (self.__listaVM[i][j].getTemp())
                cont = cont + 1
        return float (aux / cont)
    
    def listarPorDia (self, dia):
        print ('|{:^10} {:^10} {:^10} {:^10}|'. format('Hora', 'Temperatura', 'Humedad', 'Presion'))
        for j in range (len (self.__listaVM[dia])):
            print ('|{:^10} {:^10} {:^10} {:^10} |'. format(j, self.__listaVM[dia][j].getTemp(), self.__listaVM[dia][j].getHum(), self.__listaVM[dia][j].getPres()))
        print ('\n')