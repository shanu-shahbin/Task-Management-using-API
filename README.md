<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Management API</title>
</head>
<body>
    <h1>Task Management API</h1>
    <p>A simple task management REST API built with Django and Django REST Framework. This API allows users to create, read, update, and delete tasks, with support for user registration and authentication using JWT.</p>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#technologies">Technologies</a></li>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-the-application">Running the Application</a></li>
        <li><a href="#api-endpoints">API Endpoints</a></li>
        <li><a href="#authentication">Authentication</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
    </ul>

    <h2 id="features">Features</h2>
    <ul>
        <li>User registration and authentication using JWT.</li>
        <li>CRUD operations for tasks.</li>
        <li>Task search functionality by title, status, and priority.</li>
        <li>Task assignment to different users (many-to-one relationship).</li>
    </ul>

    <h2 id="technologies">Technologies</h2>
    <ul>
        <li><strong>Django</strong>: A high-level Python web framework.</li>
        <li><strong>Django REST Framework</strong>: A powerful toolkit for building Web APIs.</li>
        <li><strong>PostgreSQL</strong>: A powerful, open-source relational database.</li>
        <li><strong>JWT (JSON Web Tokens)</strong>: A compact, URL-safe means of representing claims to be transferred between two parties.</li>
    </ul>

    <h2 id="getting-started">Getting Started</h2>

    <h3 id="prerequisites">Prerequisites</h3>
    <p>Make sure you have the following installed:</p>
    <ul>
        <li>Python 3.8 or higher</li>
        <li>pip (Python package manager)</li>
        <li>PostgreSQL (if using PostgreSQL as the database)</li>
    </ul>

    <h3 id="installation">Installation</h3>
    <ol>
        <li><strong>Clone the repository</strong>:
            <pre><code>git clone https://github.com/yourusername/task-management-api.git
cd task-management-api</code></pre>
        </li>
        <li><strong>Create a virtual environment</strong>:
            <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
        </li>
        <li><strong>Install dependencies</strong>:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Configure the database</strong>:
            <p>Create a PostgreSQL database and user. Update the <code>DATABASES</code> settings in <code>settings.py</code> with your database credentials.</p>
        </li>
        <li><strong>Apply migrations</strong>:
            <pre><code>python manage.py migrate</code></pre>
        </li>
    </ol>

    <h3 id="running-the-application">Running the Application</h3>
    <ol>
        <li><strong>Start the development server</strong>:
            <pre><code>python manage.py runserver</code></pre>
        </li>
        <li><strong>Access the API</strong>: Open your browser and go to <code>http://localhost:8000/api/</code>.</li>
    </ol>

    <h2 id="api-endpoints">API Endpoints</h2>
    <h3>Authentication</h3>
    <ul>
        <li><strong>Register User</strong>: <code>POST /api/auth/register/</code></li>
        <li><strong>Obtain Token</strong>: <code>POST /api/token/</code></li>
        <li><strong>Refresh Token</strong>: <code>POST /api/token/refresh/</code></li>
    </ul>

    <h3>Task Management</h3>
    <ul>
        <li><strong>List Tasks</strong>: <code>GET /api/tasks/</code></li>
        <li><strong>Create Task</strong>: <code>POST /api/tasks/</code></li>
        <li><strong>Retrieve Task</strong>: <code>GET /api/tasks/&lt;task_id&gt;/</code></li>
        <li><strong>Update Task</strong>: <code>PUT /api/tasks/&lt;task_id&gt;/</code></li>
        <li><strong>Delete Task</strong>: <code>DELETE /api/tasks/&lt;task_id&gt;/</code></li>
    </ul>

    <h2 id="authentication">Authentication</h2>
    <p>To interact with the task management endpoints, you need to authenticate using JWT:</p>
    <ol>
        <li><strong>Register a new user</strong> using the registration endpoint.</li>
        <li><strong>Obtain a token</strong> by sending a POST request to <code>/api/token/</code> with your username and password.</li>
        <li><strong>Include the token</strong> in the Authorization header as a Bearer token for subsequent requests.</li>
    </ol>

    <h2 id="usage">Usage</h2>
    <p>You can use Postman to interact with the API. Follow these steps to create a new task:</p>
    <ol>
        <li>Set the request method to <strong>POST</strong>.</li>
        <li>Enter the URL: <code>http://localhost:8000/api/tasks/</code>.</li>
        <li>In the <strong>Authorization</strong> tab, select <strong>Bearer Token</strong> and enter your access token.</li>
        <li>In the <strong>Body</strong> tab, select <strong>raw</strong> and set the format to <strong>JSON</strong>, then enter the following JSON:</li>
    </ol>
    <pre><code>{
  "title": "Complete the report",
  "description": "Finish the quarterly report by end of the month.",
  "status": "pending",
  "priority": "high",
  "due_date": "2024-10-20"
}</code></pre>
    <p>Finally, click <strong>Send</strong> to create the task.</p>

    <h2 id="contributing">Contributing</h2>
    <p>Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.</p>

    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
</body>
</html>
