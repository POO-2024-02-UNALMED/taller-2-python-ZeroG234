coloresValidos = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']

class Asiento:
    def __init__(self, color: str = '', precio: int = 0, registro: int = 0):
        self.color    = color
        self.precio   = precio
        self.registro = registro

    def cambiarColor(self, nuevoColor: str):
        if nuevoColor in coloresValidos:
            self.color = nuevoColor

tiposValidos = ['gasolina', 'electrico']

class Motor:
    def __init__(self, numeroCilindros: int, tipo: str, registro: int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro: int):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo: str):
        if nuevoTipo in tiposValidos:
            self.tipo = nuevoTipo

class Auto:
    cantidadCreados = ''

    def __init__(self, modelo: str = '', precio: int = 0, asientos: list[Asiento] = [], marca: str = '',
                 motor: Motor = None, registro: int = 0):
        self.modelo          = modelo
        self.precio          = precio
        self.asientos        = asientos
        self.marca           = marca
        self.motor           = motor
        self.registro        = registro

    def cantidadAsientos(self) -> int:
        count = 0

        for asiento in self.asientos:
            if asiento != None:
                count += 1

        return count

    def verificarIntegridad(self) -> str:
        esOriginal = 'Auto original'

        if self.motor.registro != self.registro:
            esOriginal = 'Las piezas no son originales'

        for asiento in self.asientos:
            if asiento.registro != self.registro:
                esOriginal = 'Las piezas no son originales'

        return esOriginal