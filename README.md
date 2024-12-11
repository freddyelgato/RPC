
# RPC - Remote Procedure Call Service

This project is a simple RPC (Remote Procedure Call) service implemented using Python and Docker. The RPC service allows users to execute procedures remotely over a network, making it ideal for distributed systems where functionality is shared between different machines or processes.

## Features

- **Remote Procedure Calls**: Execute methods on the server from a client over HTTP.
- **Dockerized Deployment**: Easily deploy and run the application in a containerized environment.
- **Ease of Use**: Lightweight and simple to set up and run.
- **Scalability**: Deploy multiple instances for handling larger loads.

## Requirements

- **Docker**: [Install Docker](https://www.docker.com/get-started) if you don’t have it yet.
- **Python**: [Install Python](https://www.python.org/downloads/) if you plan to run the server locally.

## Installation Instructions

### Clone the Repository

1. Open a terminal and clone the repository:
   ```bash
   git clone https://github.com/freddyelgato/RPC.git
   cd RPC
   ```

### Running Locally

2. If you want to run the application locally, first install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the RPC server:
   ```bash
   python app.py
   ```

### Running with Docker

4. To build and run the application using Docker:
   ```bash
   docker build -t rpc_holamundo .
   docker run -d -p 8000:8000 --name rpc_server rpc_holamundo
   ```

5. Verify the service is running by accessing the endpoint in your browser or client:
   ```
   http://localhost:8000
   ```

## How it Works

- **Client-Server Architecture**: The client sends requests to the server, which executes the procedure and returns the result.
- **Endpoint Design**: All RPC methods are exposed through a single endpoint.
- **JSON Communication**: Data exchange between the client and server is performed using JSON, ensuring compatibility with various programming languages.

## Example Usage

1. Make a request to the service using `curl`:
   ```bash
   curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"method": "add", "params": [5, 3]}'
   ```

   Response:
   ```json
   {
       "result": 8
   }
   ```

2. Use any HTTP client (e.g., Postman) to test the service.

## Screenshot

### RPC Service Running:
![RPC Service Running](https://i.postimg.cc/fbbzVjvp/RPC.png)

## Connect to the Repository

- For further details or to contribute, visit the [RPC GitHub repository](https://github.com/freddyelgato/RPC/tree/main).

- You can also find the Docker image for this project here: [RPC Docker Hub Image](https://hub.docker.com/r/2424833f/rpc)
