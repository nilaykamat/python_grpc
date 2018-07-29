FROM debian:latest
RUN apt-get update && apt-get install -y \
  git \
  python-pip 

RUN python -m pip install -U pip 
RUN pip install grpcio grpcio-tools flask
WORKDIR /opt/

COPY . . 
EXPOSE 5000

ENTRYPOINT ["python","run.py"]

