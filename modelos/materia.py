class Materia:
    def __init__(
        self, id, nombre, carrera=None, docente=None
    ):
        self.id = id
        self.nombre = nombre
        self.carrera = carrera
        self.docente = None
        self.chat = None

        if carrera is not None:
            carrera.agregar_materia(self)

        if docente is not None:
            docente.asignar_materia(self)