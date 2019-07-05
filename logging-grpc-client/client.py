import grpc
import Log_pb2
import Log_pb2_grpc
import socket


hostname = "localhost" # socket.gethostname()
print(hostname)
port = 9000
uri = "%s:%d" % (hostname, port)
print("Connecting to %s" % uri)
channel = grpc.insecure_channel(uri)

print("Starting channel...")
stub = Log_pb2_grpc.LogServiceStub(channel)

print("Connection up...")

log1 = Log_pb2.LogRequest()
log1.message = 'This is a sample log message.'
log1.type = 'Info'


# Synchronous
guid_1 = stub.Log(log1)
print("Logged with id %s." % str(guid_1).strip())

# Asynchronous
guid_2_future = stub.Log.future(log1)
guid_2 = guid_2_future.result()
print("Logged with id %s." % str(guid_2).strip())

channel.close()
