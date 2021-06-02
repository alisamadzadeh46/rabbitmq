import time

import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new queue

channel.exchange_declare(exchange='logs', exchange_type='fanout')

# This method creates or checks a queue
result = channel.queue_declare(queue='', exclusive=True)

# receive queue name
qname = result.method.queue

# create bind
channel.queue_bind(exchange='logs', queue=qname)

print('waiting  for logs')


# create callback fun
def callback(ch, method, properties, body):
    print(f'Receive {body}')


channel.basic_consume(
    queue=qname,
    on_message_callback=callback,
    auto_ack=True)

# start consuming
channel.start_consuming()
