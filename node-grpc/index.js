const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const PROTO_PATH = __dirname + "/protos/order.proto";
const options = {
  keepCase: true,
  longs: String,
  enums: String,
  defaults: true,
  oneofs: true,
};
const packageDefinition = protoLoader.loadSync(PROTO_PATH, options);
const orderProto = grpc.loadPackageDefinition(packageDefinition);

function findOrders(call, callback) {
  try {
    const search = call.request.search;
    callback(null, {
      orders: [
        { mongo_id: search, id: search, otn: search, tracking_number: search },
      ],
    });
  } catch (err) {
    callback(err, null);
  }
}

/**
 * Starts an RPC server that receives requests for the Greeter service at the
 * sample server port
 */
function main() {
  const server = new grpc.Server();
  server.addService(orderProto.OrderService.service, { find: findOrders });
  server.bindAsync(
    "0.0.0.0:50051",
    grpc.ServerCredentials.createInsecure(),
    (error) => {
      if (error) console.log(error);
      console.log("Server running at http://127.0.0.1:50051");
      server.start();
    }
  );
}

main();
