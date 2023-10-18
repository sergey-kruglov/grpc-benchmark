package main

import (
	"context"
	"flag"
	"log"
	"sync"
	"time"

	pb "github.com/sergey-kruglov/grpc-test/go-grpc/order"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

var (
	addr = flag.String("addr", "localhost:50051", "the address to connect to")
)

func main() {
	flag.Parse()
	// Set up a connection to the server.
	conn, err := grpc.Dial(*addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewOrderServiceClient(conn)

	var wg sync.WaitGroup
	start := time.Now()
	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go makeRequest(c, &wg)
	}
	wg.Wait()
	log.Println(time.Since(start))
}

func makeRequest(c pb.OrderServiceClient, wg *sync.WaitGroup) {
	defer wg.Done()
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()
	_, err := c.Find(ctx, &pb.FindRequest{Search: "test"})
	if err != nil {
		log.Fatalf("could not greet: %v", err)
	}
}
