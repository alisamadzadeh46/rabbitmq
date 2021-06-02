import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new queue
# This method creates or checks a queue
# when True durable, when restart server or crash information  write in hard , Survive reboots of the broker
channel.queue_declare(queue='one', durable=True)

# create message replace command line or terminal
message = 'This is testing message'

# send simple message
# if empty exchange,means direct exchange
channel.basic_publish(
    exchange='',
    routing_key='one',
    body=message,
    properties=pika.BasicProperties(delivery_mode=2,)
)

print('Message send')

# this method close connection
connection.close()
