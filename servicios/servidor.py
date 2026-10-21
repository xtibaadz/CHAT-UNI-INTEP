
import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clientes = []
bloqueo = threading.Lock()


def enviar_a_todos(mensaje, remitente):
    datos = mensaje.encode("utf-8")

    with bloqueo:
        destinatarios = [
            cliente for cliente in clientes
            if cliente != remitente
        ]

    desconectados = []

    for cliente in destinatarios:
        try:
            cliente.sendall(datos)
        except (OSError, ConnectionError):
            desconectados.append(cliente)

    if desconectados:
        with bloqueo:
            for cliente in desconectados:
                if cliente in clientes:
                    clientes.remove(cliente)
                try:
                    cliente.close()
                except OSError:
                    pass


def manejar_cliente(cliente, direccion):
    print(f"[+] Cliente conectado: {direccion}")

    try:
        while True:
            datos = cliente.recv(4096)

            if not datos:
                break

            mensaje = datos.decode("utf-8").strip()

            if not mensaje:
                continue

            print(f"{direccion}: {mensaje}")

            enviar_a_todos(
                f"{direccion[0]}: {mensaje}",
                cliente
            )

    except (OSError, ConnectionError) as error:
        print(f"[!] Conexión interrumpida: {error}")

    finally:
        with bloqueo:
            if cliente in clientes:
                clientes.remove(cliente)

        cliente.close()
        print(f"[-] Cliente desconectado: {direccion}")


def iniciar_servidor():
    servidor = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    servidor.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:
        servidor.bind((HOST, PORT))
        servidor.listen()

        print("=" * 40)
        print(" CHAT UNI-INTEP")
        print(f" Servidor escuchando en el puerto {PORT}")
        print(" Esperando conexiones...")
        print("=" * 40)

        while True:
            cliente, direccion = servidor.accept()

            with bloqueo:
                clientes.append(cliente)

            hilo = threading.Thread(
                target=manejar_cliente,
                args=(cliente, direccion),
                daemon=True
            )

            hilo.start()

    except OSError as error:
        print(f"Error al iniciar el servidor: {error}")

    finally:
        servidor.close()


if __name__ == "__main__":
    iniciar_servidor()
