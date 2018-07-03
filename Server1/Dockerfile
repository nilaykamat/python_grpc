From debian:latest
RUN apt-get update && apt-get install -y \
  git \
  python-pip 

RUN python -m pip install -U pip 
RUN pip install grpcio grpcio-tools
WORKDIR /opt/

copy . . 
EXPOSE 50051

ENTRYPOINT ["bash","run.sh"]

