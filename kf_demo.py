from kafka import KafkaProducer, KafkaConsumer

# create Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# send messages to Kafka topic
producer.send('my-topic', b'Hello, World!')

# create Kafka consumer
consumer = KafkaConsumer('my-topic', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')

# read messages from Kafka topic
for message in consumer:
    print(message.value.decode())
