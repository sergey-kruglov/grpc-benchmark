package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"

	pb "github.com/sergey-kruglov/grpc-test/go-grpc/order"
	"google.golang.org/grpc"
)

var (
	port = flag.Int("port", 50051, "The server port")
)

type server struct {
	pb.UnimplementedOrderServiceServer
}

func (s *server) Find(ctx context.Context, in *pb.FindRequest) (*pb.FindReply, error) {
	search := in.GetSearch()
	orders := []*pb.OrderData{}
	order := pb.OrderData{MongoId: search, Id: search, Otn: search, TrackingNumber: search}
	orders = append(orders, &order)
	return &pb.FindReply{Orders: orders}, nil
}

func main() {
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterOrderServiceServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
