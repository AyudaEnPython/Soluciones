"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
def añadir(listin, nombre, telefonos):
	if nombre in listin:
		if not telefono in listin[nombre]:
			listin[nombre].append(telefono)
	else:
		listin[nombre] = [telefonos]

def consultar(listin, nombre):
	if nombre in listin:
		return listin[nombre]
	else:
		return '+'

def eliminar(listin, nombre):
    if nombre in listin:
        del listin[nombre]

def menu():
    opcion = 0
    while opcion < 1 or opcion > 4:
        print("MENU PRINCIPAL\n")
        print("1) Añadir telefonos")
        print('2) Consular listin')
        print('3) Eliminar persona del listin')
        print('4) salir')
        opcion =int(input("Seleccione una opcion: "))
    return opcion

def main():
	
	listin ={}

	opcion = 0

	while opcion != 4:
		opcion = menu()
		if opcion == 1:
			nombre = input("Ingrese un nombre: ")
			telefono = input('Ingrese un telefono: ')
			añadir(listin, nombre, telefono)
			mas = input(f'¿Desea añadir otro telefono a {nombre} (s/n)?: ')
			while mas == 's':
				telefono = input('inrese un telefono ')
				añadir(listin, nombre, telefono)
				mas = input(f'¿Desea añadir otro telefono a {nombre} (s/n)?: ')
		elif opcion == 2:
			nombre = input('Ingrese un nombre: ')
			telefonos = input('Ingrese un telefono: ')
			for telefono in telefonos:
				print('telefono')
		elif opcion == 3:
			nombre = input('Ingrese un nombre')
			eliminar(listin, nombre)
	print('Saliste...')


if __name__ == '__main__':
	main()