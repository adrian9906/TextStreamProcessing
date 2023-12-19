from kafka import KafkaProducer
from kafka import KafkaConsumer
import json
import time

def json_serializer(datos):
    return json.dumps(datos).encode("utf-8")

def Producer(server,topic,data):
    producer=KafkaProducer(bootstrap_servers=[server+':9092'],value_serializer=json_serializer)
    producer.send(topic=topic,value=data)
    time.sleep(0.8)
    
def Consumer(server,topic,auto_offset_reset,groupID):
    consumer=KafkaConsumer(topic,bootstrap_servers=[server+':9092'],auto_offset_reset=auto_offset_reset,enable_auto_commit=True,group_id=groupID)
    consumer.subscribe([topic])
    return consumer