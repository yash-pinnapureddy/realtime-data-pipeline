import time
import logging
import random
import signal
import sys
from datetime import datetime
from confluent_kafka.avro import AvroProducer
from confluent_kafka.avro.serializer import SerializerError
from confluent_kafka import avro

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

# Kafka config
KAFKA_BROKER = 'localhost:9092'
SCHEMA_REGISTRY_URL = 'http://localhost:8081'
TOPIC_NAME = 'stock-prices'

# Avro schema definition
value_schema_str = """
{
  "namespace": "stock.market",
  "type": "record",
  "name": "StockPrice",
  "fields": [
    {"name": "timestamp", "type": "string"},
    {"name": "symbol", "type": "string"},
    {"name": "price", "type": "float"},
    {"name": "volume", "type": "int"}
  ]
}
"""

value_schema = avro.loads(value_schema_str)

# Optional: Key schema if using partitioned topics
key_schema_str = """
{
  "type": "string"
}
"""

key_schema = avro.loads(key_schema_str)

# Producer config
producer_config = {
    'bootstrap.servers': KAFKA_BROKER,
    'schema.registry.url': SCHEMA_REGISTRY_URL,
    'acks': 'all',
    'retries': 3
}

# Create AvroProducer
producer = AvroProducer(
    config=producer_config,
    default_key_schema=key_schema,
    default_value_schema=value_schema
)

# Handle graceful shutdown
def shutdown_handler(sig, frame):
    logging.info("Shutting down producer...")
    producer.flush()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

# Simulated stock data
symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

def generate_event():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "symbol": random.choice(symbols),
        "price": round(random.uniform(100, 1500), 2),
        "volume": random.randint(100, 10000)
    }

# Produce loop
if __name__ == "__main__":
    logging.info("🔃 Kafka Avro producer started.")
    while True:
        try:
            event = generate_event()
            key = event["symbol"]
            producer.produce(topic=TOPIC_NAME, key=key, value=event)
            logging.info(f"✅ Produced: {event}")
        except SerializerError as e:
            logging.error(f"❌ Serialization error: {e}")
        except Exception as e:
            logging.exception(f"❌ Unexpected error during produce: {e}")
        time.sleep(1)
