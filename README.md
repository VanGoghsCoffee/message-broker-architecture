# Message-Broker-Architecture
A small architecture to get familiar with Apache Kafka. A scrapy web crawler takes a random article from the Wikipedia frontpage and publishes its title and introduction text to Kafka. From there it's read by a consumer service.

The application is dockerized. Since Kafka needs Zookeeper and the Consumer needs Kafka it's advisable to start the services one after another (I could have solved this with a waitfor script but didn't want to over-engineer things ;) )
Just run:

```
docker-compose up -d zookeeper
docker-compose up -d kafka
docker-compose up -d consumer scraper
```