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
const OrderService = grpc.loadPackageDefinition(packageDefinition).OrderService;

const client = new OrderService(
  "localhost:50051",
  grpc.credentials.createInsecure()
);

function request() {
  return new Promise((resolve, reject) => {
    client.find({ search: "test" }, (error, data) => {
      if (error) {
        reject(error);
      }
      resolve(data);
    });
  });
}

async function main() {
  console.time("perf");

  const promises = [];
  for (let i = 0; i < 10000; i++) {
    promises.push(request());
  }

  await Promise.all(promises);
  console.timeEnd("perf");
}

main().catch((err) => {
  throw err;
});
