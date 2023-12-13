from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message transmis au {msg.topic()}\n----------------------------")

def produce_messages():
    p = Producer({'bootstrap.servers': 'localhost:9092'})

    p.produce('topic-delivered', "delivery_done", callback=delivery_report)

    p.flush()

if __name__ == '__main__':
    produce_messages()
