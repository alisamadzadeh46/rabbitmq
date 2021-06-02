import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)

qname = result.method.queue

message = 'error'

channel.queue_bind(exchange='direct_logs', queue=qname, routing_key=message)

print('Waiting for message')


def callback(ch, method, properties, body):
    with open('error_logs.log', 'a') as el:
        el.write(str(f'{body}') + '\n')


channel.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
