from confluent_kafka import Consumer, KafkaException
import subprocess

def consume_messages():
    c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup', 'auto.offset.reset': 'earliest'})
    c.subscribe(['topic-delivered'])
    try:
        while True:
            msg = c.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(f"Consumer error: {msg.error()}")
                    break

            print("La livraison a bien été effectuée. Vous pouvez désormais acheter d'autres voitures\n----------------------------")
            execute_selling_producer()

    except KeyboardInterrupt:
        pass

    finally:
        c.close()
def execute_selling_producer():
    chemin_fichier = "src/producers/selling-producer.py"
    subprocess.run(["python", chemin_fichier])

if __name__ == '__main__':
    consume_messages()
