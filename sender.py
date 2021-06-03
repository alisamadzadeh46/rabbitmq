import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# create dictionary message
message = {
    'info.debug,NotImportant': 'this is an not important message',
    'error.warning.important': 'this is an important message',
}

# access to message ,k:key , v : value
for k, v in message.items():
    channel.basic_publish(
        exchange='topic_logs',
        routing_key=k,
        body=v,
    )

print('Sent')

# this method close connection
connection.close()
