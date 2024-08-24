import socket

# Dictionary to store routes and their associated HTTP methods
routes = {}


# Decorator to register routes and their allowed HTTP methods
def route(path, methods=['GET']):
    def wrapper(func):
        # Register the function for each method for the given path
        for method in methods:
            routes[(path, method)] = func
        return func

    return wrapper


# Function to handle both GET and POST requests to the '/api' path
@route('/api', methods=['GET', 'POST'])
def handle_request(method, params):
    # Build the response body with the received parameters
    response_body = f"{method} request received with the following parameters:\n"
    for key, value in params.items():
        response_body += f"{key} = {value}\n"
    return response_body


# Function to parse the HTTP request into method, path, headers, and body
def parse_http_request(request):
    headers, body = request.split('\r\n\r\n', 1)  # Split headers and body
    request_line, headers = headers.split('\r\n', 1)  # Split the request line from the rest of the headers
    method, path, _ = request_line.split(' ')  # Extract the method, path, and HTTP version (we discard the version)
    headers = dict(line.split(': ', 1) for line in headers.split('\r\n'))  # Convert headers to a dictionary
    return method, path, headers, body


# Function to extract parameters based on the request method (GET or POST)
def get_params(method, path, body):
    if method == 'GET':
        # Extract parameters from the query string in the URL
        _, query = path.split('?', 1) if '?' in path else (path, '')
        return dict(pair.split('=') for pair in query.split('&')) if query else {}
    elif method == 'POST':
        # Extract parameters from the body of the POST request
        return dict(pair.split('=') for pair in body.split('&'))
    return {}


# Function to start the server and handle incoming connections
def start_server(host='0.0.0.0', port=5000):
    # Create a TCP socket and bind it to the specified host and port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for incoming connections with a backlog of 5
    print(f"Server running on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()  # Accept a new client connection
        request = client_socket.recv(1024).decode()  # Receive the HTTP request from the client

        method, path, headers, body = parse_http_request(request)  # Parse the request into components
        print(f"Received {method} request from {client_address}")

        # Determine the appropriate handler for the request based on the path and method
        handler = routes.get((path.split('?', 1)[0], method))
        if handler:
            params = get_params(method, path, body)  # Extract parameters from the request
            response_body = handler(method, params)  # Call the handler function with the method and parameters
            status_line = "HTTP/1.1 200 OK\r\n"  # Set the response status to 200 OK
        else:
            # If no handler is found, return a 404 Not Found response
            response_body = "404 Not Found: The requested URL was not found on this server or the method is not supported.\n"
            status_line = "HTTP/1.1 404 Not Found\r\n"

        # Build the full HTTP response
        response = (
                status_line +
                "Content-Type: text/plain\r\n" +
                f"Content-Length: {len(response_body)}\r\n" +
                "Connection: close\r\n" +
                "\r\n" +
                response_body
        )

        # Send the response back to the client and close the connection
        client_socket.sendall(response.encode())
        client_socket.close()


# Start the server when the script is executed
if __name__ == "__main__":
    start_server()
