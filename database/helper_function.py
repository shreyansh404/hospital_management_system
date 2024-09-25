from datetime import datetime
import uuid

def get_greeting():
    """
        This function will return the greeting based on current time
    """
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"
    
def generate_unique_id():
    """
        This function will generate UUID
    """
    random_uuid = uuid.uuid4()
    uuid_integer = int(str(random_uuid.int)[:7])
    return uuid_integer