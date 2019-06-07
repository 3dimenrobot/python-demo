# _*_coding:utf-8_*_
__author__ = 'Alex Li'
import pika
import time


credentials = pika.PlainCredentials('alex', '123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.112.128',credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume('rpc_queue',on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()