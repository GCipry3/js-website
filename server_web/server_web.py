import socket
import time
import gzip
import threading


def compress_content(content):
    return gzip.compress(content, compresslevel=9)

def log_request(request):
    with open('log_requests.txt', 'a') as f:
        f.write(f"{'#' * 30}{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}{'#' * 30}")
        f.write(f"\n{request}\n")

def get_content_type(file):
    if file.endswith(".html"):
        return "text/html"
    if file.endswith(".css"):
        return "text/css"
    if file.endswith(".js"):
        return "application/javascript"
    if file.endswith(".jpg"):
        return "image/jpeg"
    if file.endswith(".mp4"):
        return "video/mp4"
    if file.endswith(".xml"):
        return "application/xml"
    return "text/plain"


def handle_request(request, client):
    headers = request.split('\r\n')

    first_header = headers[0].split()
    if len(first_header) < 2:
        response = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\nInvalid request."
        client.send(response.encode())
        client.close()
        return

    filename = first_header[1]

    if filename == "/":
        filename = "/index.html"

    filepath = "../content" + filename
    try:
        with open(filepath, "rb") as f:
            content = f.read()
        
        # Send the videos in chunks to avoid memory issues , and send the rest of the files compressed
        if filename.endswith(".mp4"):
            response = f"HTTP/1.1 200 OK\r\nContent-Type: {get_content_type(filename)}\r\n\r\n"
            client.send(response.encode())
            with open(filepath, "rb") as f:
                chunk = f.read(1024)
                while chunk:
                    client.send(chunk)
                    chunk = f.read(1024)
        else:
            # Compress the content
            compressed_content = compress_content(content)
            response = f"HTTP/1.1 200 OK\r\nContent-Type: {get_content_type(filename)}\r\nContent-Encoding: gzip\r\n\r\n"
            log_request(f"{headers[0]}\n{response}")

            client.send(response.encode())
            client.send(compressed_content)
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\nFile not found."
        client.send(response.encode())

    client.close()


def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8080))
    server_socket.listen(5)
    print("Server is running on http://localhost:8080")

    # Accept connections forever
    while True:
        try:
            # Accept a connection
            print(f"\n{'#' * 70}")
            print('The server is listening for the clients.')
            client_socket, addr = server_socket.accept()
            print(f'Client {addr} connected.')

            # Receive the request
            request = client_socket.recv(1024).decode('utf-8')
            print(f"\nThe message is:\n{'-'*35}\n{request}\n{'-'*35}\n")
            client_thread = threading.Thread(target=handle_request, args=(request, client_socket))
            client_thread.start()

            print('S-a terminat comunicarea cu clientul.')
        except Exception as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    main()
