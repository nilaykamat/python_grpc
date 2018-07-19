
import grpc
# import the generated classes
from vessel_protos import vessel_pb2
from vessel_protos import vessel_pb2_grpc
# open a gRPC channel
#channel = grpc.insecure_channel('localhost:50052')
channel = grpc.insecure_channel('shippy.example.com')
# create a stub (client)
stub = vessel_pb2_grpc.VesselStub(channel)
# create a valid request message
vessel = vessel_pb2.GetVesselRequest(weight = 100)
# make the call
response = stub.GetVessel(vessel)
print response

