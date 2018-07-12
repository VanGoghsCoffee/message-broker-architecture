import os
import random
import re
import scrapy
from kafka import KafkaProducer
import json


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    start_urls = [
        "https://en.wikipedia.org/wiki/Main_Page"
    ]
    TAG_RE = re.compile(r'<[^>]+>')
    
    def parse(self, response):
        urls = response.xpath('//table[@id="mp-upper"]//a/@href').extract()
        random_link = random.choice(self.clean_imgs_and_links_from_urls(urls))

        yield scrapy.Request(
            url=response.urljoin(random_link),
            callback=self.parse_title_and_intro
        )

    def parse_title_and_intro(self, response):
        title = response.xpath(
            '//h1[@id="firstHeading"]/text()'
        ).extract_first()

        intro_html = ''.join(response.xpath(
            '//table[contains(@class, "infobox") and contains(@class, "vcard")]'\
            '/following-sibling::p[following::div[@id="toc"]]/node()'
            ).extract())
        intro = self.strip_content_from_html(intro_html)
        wikipedia_article = {
            'title': title,
            'intro': intro
        }

        producer = KafkaProducer(
            bootstrap_servers=os.getenv("KAFKA_CONNECT"),
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        producer.send(os.getenv("TOPIC"), wikipedia_article)
        producer.close()
        yield wikipedia_article

    def strip_content_from_html(self, html):
        return self.TAG_RE.sub('', html)
        
    def clean_imgs_and_links_from_urls(self, urls):
        clean_urls = []

        for url in urls:
            if "File:" not in url \
               and "https://" not in url \
               and "http://" not in url:
                clean_urls.append(url)

        return clean_urls
