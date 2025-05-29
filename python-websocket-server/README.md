# Python WebSocket Server

This project implements a WebSocket server in Python that handles client connections and processes various commands. The server is designed to be lightweight and efficient, making it suitable for real-time applications.

## Project Structure

```
python-websocket-server
├── src
│   ├── server.py        # Entry point for the WebSocket server
│   └── handlers.py      # Handles client connections and commands
├── requirements.txt     # Lists project dependencies
├── Dockerfile           # Docker configuration for the server
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to have the following dependencies installed:

- Python 3.x
- WebSocket library (e.g., `websockets`)

You can install the required dependencies using the following command:

```
pip install -r requirements.txt
```

## Running the Server

### Using Docker

1. Build the Docker image:

   ```
   docker build -t python-websocket-server .
   ```

2. Run the Docker container:

   ```
   docker run -p 8000:8000 python-websocket-server
   ```

The server will be accessible at `ws://localhost:8000`.

### Running Locally

If you prefer to run the server locally without Docker, you can execute the following command:

```
python src/server.py
```

## Functionality

The WebSocket server supports various commands, including:

- Echoing messages back to the client
- Performing basic arithmetic operations
- Reading and creating files
- User login functionality

Refer to the `src/handlers.py` file for detailed command handling logic.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.