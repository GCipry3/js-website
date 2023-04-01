import socket


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
    if not headers:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\nError occured."
        client.send(response.encode())
        return
    
    filename = headers[0].split()[1]

    if filename == "/":
        filename = "/index.html"

    filepath = "../content" + filename
    try:
        with open(filepath, "rb") as f:
            content = f.read()
        response = f"HTTP/1.1 200 OK\r\nContent-Type: {get_content_type(filename)}\r\n\r\n"
        client.send(response.encode())
        client.send(content)
    except FileNotFoundError:
        response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\nFile not found."
        client.send(response.encode())


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8080))
    server_socket.listen(5)
    print("Server is running on http://localhost:8080")

    while True:
        print('\n' + '#' * 70)
        print('Serverul asculta potentiali clienti.')
        client_socket, addr = server_socket.accept()
        print('S-a conectat un client.')

        request = client_socket.recv(1024).decode('utf-8')
        print(
            f'S-a citit mesajul: \n---------------------------\n{request}\n--------------------------')
        handle_request(request, client_socket)
        client_socket.close()

        print('S-a terminat comunicarea cu clientul.')


if __name__ == "__main__":
    main()
