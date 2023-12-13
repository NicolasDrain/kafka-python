from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message transmis au {msg.topic()}\n----------------------------")

def produce_messages():
    p = Producer({'bootstrap.servers': 'localhost:9092'})

    for i in range(5):  # Envoyer 5 messages
        p.produce('topic-delivered', f"Message {i}", callback=delivery_report)

    p.flush()

if __name__ == '__main__':
    produce_messages()
