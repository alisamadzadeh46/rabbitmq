import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new queue
# This method creates or checks a queue
channel.queue_declare(queue='hi')

# send simple message
# if empty exchange,means direct exchange
channel.basic_publish(
    exchange='',
    routing_key='hi',
    body='hello world')

print('Message send')

# this method close connection
connection.close()
