from modelos.usuario import Usuario

class Docente(Usuario):
    def __init__(self, id, nombre, email, contrasena):
        super().__init__(id, nombre, email, contrasena)
        self.materias_asignadas = []

    def asignar_materia(self, materia):
        if materia not in self.materias_asignadas:
            self.materias_asignadas.append(materia)
        materia.docente = self

    def crear_chat(self, materia):
        from modelos.chat import Chat

        if materia.docente is not self:
            raise ValueError("El docente no está asignado a esta materia.")

        if materia.chat is None:
            materia.chat = Chat(materia.id, materia)

        materia.chat.agregar_participante(self)
        return materia.chat