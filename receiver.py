import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new queue
# This method creates or checks a queue
channel.queue_declare(queue='hi')


# body: this parameter reading from within the queue
def callback(ch, method, properties, body):
    print(f'Received {body}')


# Consume to the broker and binds messages
# for the consumer_tag to the consumer callback
channel.basic_consume(
    queue='hi',
    on_message_callback=callback,
    auto_ack=True
)

print('waiting for message , to exit press ctrl+c')

# start consuming
channel.start_consuming()
