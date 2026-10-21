
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print("Conectado al servidor.")
print("Escribe un mensaje y presiona Enter.")
print("Escribe 'salir' para desconectarte.")

def recibir_mensajes():
    while True:
        try:
            datos = cliente.recv(1024)

            if not datos:
                print("\nEl servidor cerró la conexión.")
                break

            print("\nMensaje recibido:", datos.decode("utf-8"))

        except OSError:
            break

hilo = threading.Thread(target=recibir_mensajes, daemon=True)
hilo.start()

try:
    while True:
        mensaje = input("Tú: ")

        if mensaje.lower() == "salir":
            break

        cliente.sendall(mensaje.encode("utf-8"))

except (OSError, EOFError):
    print("Conexión finalizada.")

finally:
    cliente.close()
    print("Cliente desconectado.")
