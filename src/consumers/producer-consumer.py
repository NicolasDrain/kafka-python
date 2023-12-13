from confluent_kafka import Consumer, KafkaException
import time
import subprocess
import os

def consume_messages():
    c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup', 'auto.offset.reset': 'earliest'})
    c.subscribe(['topic-sold'])
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

            print(f"Demande de construction reçue, modèle {msg.value().decode('utf-8')} demandé")
            model = msg.value().decode('utf-8')
            match model:
                case "M":
                    print("La construction du modèle %s est en cours cela va prendre 10 secondes\n----------------------------"%model)
                    time.sleep(10)
                case "I":
                    print("La construction du modèle %s est en cours cela va prendre 2 secondes\n----------------------------"%model)
                    time.sleep(2)
                case "A":
                    print("La construction du modèle %s est en cours cela va prendre 3 secondes\n----------------------------"%model)
                    time.sleep(3)
                case "G":
                    print("La construction du modèle %s est en cours cela va prendre 4 secondes\n----------------------------"%model)
                    time.sleep(4)
                case "E":
                    print("La construction du modèle %s est en cours cela va prendre 7 secondes\n----------------------------"%model)
                    time.sleep(7)
            print("La construction de votre voiture modèle %s est terminée\n----------------------------"%model)
            execute_producer_producer()
    except KeyboardInterrupt:
        pass

    finally:
        c.close()

def execute_producer_producer():
    chemin_fichier = "src/producers/producer-producer.py"
    subprocess.run(["python", chemin_fichier])

if __name__ == '__main__':
    consume_messages()
