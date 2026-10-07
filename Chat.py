from mensaje import Mensaje


class Chat:
    def __init__(self):
        self.mensajes = []

    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)

    def obtener_mensajes(self):
        return self.mensajes
