class Persona:
    def __init__(self, edad, nombre, telefono):
        self.__edad = edad
        self.__nombre = nombre
        self.__telefono = telefono

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono


class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self.__credito = credito

    def get_credito(self):
        return self.__credito

    def set_credito(self, credito):
        self.__credito = credito


class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario


def main():
    opcion = input("¿Qué objeto quieres crear? (C: Cliente, T: Trabajador)")

    if opcion.upper() == "C":
        edad = int(input("Introduce la edad del cliente: "))
        nombre = input("Introduce el nombre del cliente: ")
        telefono = input("Introduce el teléfono del cliente: ")
        credito = float(input("Introduce el crédito del cliente: "))
        cliente = Cliente(edad, nombre, telefono, credito)
        print("Edad del cliente:", cliente.get_edad())
        print("Nombre del cliente:", cliente.get_nombre())
        print("Teléfono del cliente:", cliente.get_telefono())
        print("Crédito del cliente:", cliente.get_credito())

    elif opcion.upper() == "T":
        edad = int(input("Introduce la edad del trabajador: "))
        nombre = input("Introduce el nombre del trabajador: ")
        telefono = input("Introduce el teléfono del trabajador: ")
        salario = float(input("Introduce el salario del trabajador: "))
        trabajador = Trabajador(edad, nombre, telefono, salario)
        print("Edad del trabajador:", trabajador.get_edad())
        print("Nombre del trabajador:", trabajador.get_nombre())
        print("Teléfono del trabajador:", trabajador.get_telefono())
        print("Salario del trabajador:", trabajador.get_salario())

    else:
        print("Opción inválida. Introduce 'C' para crear un cliente o 'T' para crear un trabajador.")


if __name__ == '__main__':
    main()