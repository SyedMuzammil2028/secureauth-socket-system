import json
import socket

from backend.common.config import settings


def call_socket_action(payload: dict, client_ip: str = "127.0.0.1") -> dict:
    try:
        raw_request = json.dumps(payload).encode("utf-8")

        with socket.create_connection(
            (settings.SOCKET_HOST, settings.SOCKET_PORT),
            timeout=5,
        ) as sock:
            sock.sendall(raw_request)
            raw_response = sock.recv(65535)

        return json.loads(raw_response.decode("utf-8"))

    except ConnectionRefusedError:
        return {
            "status": "error",
            "message": "Socket server is not running. Start it with: python -m backend.socket_server.server",
        }

    except socket.timeout:
        return {
            "status": "error",
            "message": "Socket server request timed out.",
        }

    except Exception as exc:
        return {
            "status": "error",
            "message": f"Socket client error: {exc}",
        }