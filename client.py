import socket
import json

def start_client(host='127.0.0.1', port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    
    # Get user input
    filename = input("Enter the filename: ")
    word = input("Enter the word to search: ")
    
    # Create the request dictionary
    request = {
        "filename": filename,
        "word": word
    }
    
    # Send the request to the server
    client.send(json.dumps(request).encode())
    
    # Receive the response from the server
    response_data = client.recv(1024).decode()
    response = json.loads(response_data)
    
    if 'error' in response:
        print(f"Error: {response['error']}")
    else:
        print(f"Results for '{response[0]}':")
        for item in response[1:]:
            print(f"Line {item[0]}: {item[1]}")

    client.close()

if __name__ == "__main__":
    start_client()
