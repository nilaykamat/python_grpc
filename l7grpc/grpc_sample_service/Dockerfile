FROM golang:1.8 as build

RUN apt-get update -y && apt-get install -y build-essential wget unzip curl


RUN curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip && \
    unzip protoc-3.2.0-linux-x86_64.zip -d protoc3 && \
    mv protoc3/bin/* /usr/local/bin/ && \
    mv protoc3/include/* /usr/local/include/


WORKDIR /go/

RUN go get github.com/golang/protobuf/proto \
           github.com/golang/protobuf/protoc-gen-go \
           golang.org/x/net/context \
           google.golang.org/grpc \
           google.golang.org/grpc/credentials \
           golang.org/x/oauth2 \
           golang.org/x/net/http2
ADD . /go/

RUN protoc --go_out=plugins=grpc:. src/echo/echo.proto

RUN export GOBIN=/go/bin && go install src/grpc_server.go
RUN export GOBIN=/go/bin && go install src/grpc_client.go


FROM gcr.io/distroless/base
COPY --from=build /go/server_crt.pem /
COPY --from=build /go/server_key.pem /
COPY --from=build /go/CA_crt.pem /
COPY --from=build /go/bin /


EXPOSE 8081
EXPOSE 443

#ENTRYPOINT ["grpc_server"]
#ENTRYPOINT ["grpc_client", "--host",  "main.esodemoapp2.com:443"]
