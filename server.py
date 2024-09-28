import socket
import threading
import json
from search import Search

def handle_client(client_socket):
    try:
        # Receive data from the client
        request_data = client_socket.recv(1024).decode()
        request = json.loads(request_data)
        
        filename = request.get('filename')
        word = request.get('word')
        
        # Process the search
        try:
            search_obj = Search(filename)
            search_obj.clean()
            result = search_obj.getLines(word)
            response = json.dumps(result)
        except Exception as e:
            response = json.dumps({"error": str(e)})
        
        # Send the response to the client
        client_socket.send(response.encode())
    finally:
        client_socket.close()

def start_server(host='127.0.0.1', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
