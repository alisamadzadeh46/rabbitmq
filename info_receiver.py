import pika

# if you use server , replace 'localhost' to ip server
# create new connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# create new channel
channel = connection.channel()

# create new exchange
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)

qname = result.method.queue

binding_key = '#.notimportant'

channel.queue_bind(exchange='topic_logs', queue=qname, routing_key=binding_key)

print('Waiting for message')


def callback(ch, method, properties, body):
    print(body)


channel.basic_consume(queue=qname, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
