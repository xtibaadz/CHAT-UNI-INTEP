from modelos.mensaje import Mensaje


class Chat:
    def __init__(self, id, materia):
        self.id = id
        self.materia = materia
        self.participantes = []
        self.mensajes = []

    def agregar_participante(self, usuario):
        if usuario not in self.participantes:
            self.participantes.append(usuario)

    def agregar_mensaje(self, emisor, contenido):
        if emisor not in self.participantes:
            raise ValueError(
                "El usuario no pertenece a este chat."
            )

        if not contenido or not contenido.strip():
            raise ValueError(
                "El mensaje no puede estar vacío."
            )

        mensaje = Mensaje(
            len(self.mensajes) + 1,
            emisor,
            contenido.strip()
        )

        self.mensajes.append(mensaje)
        return mensaje