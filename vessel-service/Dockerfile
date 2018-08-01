FROM golang:1.8
WORKDIR /go/
RUN go get golang.org/x/net/http2
copy http2-test.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o http2-test . 

From debian:latest
RUN apt-get update && apt-get install -y \
  git \
  python-pip 

RUN python -m pip install -U pip 
RUN pip install grpcio grpcio-tools
WORKDIR /opt/
COPY --from=0 /go/http2-test .
copy . . 
EXPOSE 443
EXPOSE 9000

ENTRYPOINT ["/bin/bash","run.sh"]

