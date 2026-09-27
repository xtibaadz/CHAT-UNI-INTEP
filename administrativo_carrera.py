"""
Clases Administrativo y Carrera para el sistema de chat universitario.

Se asume que ya existen (o existirán) las clases Docente, Estudiante,
Materia y Coordinador del diagrama UML general del proyecto. Aquí se
usa una versión mínima de Docente y Materia solo para que el ejemplo
sea ejecutable de forma independiente; si ya tienes esas clases
definidas en otro módulo, basta con importarlas en vez de usar estas.
"""

from typing import List, Optional


# --- Clases de apoyo mínimas (reemplázalas por las tuyas si ya existen) ---

class Docente:
    def __init__(self, nombre: str, id_docente: str):
        self.nombre = nombre
        self.id_docente = id_docente
        self.materias_asignadas: List["Materia"] = []

    def __str__(self):
        return f"Docente({self.nombre})"


class Materia:
    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.docente_asignado: Optional[Docente] = None

    def __str__(self):
        return f"Materia({self.nombre} - {self.codigo})"


# --- Clases solicitadas ---

class Administrativo:
    """
    Representa a un miembro del personal administrativo.
    Su responsabilidad principal es asignar docentes a materias.
    """

    def __init__(self, nombre: str, id_administrativo: str, cargo: str):
        self.nombre = nombre
        self.id_administrativo = id_administrativo
        self.cargo = cargo
        self.asignaciones_realizadas: List[dict] = []  # historial de asignaciones

    def asignar_docente_a_materia(self, docente: Docente, materia: Materia) -> bool:
        """
        Asigna un docente a una materia. Si la materia ya tenía un
        docente asignado, se reemplaza y se registra el cambio.
        """
        if materia.docente_asignado is not None:
            print(
                f"Aviso: {materia} ya tenía asignado a {materia.docente_asignado}. "
                f"Se reemplaza por {docente}."
            )

        materia.docente_asignado = docente
        if materia not in docente.materias_asignadas:
            docente.materias_asignadas.append(materia)

        self.asignaciones_realizadas.append(
            {"docente": docente.nombre, "materia": materia.nombre}
        )
        print(f"{self.nombre} asignó a {docente} la materia {materia}.")
        return True

    def __str__(self):
        return f"Administrativo({self.nombre}, {self.cargo})"


class Carrera:
    """
    Representa un programa académico (carrera). Gestiona sus materias
    y su relación con el personal administrativo asociado.
    """

    def __init__(self, nombre: str, codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.materias: List[Materia] = []
        self.personal_administrativo: List[Administrativo] = []

    # --- Gestión de materias ---
    def agregar_materia(self, materia: Materia) -> None:
        if materia not in self.materias:
            self.materias.append(materia)
            print(f"Materia {materia} agregada a la carrera {self.nombre}.")

    def eliminar_materia(self, materia: Materia) -> bool:
        if materia in self.materias:
            self.materias.remove(materia)
            print(f"Materia {materia} eliminada de la carrera {self.nombre}.")
            return True
        print(f"La materia {materia} no pertenece a la carrera {self.nombre}.")
        return False

    def listar_materias(self) -> List[str]:
        return [str(m) for m in self.materias]

    # --- Gestión del personal administrativo ---
    def vincular_administrativo(self, administrativo: Administrativo) -> None:
        if administrativo not in self.personal_administrativo:
            self.personal_administrativo.append(administrativo)
            print(f"{administrativo} vinculado a la carrera {self.nombre}.")

    def desvincular_administrativo(self, administrativo: Administrativo) -> bool:
        if administrativo in self.personal_administrativo:
            self.personal_administrativo.remove(administrativo)
            print(f"{administrativo} desvinculado de la carrera {self.nombre}.")
            return True
        return False

    def solicitar_asignacion_docente(
        self, administrativo: Administrativo, docente: Docente, materia: Materia
    ) -> bool:
        """
        La carrera solicita a uno de sus administrativos que asigne
        un docente a una materia perteneciente a la carrera.
        """
        if administrativo not in self.personal_administrativo:
            print(
                f"{administrativo} no pertenece al personal administrativo "
                f"de la carrera {self.nombre}."
            )
            return False
        if materia not in self.materias:
            print(f"La materia {materia} no pertenece a la carrera {self.nombre}.")
            return False

        return administrativo.asignar_docente_a_materia(docente, materia)

    def __str__(self):
        return f"Carrera({self.nombre} - {self.codigo})"


# --- Ejemplo de uso ---
if __name__ == "__main__":
    ingenieria = Carrera("Ingeniería de Sistemas", "IS-01")

    prog1 = Materia("Programación I", "PROG-101")
    estructuras = Materia("Estructuras de Datos", "EST-201")
    ingenieria.agregar_materia(prog1)
    ingenieria.agregar_materia(estructuras)

    coordinadora = Administrativo("María Gómez", "ADM-01", "Coordinadora Académica")
    ingenieria.vincular_administrativo(coordinadora)

    docente1 = Docente("Carlos Ruiz", "DOC-01")

    ingenieria.solicitar_asignacion_docente(coordinadora, docente1, prog1)

    print("\nMaterias de la carrera:", ingenieria.listar_materias())
