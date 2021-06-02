import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new exchange
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# create message replace command line or terminal
message = 'This is testing message'

# send simple message
# if empty exchange,means direct exchange
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message,
)

print('Message send')

# this method close connection
connection.close()
