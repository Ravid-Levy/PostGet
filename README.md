
# HTTP Server and Client Examples

This repository contains four Python scripts that demonstrate basic HTTP server and client interactions using both Flask and raw sockets. Below is an overview of each script and how they work.

## Files Overview

### 1. `flask_api.py`

This script creates a simple HTTP server using the Flask framework. The server listens on `http://localhost:5000` and can handle both `GET` and `POST` requests at the `/api` endpoint.

- **GET Requests**: The server extracts all query parameters from the URL and returns them in the response.
- **POST Requests**: The server extracts all form data sent in the request body and returns them in the response.

**Usage**:
```bash
python flask_api.py
```

After running the script, you can test it using a browser or a tool like `curl`.

### 2. `get.py`

This script demonstrates how to send a `GET` request to the `flask_api.py` server using raw sockets.

- The request is manually constructed, and the parameters are included in the URL.
- The script sends the request and prints the server’s response.

**Usage**:
```bash
python get.py
```

Make sure the `flask_api.py` server is running before executing this script.

### 3. `post.py`

This script demonstrates how to send a `POST` request to the `flask_api.py` server using raw sockets.

- The request is manually constructed, including both headers and a body containing form data.
- The script sends the request and prints the server’s response.

**Usage**:
```bash
python post.py
```

Make sure the `flask_api.py` server is running before executing this script.

### 4. `socket_api.py`

This script implements a simple HTTP server using only Python’s built-in `socket` library. The server can handle both `GET` and `POST` requests at the `/api` endpoint.

- **Routing**: A decorator (`@route`) is used to register handler functions for specific paths and methods.
- **Request Parsing**: The script manually parses the HTTP request, extracting the method, path, headers, and body.
- **Dynamic Responses**: Based on the request method (`GET` or `POST`), the server responds with the received parameters.

**Usage**:
```bash
python socket_api.py
```

After running the script, you can test it using `get.py` and `post.py` scripts or by sending requests manually.

## Key Concepts

- **GET vs. POST**: `GET` requests send data as part of the URL (query parameters), whereas `POST` requests send data in the request body.
- **Raw Sockets**: The `get.py` and `post.py` scripts illustrate how HTTP requests can be sent using raw sockets, giving you control over the entire HTTP request structure.
- **Flask vs. Raw Sockets**: `flask_api.py` is a high-level abstraction using the Flask framework, whereas `socket_api.py` demonstrates a low-level approach to building an HTTP server from scratch.

## Running the Examples

1. **Start the Flask Server**:
   ```bash
   python flask_api.py
   ```

2. **Send a GET Request**:
   ```bash
   python get.py
   ```

3. **Send a POST Request**:
   ```bash
   python post.py
   ```

4. **Start the Raw Socket Server**:
   ```bash
   python socket_api.py
   ```

5. **Test the Raw Socket Server**:
   Use the `get.py` and `post.py` scripts to send requests to `socket_api.py` or use a tool like `curl` to send requests manually.

## Conclusion

These scripts are educational examples showing how HTTP requests and responses work at both high and low levels of abstraction. They are useful for understanding the basics of HTTP communication, the difference between `GET` and `POST` methods, and how to build simple HTTP servers and clients in Python.
