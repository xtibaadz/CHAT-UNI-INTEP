from datetime import datetime


class Mensaje:
    def __init__(self, identificador, emisor, contenido):
        self.identificador = identificador
        self.emisor = emisor
        self.contenido = contenido
        self.fecha_hora = datetime.now()

    def __str__(self):
        return f"[{self.fecha_hora}] {self.emisor}: {self.contenido}"
