import grpc

# import the generated classes
from consignment_protos import consignment_pb2
from consignment_protos import consignment_pb2_grpc

# open a gRPC channel
#channel = grpc.insecure_channel('35.239.89.67:50051')
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = consignment_pb2_grpc.ShippingStub(channel)

# create a valid request message
consignment = consignment_pb2.GetConsignmentRequest(consignment_id = 3)

# make the call
response = stub.GetConsignment(consignment)
print response

print "getting vessel for consignment"

vessel = consignment_pb2.Consignment(id = response.id, name = response.name, weight = response.weight)
vessel_response = stub.GetVesselForConsignment(vessel)
print vessel_response