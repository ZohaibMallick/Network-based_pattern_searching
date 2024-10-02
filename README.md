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
```
### Run the Client
```bash
python client.py
```

### Sample Input
```bash
Enter the filename: socketinpython.txt

Enter the word to search: physical world
```

### Sample Output:
```bash
Results for 'physical world':

Line 7: There are a lot of networks that we can observe in our physical world airline or powerline networks or cities interconnected with one another via highways are some good examples
```

### Stopping the Server:
- To stop the server, press Ctrl + C in the terminal running server.py.


### Notes
- Make sure you have the test files (e.g., socketinpython.txt) in the appropriate location for the server to read them.
- Adjust the filename and file path as needed when entering information in the client.


![RP712i8m44Jl-OeS5V47F4YX7WMX5Jo6c2us4bFDRaKH_zqaJKgHvhOpRtO7KY19H_tDCAQCHEIbqM29VnZtRyMZBLGK5qlspLWDxWdk3yCeUcmGMsaR0xDXwLGxXeNGLfCGOr0Pa7QSBa1xRG673QdVUfigR7ZPMGkAPfmQR9EFLV3e0Ocbuf4AXiyxa0IPEvolOLcQfbWenO_mcZEJS](https://github.com/user-attachments/assets/c8893fd6-aa62-4099-b126-be3913ccd51b)
