import time

import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new queue
# This method creates or checks a queue
channel.queue_declare(queue='one')


# body: this parameter reading from within the queue
def callback(ch, method, properties, body):
    print(f'Received {body}')
    time.sleep(9)
    print('Done')
    channel.basic_ack(delivery_tag=method.delivery_tag)


# Consume to the broker and binds messages
# for the consumer_tag to the consumer callback
channel.basic_consume(
    queue='one',
    on_message_callback=callback,
    auto_ack=True
)

channel.basic_qos(prefetch_count=1)
print('waiting for message , press ctrl+c to exit ')

# start consuming
channel.start_consuming()
