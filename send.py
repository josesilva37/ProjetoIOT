import pika

#Read BLE Data

#Send BLE Data to Broker
host = '192.168.1.158'
credentials = pika.PlainCredentials("admin", "admin")
parameters = pika.ConnectionParameters(host, 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='battery')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()