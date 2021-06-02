# rabbitmq
rabbitmq

# Description

1. direct exchange 

if you give Routing Key, direct exchange found queues and set

![alt text](https://alisamadzadeh.ir/rabbitmq/DirectExchange1.png)

2. headers exchange 

In rabbitmq, headers exchanges will use the message header attributes for routing.
Following is the pictorial representation of message flow in rabbitmq headers exchange.

![alt text](https://alisamadzadeh.ir/rabbitmq/HeadersExchange2.png)


3. topic exchange 

In rabbitmq, topic exchange will perform a wildcard match between the routing key and the routing pattern specified in the binding to publish a messages to queue.
Following is the pictorial representation of message flow in rabbitmq topic exchange.

![alt text](https://alisamadzadeh.ir/rabbitmq/TopicExchange2.png)

4.fanout exchange

In rabbitmq, fanout exchange will route messages to all of the queues that are bound to it.
Following is the pictorial representation of message flow in rabbitmq fanout exchange.

![alt text](https://alisamadzadeh.ir/rabbitmq/rabbitmq_fanout_exchange_process_flow_diagram.png)

# Resource
1.https://www.tutlane.com/tutorial/rabbitmq/rabbitmq-exchanges

![alt text](https://alisamadzadeh.ir/rabbitmq/exchanges-bidings-routing-keys.png)
