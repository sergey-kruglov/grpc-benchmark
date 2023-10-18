import asyncio
import logging

import grpc

import order_pb2
import order_pb2_grpc

_cleanup_coroutines = []


class Order(order_pb2_grpc.OrderServiceServicer):
    async def Find(self, request: order_pb2.FindRequest, context: grpc.aio.ServicerContext):
        return order_pb2.FindReply(orders=[])


async def run() -> None:
    server = grpc.aio.server()
    order_pb2_grpc.add_OrderServiceServicer_to_server(Order(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()

    async def server_graceful_shutdown():
        logging.info("Starting graceful shutdown...")
        # Shuts down the server with 5 seconds of grace period. During the
        # grace period, the server won't accept new connections and allow
        # existing RPCs to continue within the grace period.
        await server.stop(5)

    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()
