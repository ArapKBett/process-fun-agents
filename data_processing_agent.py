import requests
import pandas as pd

def fetch_and_process_data():
    print("Fetching and processing data...")
    response = requests.get('https://api.example.com/data')
    data = response.json()
    
    # Convert data to a DataFrame
    df = pd.DataFrame(data)
    
    # Process data (example: calculate summary statistics)
    summary = df.describe()
    print(summary)
    
    # Save processed data to a CSV file
    df.to_csv('processed_data.csv', index=False)
    
    return summary
