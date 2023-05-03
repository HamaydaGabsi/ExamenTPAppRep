import mysql.connector
import pika
import json
import time
from CustomJSONEncoder  import CustomJSONEncoder;

# Connect to the BO database
bo1_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bo1_sales"
)



# Define a function to send sales data to the HO database
def send_sales_data():
    # Connect to the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the and queue names
    queue_name = 'bo1_sales_queue'

    # Declare the queue
    channel.queue_declare(queue=queue_name)
    # Fetch the latest sales data from the BO database
    cursor = bo1_db.cursor()
    query = "SELECT * FROM sales ORDER BY sale_date DESC LIMIT 10"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    # Convert the rows to a JSON string and send it to the HO database
    message =json.dumps(rows, cls=CustomJSONEncoder)
    # print(rows)
    channel.basic_publish(exchange='', routing_key=queue_name, body=message)

    print('Sent sales data to HO database')
    # Close the connection
    connection.close()

# Start the sending loop


send_sales_data()



