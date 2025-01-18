from flask import Flask, request, jsonify
import schedule
import time
import threading
from data_processing_agent import fetch_and_process_data
from email_notification_agent import send_email
from fun_agent import send_fun_fact

app = Flask(__name__)

# Main Agent Task
def main_task():
    summary = fetch_and_process_data()
    send_email('Daily Data Summary', summary.to_string(), 'recipient@example.com')
    fun_fact = send_fun_fact()
    send_email('Daily Fun Fact', fun_fact, 'recipient@example.com')

# Schedule the main task to run daily at 9 AM
schedule.every().day.at("09:00").do(main_task)

# Function to run the scheduler in a separate thread
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Process the data here
    print(data)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(port=5000)
