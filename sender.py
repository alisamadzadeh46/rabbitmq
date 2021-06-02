import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# create dictionary message
message = {
    'info': 'this is information message',
    'error': 'this is error message',
    'warning': 'this is warning message',
}

# access to message ,k:key , v : value
for k, v in message.items():
    channel.basic_publish(
        exchange='direct_logs',
        routing_key=k,
        body=v,
    )

# this method close connection
connection.close()
