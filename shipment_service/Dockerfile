FROM debian:latest
RUN apt-get update && apt-get install -y \
  git \
  python-pip 

RUN python -m pip install -U pip 
RUN pip install grpcio grpcio-tools
WORKDIR /opt/

COPY . . 
EXPOSE 50051

ENTRYPOINT ["python","server.py"]

