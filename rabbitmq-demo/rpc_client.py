import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):

        credentials = pika.PlainCredentials('alex', '123')
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            '192.168.112.128', credentials=credentials))

        self.connection = connection

        self.channel = self.connection.channel()

        result = self.channel.queue_declare("",exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.callback_queue,self.on_response, auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events() # 检查队列里有没有新消息，但是不会阻塞
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)
print(" [.] Got %r" % response)