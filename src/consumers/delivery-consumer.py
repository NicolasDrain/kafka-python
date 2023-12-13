from confluent_kafka import Consumer, KafkaException
import time
import subprocess

def consume_messages():
    c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'mygroup', 'auto.offset.reset': 'earliest'})
    c.subscribe(['topic-produced'])
    number_cars_built = 0

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

            print("Nouveau message reçu, une nouvelle voiture a été produite")
            number_cars_built+=1
            if(number_cars_built == 10):
                print("Un total de 10 voitures ont été produites la livraison commence et prends 2 secondes, veuillez-patienter\n----------------------------")
                time.sleep(2)
                number_cars_built = 0
                execute_selling_consumer()
                
            else:
                print("Vous avez actuellement %d voitures produites, la livraison sera effectuée à 10 voitures\n----------------------------" %number_cars_built)
                execute_selling_producer()

    except KeyboardInterrupt:
        pass

    finally:
        c.close()


def execute_selling_producer():
    chemin_fichier = "src/producers/selling-producer.py"
    subprocess.run(["python", chemin_fichier])

def execute_selling_consumer():
    chemin_fichier = "src/consumers/selling-consumer.py"
    subprocess.run(["python", chemin_fichier])

if __name__ == '__main__':
    consume_messages()
