class Usuario:
    def __init__(self, id, nombre, email, contraseña):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.contrasena = contraseña

    def enviar_mensaje(self, chat, contenido):
        return chat.agregar_mensaje(self, contenido)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "tipo": self.__class__.__name__
        }