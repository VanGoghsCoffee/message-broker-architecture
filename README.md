# Message-Broker-Architecture
A small architecture to get familiar with Apache Kafka. A scrapy web crawler takes a random article from the Wikipedia frontpage and publishes its title and introduction text to Kafka. From there it's read by a consumer service.

The application is dockerized. Build all the images locally

```
docker build -t davidrochholz/zookeeper ./zookeeper
docker build -t davidrochholz/kafka ./kafka
docker build -t davidrochholz/consumer ./consumer
docker build -t davidrochholz/scraper ./wikipedia-scraper
```

Since Kafka needs Zookeeper and the Consumer needs Kafka it's advisable to start the services one after another (I could have solved this with a waitfor script but didn't want to over-engineer things ;) )
Just run:

```
docker-compose up -d zookeeper
docker-compose up -d kafka
docker-compose up -d consumer scraper
```

Check the logs of the consumer container for the scraping results. You can also attach to the container...