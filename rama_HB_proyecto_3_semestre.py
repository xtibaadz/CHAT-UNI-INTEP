from datetime import datetime


class Mensaje:
    """Clase que representa un mensaje individual en el chat."""

    def __init__(self, id_mensaje, emisor, contenido):
        self.id_mensaje = id_mensaje
        self.emisor = emisor
        self.contenido = contenido
        # Registra automáticamente la fecha y hora actual al crearse
        self.fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"[{self.fecha_hora}] {self.emisor} (ID: {self.id_mensaje}): {self.contenido}"


class Chat:
    """Clase encargada de gestionar y almacenar el historial de mensajes."""

    def __init__(self, nombre_chat):
        self.nombre_chat = nombre_chat
        self.mensajes = []
        self._contador_id = 1  # Autoincremento para generar IDs únicos

    def enviar_mensaje(self, emisor, contenido):
        """Crea un nuevo mensaje y lo almacena en el chat."""
        nuevo_mensaje = Mensaje(self._contador_id, emisor, contenido)
        self.mensajes.append(nuevo_mensaje)
        self._contador_id += 1
        return nuevo_mensaje

    def ver_mensajes(self):
        """Muestra todos los mensajes guardados."""
        print(f"\n--- Historial del Chat: {self.nombre_chat} ---")
        if not self.mensajes:
            print("No hay mensajes en este chat.")
            return

        for msg in self.mensajes:
            print(msg)

    def buscar_por_emisor(self, emisor):
        """Devuelve una lista con los mensajes de un usuario en específico."""
        return [msg for msg in self.mensajes if msg.emisor == emisor]



# Ejemplo de uso


if __name__ == "__main__":
    # 1. Crear una sala de chat
    mi_chat = Chat("Grupo de Proyecto Python")

    # 2. Enviar mensajes
    mi_chat.enviar_mensaje("Hector", "¡Hola a todos! ¿Cómo van con la tarea?")
    mi_chat.enviar_mensaje("Nikoll", "¡Hola Hector! Ya casi termino la parte de la clase Mensaje.")
    mi_chat.enviar_mensaje("Hector", "¡Excelente, avísame si necesitan ayuda!")
    mi_chat.enviar_mensaje("Ivan", "¡Gracias, Hector! yo necesito ayuda con la función de búsqueda por emisor.")

    # 3. Consultar todos los mensajes
    mi_chat.ver_mensajes()

    # 4. Consultar mensajes de un emisor específico
    print("\n--- Mensajes enviados solo por Hector and Nikoll ---")
    mensajes_hector = mi_chat.buscar_por_emisor("Hector")
    mensajes_nikoll = mi_chat.buscar_por_emisor("Nikoll")
    mensajes_ivan = mi_chat.buscar_por_emisor("Ivan")
    for msg in mensajes_hector:
        print(msg)
    for msg in mensajes_nikoll:
        print(msg)
    for msg in mensajes_ivan:
        print(msg)
    