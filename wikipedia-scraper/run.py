from wikipedia_scraper.wikipedia_scraper.spiders.wikipedia import WikipediaSpider

import schedule
from scrapy import signals, log
from scrapy.crawler import CrawlerProcess, Crawler
from scrapy.utils.log import configure_logging
import time
from twisted.internet import reactor

import multiprocessing as mp

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})


def crawl():
    process = CrawlerProcess()
    crawler = Crawler(WikipediaSpider)
    process.crawl(crawler)
    process.start()


def job():
    p = mp.Process(target=crawl)
    p.start()
    p.join()



schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

    
