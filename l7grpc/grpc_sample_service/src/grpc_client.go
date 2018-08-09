package main

import (

	//"os"

	pb "echo"
	"flag"
	"log"
	"time"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/metadata"
)

const (
	userinfo_scope = "https://www.googleapis.com/auth/userinfo.email"
)

var ()

func main() {

	address := flag.String("host", "localhost:50051", "host:port of gRPC server")
	flag.Parse()

	ce, err := credentials.NewClientTLSFromFile("server_crt.pem", "")
	if err != nil {
		log.Fatalf("Failed to generate credentials %v", err)
	}

	conn, err := grpc.Dial(*address, grpc.WithTransportCredentials(ce))
	//conn, err := grpc.Dial(*address, grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	c := pb.NewEchoServerClient(conn)

	var testMetadata = metadata.MD{
		"sal":  []string{"value1"},
		"key2": []string{"value2"},
	}

	ctx := metadata.NewOutgoingContext(context.Background(), testMetadata)

	var header, trailer metadata.MD

	for i := 0; i < 10; i++ {
		r, err := c.SayHello(ctx, &pb.EchoRequest{Name: "unary RPC msg "}, grpc.Header(&header), grpc.Trailer(&trailer))
		if err != nil {
			log.Fatalf("could not greet: %v", err)
		}
		time.Sleep(1 * time.Second)
		log.Printf("RPC Response: %v %v", i, r)
	}

	/*
		stream, err := c.SayHelloStream(ctx, &pb.EchoRequest{Name: "Stream RPC msg"}, grpc.Header(&header))
		if err != nil {
			log.Fatalf("SayHelloStream(_) = _, %v", err)
		}
		for {
			m, err := stream.Recv()
			if err == io.EOF {
				t := stream.Trailer()
				log.Println("Stream Trailer: ", t)
				break
			}
			if err != nil {
				log.Fatalf("SayHelloStream(_) = _, %v", err)
			}

			h, err := stream.Header()
			if err != nil {
				log.Fatalf("stream.Header error _, %v", err)
			}
			log.Printf("Stream Header: ", h)
			log.Printf("Message: ", m.Message)

		}
	*/
}
