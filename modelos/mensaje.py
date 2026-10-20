from datetime import datetime


class Mensaje:
    def __init__(self, id, emisor, contenido, fecha_hora=None):
        self.id = id
        self.emisor = emisor
        self.contenido = contenido
        self.fecha_hora = fecha_hora or datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "emisor": self.emisor.nombre,
            "contenido": self.contenido,
            "fecha_hora": self.fecha_hora.isoformat(timespec="seconds")
        }    