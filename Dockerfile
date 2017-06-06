FROM python
RUN pip install psycopg2
RUN apt-get update
RUN apt-get install -y postgresql-client
COPY app.py app.py
COPY wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh
