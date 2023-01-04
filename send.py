import pika

#Read BLE Data

#Send BLE Data to Broker
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='data', exchange_type='fanout')
# channel.queue_declare(queue='pedometer')

channel.basic_publish(exchange='', routing_key='pedometer', body='Test')
print(" [x] Sent 'Hello World!'")
connection.close()