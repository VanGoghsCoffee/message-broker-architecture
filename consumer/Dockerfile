FROM ubuntu:18.04

RUN apt update

# Install add-apt-repository
RUN apt install -y software-properties-common

# Install Oracle Java
RUN apt remove -y java*
RUN add-apt-repository ppa:webupd8team/java
RUN apt update
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN apt install -y oracle-java8-installer

# Install scala
RUN apt install -y scala

# Install kafka
RUN apt install -y wget
RUN wget http://mirror.dkd.de/apache/kafka/1.1.0/kafka_2.12-1.1.0.tgz -P ~/Downloads
RUN mkdir ~/kafka
RUN tar -xvf ~/Downloads/kafka_2.12-1.1.0.tgz -C ~/kafka

# Create topic

# Run kafka consumer
CMD /root/kafka/kafka_2.12-1.1.0/bin/kafka-topics.sh --create --zookeeper ${KAFKA_ZOOKEEPER_CONNECT} --replication-factor 1 --partitions 1 --topic ${TOPIC} && /root/kafka/kafka_2.12-1.1.0/bin/kafka-console-consumer.sh --bootstrap-server ${KAFKA_CONNECT} --topic ${TOPIC} --from-beginning