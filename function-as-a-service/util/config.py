
class Config:
    def __init__(self):
        self.KAFKA_QUEUE_HOSTNAME_PORT = "kafkaserver:9092"  ## localhost kafkaserver
        self.TOPIC_KEYS = ['function1']
        self.TOPIC_FLAGS = []

        #
        self.INSTANCE = "ec2-user@ec2-34-205-18-19.compute-1.amazonaws.com"

