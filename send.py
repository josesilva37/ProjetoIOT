import pika


#Read BLE Data



#Send BLE Data to Broker
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedometer')

channel.basic_publish(exchange='', routing_key='pedometer', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()