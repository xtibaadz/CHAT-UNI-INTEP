from datetime import datetime


class Mensaje:

    def __init__(self, identificador: int, emisor: str, contenido: str, fecha_hora=None):
        self.identificador = identificador
        self.emisor = emisor
        self.contenido = contenido
        # Si no se proporciona fecha y hora, se asigna el momento actual
        self.fecha_hora = (fecha_hora if fecha_hora else datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __repr__(self):
        return f"[{self.fecha_hora}] ID {self.identificador} | {self.emisor}: {self.contenido}"


class Chat:

    def __init__(self, nombre_chat: str):
        self.nombre_chat = nombre_chat
        self.mensajes = []  # Lista para almacenar los objetos Mensaje
        self._contador_id = 1

    def enviar_mensaje(self, emisor: str, contenido: str):
        """Crea y almacena un nuevo mensaje en el chat."""
        nuevo_mensaje = Mensaje(self._contador_id, emisor, contenido)
        self.mensajes.append(nuevo_mensaje)
        self._contador_id += 1

    def recorrer_mensajes_inverso_while(self):
        """Recorre e imprime la lista de mensajes de forma inversa usando un bucle while."""
        print(f"--- Historial Inverso del Chat '{self.nombre_chat}' ---")

        if not self.mensajes:
            print("El chat no tiene mensajes.")
            return

        # Iniciamos el índice en la última posición válida
        i = len(self.mensajes) - 1

        # Mientas el índice sea mayor o igual a 0, recorremos hacia atrás
        while i >= 0:
            print(self.mensajes[i])
            i -= 1


# --- PRUEBA Y EJECUCIÓN ---
if __name__ == "__main__":
    # 1. Creamos una instancia de Chat
    mi_chat = Chat(nombre_chat="Proyecto Python")

    # 2. Registramos varios mensajes
    mi_chat.enviar_mensaje("Alice", "Hola a todos, ¿cómo van?")
    mi_chat.enviar_mensaje("ivan", "¡Hola! Todo bien por acá.")
    mi_chat.enviar_mensaje("Charlie", "Avanzando con el código.")
    mi_chat.enviar_mensaje("Alice", "Excelente, no olviden hacer push.")

    # 3. Recorremos la lista de mensajes de forma inversa usando while
    mi_chat.recorrer_mensajes_inverso_while()
    
    