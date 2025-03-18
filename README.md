# Task List Application

This project is a simple web application for managing a list of tasks. It consists of a backend built with Flask (Python), a PostgreSQL database, and a frontend served by Flask. The application is containerized using Docker and orchestrated with Docker Compose.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML (served by Flask)
- **Containerization**: Docker
- **Orchestration**: Docker Compose

## Setup

### Requirements

- Docker Desktop installed and running on your machine.
- Basic knowledge of Docker and Docker Compose.

### Project Structure
myapp/

├── Dockerfile
├── app.py
├── requirements.txt
├── test_api.py
├── templates/
│   └── index.html
└── docker-compose.yml

## Building and Running the Application

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/myapp.git
   cd myapp

2. **Build the Docker images**:
    ```bash
   docker-compose build
3. **Run the application:**:
    ```bash
   docker-compose up

This will start the following services:

- db: PostgreSQL database
- backend: Flask application serving the API and frontend
- tests: Runs the API tests

4. **Access the application:**
- Open a web browser and navigate to http://localhost:5000 to see the task list interface.

5. **Running tests:**
- Tests are automatically run when the application is started with docker-compose up. You can view the test results in the logs of the tests service.

## Stopping the Application

**To stop the application and remove the containers, run:**
```bash
docker-compose down
