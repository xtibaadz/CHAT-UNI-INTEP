from typing import List, Optional

class Usuario:
    """Clase Base del diagrama UML general."""
    def __init__(self, id_usuario: str, nombre: str, email: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.chats: List[str] = [] 

    def ver_perfil(self) -> str:
        return f"[{self.__class__.__name__}] {self.nombre} (ID: {self.id_usuario}) - Email: {self.email}"


class Estudiante(Usuario):
    """Especialización de Usuario solicitada en la Tarea #2."""
    def __init__(self, id_usuario: str, nombre: str, email: str, carrera: str):
        super().__init__(id_usuario, nombre, email)
        self.carrera = carrera
        self.materias_inscritas: List[str] = [] 

    def inscribir_materia(self, nombre_materia: str) -> None:
        if nombre_materia not in self.materias_inscritas:
            self.materias_inscritas.append(nombre_materia)
            print(f"✓ Estudiante {self.nombre} inscribió la materia: {nombre_materia}")
        else:
            print(f"x El estudiante ya está inscrito en {nombre_materia}")

    def unirse_a_chat(self, nombre_chat: str) -> None:
        if nombre_chat not in self.chats:
            self.chats.append(nombre_chat)
            print(f"✓ Estudiante {self.nombre} se ha unido al chat: '{nombre_chat}'")
        else:
            print(f"x Ya formas parte del chat: '{nombre_chat}'")


class Docente(Usuario):
    """Especialización de Usuario solicitada en la Tarea #2."""
    def __init__(self, id_usuario: str, nombre: str, email: str):
        super().__init__(id_usuario, nombre, email)
        self.materias_asignadas: List[str] = []

    def administrar_materia(self, nombre_materia: str) -> None:
        """Permite al docente registrar o administrar una materia asignada."""
        if nombre_materia not in self.materias_asignadas:
            self.materias_asignadas.append(nombre_materia)
            print(f"✓ Materia '{nombre_materia}' añadida a la administración del docente {self.nombre}")

    def crear_chat_relacionado(self, nombre_materia: str) -> Optional[str]:
        """Crea un chat relacionado a la materia siempre y cuando la administre."""
        if nombre_materia in self.materias_asignadas:
            nombre_chat = f"Chat - {nombre_materia}"
            if nombre_chat not in self.chats:
                self.chats.append(nombre_chat)
                print(f"✓ Docente {self.nombre} creó el chat relacionado: '{nombre_chat}'")
                return nombre_chat
            else:
                print(f"x El chat para {nombre_materia} ya existe.")
                return nombre_chat
        else:
            print(f"x Error: El docente no puede crear un chat para '{nombre_materia}' porque no la tiene asignada.")
            return None