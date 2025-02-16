from mongoengine import Document, StringField, ReferenceField, DateTimeField
from models.user import User
from datetime import datetime

class Task(Document):
    title = StringField(required=True)
    description = StringField()
    status = StringField(choices=["Pending", "Completed"], default="Pending")
    created_at = DateTimeField(default=datetime.utcnow)
    user = ReferenceField(User, required=True)
