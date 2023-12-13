from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message transmis au {msg.topic()}\n----------------------------")

def produce_messages(state_production):
    p = Producer({'bootstrap.servers': 'localhost:9092'})

    p.produce('topic-produced', state_production, callback=delivery_report)

    p.flush()

if __name__ == '__main__':
    produce_messages("production_finished")
