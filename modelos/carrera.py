class Carrera:
    def __init__(self, id, nombre, administrativo=None):
        self.id = id
        self.nombre = nombre
        self.materias = []
        self.administrativo = administrativo

    def agregar_materia(self, materia):
        if materia not in self.materias:
            self.materias.append(materia)
            materia.carrera = self


#Hola