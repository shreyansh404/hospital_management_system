from datetime import datetime
import uuid
import matplotlib.pyplot as plt

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

def plat_graph_function(response):
    timestamps = []
    temperatures = []
    print(response)
    for entry in response:
        dt = datetime.fromtimestamp(entry['created_at'])
        timestamps.append(dt)
        temperatures.append(entry['value'])

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o')
    plt.title('Body Temperature Over Time')
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°F)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.tight_layout()

    plt.savefig('temperature_report.pdf')  # Save as PDF
    plt.show()
    return