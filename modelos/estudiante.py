from modelos.usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, id, nombre, email, contraseña, carrera=None):
        super().__init__(id, nombre, email, contraseña)
        self.carrera = carrera
        self.materias_inscritas = []

    def inscribir_materia(self, materia):
        if materia not in self.materias_inscritas:
            self.materias_inscritas.append(materia)

    def unirse_chat(self, materia):
        if materia.chat is None:
            raise ValueError("La materia todavía no tiene un chat.")
        materia.chat.agregar_participante(self)
        return materia.chat