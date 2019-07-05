import grpc
import Log_pb2
import Log_pb2_grpc
import socket


def main():
    hostname = socket.gethostname()
    print(hostname)
    port = 9000
    uri = "%s:%d" % (hostname, port)
    print("Connecting to %s" % uri)
    channel = grpc.insecure_channel(uri)

    print("Starting channel...")
    stub = Log_pb2_grpc.LogServiceStub(channel)

    print("Connection up...")

    log1 = Log_pb2.LogRequest()
    log1.log.message = 'This is a sample log message.'
    log1.log.type = Log_pb2.LogMessage.INFO

    # Synchronous
    guid_1 = stub.Log(log1)
    print("Logged with id %s." % str(guid_1).strip())

    # Asynchronous
    guid_2_future = stub.Log.future(log1)
    guid_2 = guid_2_future.result()
    print("Logged with id %s." % str(guid_2).strip())

    print(stub.GetLog(guid_1))
    print(stub.GetLog(guid_2))

    # Get all
    print("==GETTING ALL LOGS==")
    for log in stub.GetAllLogs(Log_pb2.GetAllRequest()):
        print(log)
    channel.close()


if __name__ == "__main__":
    main()
