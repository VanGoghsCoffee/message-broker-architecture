FROM python:3.6

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY ./run.py /usr/src/app/
COPY wikipedia_scraper /usr/src/app/wikipedia_scraper

CMD ["python", "run.py"]
