FROM python:3.10

WORKDIR /usr/app/src

COPY . ./
RUN pip install -e ./
RUN pip install --no-cache-dir -r requirements.txt

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait
RUN chmod +x ./run.sh

CMD /wait && ./run.sh