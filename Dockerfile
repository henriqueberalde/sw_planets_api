FROM python:3.10

WORKDIR /usr/app/src

COPY . ./
RUN pip install -e ./
RUN pip install --no-cache-dir -r requirements.txt
