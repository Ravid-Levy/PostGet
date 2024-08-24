import socket

def send_post_request():
    host = "localhost"
    port = 5000

    # יצירת סוקט
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # נתונים לשליחה
    params = "param1453=value1&param500=value250"
    content_length = len(params)
    # request of post is just the request itself, and after it headers and after it the parameters
    # (what called body).

    # בניית בקשת POST ידנית
    request = f"POST /api HTTP/1.1\r\n" \
              f"Host: {host}\r\n" \
              f"Content-Type: application/x-www-form-urlencoded\r\n" \
              f"Content-Length: {content_length}\r\n" \
              f"Connection: close\r\n\r\n" \
              f"{params}"

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
    send_post_request()
