import grpc
# import the generated classes
from carrier_protos import carrier_pb2
from carrier_protos import carrier_pb2_grpc
# open a gRPC channel
#channel = grpc.insecure_channel('localhost:50052')

###--------

with open('certs/tls.crt') as f:
     trusted_certs = f.read().encode()
# create credentials
credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
#channel = grpc.secure_channel('localhost:50052', credentials)
channel = grpc.secure_channel('delivery.gship.com:443', credentials)

###--------

#channel = grpc.insecure_channel('localhost:50052')

# create a stub (client)
stub = carrier_pb2_grpc.CarrierStub(channel)
# create a valid request message
carrier = carrier_pb2.GetCarrierRequest(weight = 200)
# make the call
response = stub.GetCarrier(carrier)
print response
