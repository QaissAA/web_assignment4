import os
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/task_manager')
JWT_SECRET = os.getenv('JWT_SECRET', 'your_secret_key')
