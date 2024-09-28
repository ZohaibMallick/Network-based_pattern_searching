# -Network-based_pattern_searching

## Prerequisites
- Ensure you have Python installed on your system (version 3.x is recommended).
- Create three Python files (`search.py`, `server.py`, and `client.py`) in the same directory.

## Steps to Run the Program

### 1. Create the Program Files
- Copy the code provided for `search.py`, `server.py`, and `client.py` and paste each into their respective files in the same directory.

### 2. Run the Server
- Open a terminal (command prompt) and navigate to the directory containing your program files.
- Start the server by running the following command:
    ```bash
    python server.py
    ```
- The server will start listening for client connections on `127.0.0.1:9999`.
- The server will continuously listen for connections until you stop it.

### 3. Run the Client
- Open a new terminal window and navigate to the same directory as the program files.
- Run the client program using:
    ```bash
    python client.py
    ```
- The client will prompt you to enter:
    - **Filename**: Enter the name of the file (make sure the file exists in the same directory as the program or provide the full path to the file).
    - **Word to Search**: Enter the word or pattern you want to search for in the file.
- The client sends the filename and search word to the server.
- The server processes the request using `search.py` and sends back the result to the client.
- The client displays the result, which includes the line number and content for each match found in the file.

### 4. Testing with Multiple Clients
- You can open more terminal windows and run `client.py` multiple times to test the server's multithreading capability.

## Example Execution

### Run the Server
```bash
python server.py
![Screenshot 2024-09-28 150959](https://github.com/user-attachments/assets/32074a39-f19f-4a05-8751-8ed5c5650f8a)
![Screenshot 2024-09-28 151109](https://github.com/user-attachments/assets/5993ba42-fa05-4d0c-a5dd-81a90b4bcf5d)
![Screenshot 2024-09-28 150644](https://github.com/user-attachments/assets/47ce058c-1f8f-40d4-b5aa-19b0ed73369b)

