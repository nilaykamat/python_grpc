
import grpc
# import the generated classes
from vessel_protos import vessel_pb2
from vessel_protos import vessel_pb2_grpc
# open a gRPC channel
#channel = grpc.insecure_channel('localhost:50052')
#channel = grpc.insecure_channel('35.232.149.193:50052')

###--------

with open('tls.crt') as f:
    trusted_certs = f.read().encode()
# create credentials
credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
#channel = grpc.secure_channel('localhost:50052', credentials)
#channel = grpc.secure_channel('vessel:50052', credentials)
#channel = grpc.secure_channel('shippy.example.com:50052', credentials)
channel = grpc.secure_channel('shippy.example.com:443', credentials)

###--------

#channel = grpc.insecure_channel('35.237.1.120:80')

# create a stub (client)
stub = vessel_pb2_grpc.VesselStub(channel)
# create a valid request message
vessel = vessel_pb2.GetVesselRequest(weight = 200)
# make the call
response = stub.GetVessel(vessel)
print response
