import subprocess
import multiprocessing
import time


def execute_consumer(file_path):
    subprocess.run(["python", file_path])
    time.sleep(1)


def execute_delivery_producer():
    delivery_consumer = "src/consumers/delivery-consumer.py"
    producer_consumer = "src/consumers/producer-consumer.py"
    selling_consumer = "src/consumers/selling-consumer.py"
    selling_producer = "src/producers/selling-producer.py"

    processes = [
        multiprocessing.Process(target=execute_consumer, args=(delivery_consumer,)),
        multiprocessing.Process(target=execute_consumer, args=(producer_consumer,)),
        multiprocessing.Process(target=execute_consumer, args=(selling_consumer,)),
        multiprocessing.Process(target=execute_consumer, args=(selling_producer,))
    ]

    for process in processes:
        process.start()

    # Attente de la fin de chaque processus
    for process in processes:
        process.join()

if __name__ == '__main__':
    execute_delivery_producer()
