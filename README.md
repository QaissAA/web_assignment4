Secure Task Manager

Overview
Secure Task Manager is a Flask-based web application that allows users to manage tasks securely. It includes user authentication, task creation, and task management with MongoDB as the database.

Features
- User authentication (registration & login with JWT)
- Secure password hashing using bcrypt
- Task management (Create, Read, Update, Delete)
- Role-based access control
- Secure API endpoints with CSRF protection
- Uses MongoDB Atlas for data storage

Installation
1. Clone the repository:

   git clone 
   cd secure-task-manager

2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate 
3. Install dependencies:
   pip install -r requirements.txt
4. Set up environment variables:
   - Create a `.env` file in the root directory and add:
     MONGO_URI=your_mongodb_connection_string
     JWT_SECRET=your_jwt_secret_key
5. Run the application:
   python app.py
6. Open the browser and visit:
   http://localhost:5000

Folder Structure

secure_task_manager/
│── app.py
│── models/
│   ├── user.py
│   ├── task.py
│── routes/
│   ├── auth.py
│   ├── task.py
│── views/
│   ├── index.html
│── config/
│   ├── settings.py
│── requirements.txt
│── .env (not included in repo)


