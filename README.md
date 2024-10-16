<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Task Management API</h1>
    <p>A simple task management REST API built with Django and Django REST Framework. This API allows users to create, read, update, and delete tasks, with support for user registration, Searching and authentication using JWT.</p
                                                                                                                                                                                                                           
## Features

- User registration and authentication using JWT.
- CRUD operations for tasks.
- Task search functionality by title, status, and priority.
- Task assignment to different users (many-to-one relationship).

## Technologies

- **Django**: A high-level Python web framework.
- **Django REST Framework**: A powerful toolkit for building web APIs.
- **PostgreSQL**: A powerful, open-source relational database.
- **JWT (JSON Web Tokens)**: A compact, URL-safe means of representing claims to be transferred between two parties.
- **POSTMAN

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- PostgreSQL
- Django 4.x or later
- Django REST Framework
- Django SimpleJWT

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shanu-shahbin/Task-Management-using-API.git
2. Navigate to the project directory:
   ```bash
   cd Task-Management-using-API
3. Create a virtual environment and activate it:
   ```bash
    python3 -m venv venv
    venv\Scripts\activate  
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
5. Set up the PostgreSQL database and add your credentials to the settings.py file:
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
   }

6. Apply migrations:
   ```bash
     python manage.py makemigrations
     python manage.py migrate
     python manage.py runserver

## Endpoints

- Register: /auth/register/ - Registers a new user.
- Login: /auth/login/ - Obtain JWT for authentication.
- Token Refresh: /auth/token/refresh/ - Refresh the JWT
- Tasks: /tasks/ - List or create tasks (requires authentication).
- Task Detail: /tasks/<id>/ - Retrieve, update, or delete a task (requires authentication).

## usage

- You can use tools like Postman or curl to test the API endpoints.
- Ensure you include the JWT token in the Authorization header as:
  ```bash
  Authorization: Bearer <your_token_here>

## License

-This project is licensed under the MIT License.

## output screenshots
- Listed all the tasks using GET

  
![http___127 0 0 1_8000_api_tasks_ - My Workspace 1](https://github.com/user-attachments/assets/1cb4acee-cdb9-4e55-bad8-311a347e1fa3)

- Searching the tasks using title, task progress
  
![http___127 0 0 1_8000_api_tasks_ - My Workspace serach](https://github.com/user-attachments/assets/788d56eb-df7b-4aa1-89ca-b53ba33c22c2)

- Using post adding new tasks 

![http___127 0 0 1_8000_api_tasks_ - My Workspace post](https://github.com/user-attachments/assets/db086f20-4ac5-47be-8a87-223ca0db2023)

- JWT authentication and using bearer token
  
![Token Obtain Pair – Django REST framework - Google Chrome 10_16_2024 2_39_47 PM](https://github.com/user-attachments/assets/e25563c1-6b7d-4664-abd2-0144b6b83a6d)

- Postgresql structure

  ![pgAdmin 4 10_16_2024 2_53_47 PM](https://github.com/user-attachments/assets/a2f383f4-2c16-4ece-b613-5522ef2e66fa)







 

    


   
