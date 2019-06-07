# _*_coding:utf-8_*_
__author__ = 'Alex Li'
import pika


credentials = pika.PlainCredentials('alex', '123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.112.128',credentials=credentials))


channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(queue="",exclusive=True)  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue_name,callback,auto_ack=True)

channel.start_consuming()