from classMenu import Menu
from classControlVarMet import controlVM


if __name__ == '__main__':
    menu = Menu()
    vm = controlVM()
    lista = [1, 2, 3]
    print (len(lista))
    op = int (menu.mostrarMenu())
    while op != 0:
        menu.manejadorMenu(op, vm)
        op = int (menu.mostrarMenu())