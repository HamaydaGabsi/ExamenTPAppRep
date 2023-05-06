import mysql.connector
import pika
import json
import time
from CustomJSONEncoderDecoder  import CustomJSONEncoder;

# Connect to the BO database
bo2_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bo2_sales"
)



# Define a function to send sales data to the HO database
def send_sales_data():
    # Connect to the RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the exchange and queue names
    exchange_name = 'sales_exchange'
    queue_name = 'ho_sales_queue'
    routing_key = 'sales.ho'

    # Declare the exchange
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')


    # Declare the queue
    channel.queue_declare(queue=queue_name)

    # Bind the queue to the exchange
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)
    # Fetch the latest sales data from the BO database where isSync is False
    cursor = bo2_db.cursor()
    query = "SELECT * FROM sales WHERE isSync = 0 ORDER BY sale_date DESC LIMIT 10"
    cursor.execute(query)
    rows = cursor.fetchall()
    rows.append("2")
    cursor.close()

    # Convert the rows to a JSON string and send it to the HO database
    message = json.dumps(rows, cls=CustomJSONEncoder)
    # Publish the message to RabbitMQ
    channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=message)

    # Update the isSync column for the rows that were sent
    cursor = bo2_db.cursor()
    update_query = "UPDATE sales SET isSync = 1 WHERE id IN (%s)"
    update_query_params = ', '.join(str(row[0]) for row in rows)
    cursor.execute(update_query % update_query_params)
    bo2_db.commit()
    cursor.close()

    print('Sent sales data to HO database')
    # Close the connection
    connection.close()

# Start the sending loop
