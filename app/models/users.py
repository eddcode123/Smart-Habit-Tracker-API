from mongoengine import (
    Document,
    StringField,
    IntField,
    ListField,
    EmailField,
    DateTimeField,
    connect,
)
from datetime import datetime

# Create a connection to the database
connect("smartHabit")  # Database name is 'smartHabit'

# Counter class for auto-incrementing IDs (Optional implementation)
class Counter:
    id = 0

    @classmethod
    def get_next_id(cls):
        cls.id += 1
        return cls.id


# Users collection schema
class Users(Document):
    """
    Schema for user data.
    """
    id = IntField(primary_key=True, default=Counter.get_next_id)
    email = EmailField(required=True, unique=True)
    password = StringField(max_length=100, required=True)
    created_on = DateTimeField(default=datetime.utcnow)
    time_zone = StringField(max_length=30, required=True)

    def __str__(self):
        return f"User({self.email})"


# Habits collection schema
class Habit(Document):
    """
    Schema for habit tracking.
    """
    habit_id = IntField(primary_key=True, default=Counter.get_next_id)
    title = StringField(max_length=100, required=True)
    start_date = DateTimeField(required=True)
    end_date = DateTimeField(required=True)
    streak = IntField(default=0)

    def __str__(self):
        return f"Habit({self.title}, Streak: {self.streak})"


# Notifications collection schema
class Notification(Document):
    """
    Schema for notifications.
    """
    notification_id = IntField(primary_key=True, default=Counter.get_next_id)
    user_id = IntField(required=True)  # Reference to Users' ID
    habit_id = IntField(required=True)  # Reference to Habits' ID
    notification_type = StringField(max_length=100, required=True)
    scheduled_time = DateTimeField(required=True)
    message = StringField(max_length=100, required=True)
    recurring = ListField(StringField(), default=[])
    sent_status = StringField(max_length=20, choices=["Sent", "Pending"], required=True)
    delivery_status = StringField(max_length=20, choices=["Delivered", "Failed"], required=True)
    created_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"Notification({self.message}, Status: {self.sent_status})"



# test data
