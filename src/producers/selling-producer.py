from confluent_kafka import Producer

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message transmis au {msg.topic()}\n----------------------------")

def produce_messages(model):
    p = Producer({'bootstrap.servers': 'localhost:9092'})

    p.produce('topic-sold', model, callback=delivery_report)

    p.flush()

if __name__ == '__main__':
    running = True
    number_cars = 0
    model = input("Quel modèle souhaitez-vous achetez ? Les valeurs acceptées sont M, I, A, G, E\n")
    while model not in ["M", "I", "A", "G", "E"]:
        model = input("Erreur le modèle saisi n'est pas valide veuillez indiquer un nouveau model, les valeurs acceptées sont M, I, A, G, E\n")
    number_cars +=1
    produce_messages(model)
