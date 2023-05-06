import os
class Menu:
    def mostrarMenu(self):
        os.system('cls')
        op = int (input('''
************* Menu Principal *************
1 -- REALIZAR CARGA
2 -- Mostrar MAYOR y MENOR por variable
3 -- Mostar TEMPERATURA PROMEDIO del mes
4 -- Ver VALORES POR DIA
0 -- Salir
Su opcion: '''))
        return op
    
    def manejadorMenu(self, op, VM):
        if op == 1:
            self.opc1(VM)
        
        elif op == 2:
            self.opc2(VM)

        elif op == 3:
            self.opc3(VM)

        elif op == 4:
            self.opc4(VM)
        
        else:
            print ('saliendo del menu')
            os.system('pause')

    def opc1(self, VM):
        VM.cargarDatos()

    def opc2 (self, VM):
        VM.mostrarMayoryMenor()
        os.system('pause')

    def opc3 (self, VM):
        r = VM.calcularPromedio()
        print ('La Temperatura promedio del mes es: {} grados'.format(r))
        os.system('pause')

    def opc4 (self, VM):
        os.system('cls')
        xop = int (input ('Ingrese día del mes que desea listar: '))
        VM.listarPorDia(xop-1)
        os.system('pause')