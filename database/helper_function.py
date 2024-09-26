from datetime import datetime
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
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
#     return

def plat_graph_function(response):
    timestamps = []
    temperatures = []
    
    # Extract data for the graph and table
    for entry in response:
        dt = datetime.fromtimestamp(entry['created_at'])
        timestamps.append(dt)
        temperatures.append(entry['value'])
    
    # Create a DataFrame for the table
    data = {'Date & Time': timestamps, 'Temperature (°F)': temperatures}
    df = pd.DataFrame(data)
    
    # Create a PDF to save both the graph and the table
    with PdfPages('temperature_report.pdf') as pdf:
        
        # Plot the temperature graph
        plt.figure(figsize=(10, 5))
        plt.plot(timestamps, temperatures, marker='o')
        plt.title('Body Temperature Over Time')
        plt.xlabel('Date & Time')
        plt.ylabel('Temperature (°F)')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        
        # Save the graph to the PDF
        pdf.savefig()  # Save the current figure
        
        # Close the graph figure
        plt.close()
        
        # Add a new page with the table
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)
        
        # Save the table to the PDF
        pdf.savefig(fig)
        
        # Close the table figure
        plt.close()

    return