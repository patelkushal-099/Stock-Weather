import grpc
import example_pb2
import example_pb2_grpc

def run():
    # Create a channel to the server
    channel = grpc.insecure_channel('localhost:50051')

    # Create a stub (client)
    stub = example_pb2_grpc.ExampleServiceStub(channel)

    # Create a request
    request = example_pb2.ExampleRequest(name='test')

    # Make the call
    response = stub.ExampleMethod(request)

    # Print the response
    print(f"Response message: {response.message}")

if __name__ == '__main__':
    run()
