from modelos.usuario import Usuario


class Administrativo(Usuario):
    def __init__(
        self, id, nombre, email, contrasena, carrera=None
    ):
        super().__init__(id, nombre, email, contrasena)
        self.carrera = carrera

    def asignar_docente(self, docente, materia):
        if materia.carrera is not self.carrera:
            raise ValueError(
                "La materia no pertenece a esta carrera."
            )

        docente.asignar_materia(materia)

#Hola