import socket

def send_get_request():
    host = "localhost"
    port = 5000

    # יצירת סוקט
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    # request of get is just the request itself, and after it headers.
    # בניית בקשת GET ידנית
    request = "GET /api?param1=value1&param2=value2 HTTP/1.1\r\n" \
              "Host: localhost\r\n" \
              "Connection: close\r\n\r\n"

    # שליחת הבקשה
    client_socket.sendall(request.encode())

    # קבלת תשובת השרת
    response = b""
    while True:
        part = client_socket.recv(1024)
        if not part:
            break
        response += part

    # הצגת תשובת השרת
    print(response.decode("utf-8"))

    # סגירת החיבור
    client_socket.close()

if __name__ == "__main__":
    send_get_request()
