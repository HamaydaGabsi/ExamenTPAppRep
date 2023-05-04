import mysql.connector
import pika
import json
from CustomJSONEncoderDecoder  import CustomJSONDecoder;
# Connect to the HO database
ho_db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ho_sales"
)

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

# Bind the queue to the exchange with the routing key
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# Define a function to handle incoming sales data
def handle_sales_data(ch, method, properties, body):
    print(body)
    # Parse the JSON message body
    rows = json.loads(body,cls=CustomJSONDecoder)

    # Insert the sales data into the HO database
    cursor = ho_db.cursor()
    query = "INSERT INTO sales (id, product_name, sale_date) VALUES (%s, %s, %s)"
    for row in rows:
        values = (row[0], row[1], row[2])
        cursor.execute(query, values)
    ho_db.commit()
    cursor.close()

    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print('Received and processed sales data')

# Consume messages from the queue
channel.basic_consume(queue=queue_name, on_message_callback=handle_sales_data)

# Start consuming
print('Waiting for sales data...')
channel.start_consuming()
