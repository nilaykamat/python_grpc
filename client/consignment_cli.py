import grpc
from google.protobuf import json_format
# import the generated classes
from consignment_protos import consignment_pb2
from consignment_protos import consignment_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')
# channel = grpc.insecure_channel('consignment:50051')

# create a stub (client)
stub = consignment_pb2_grpc.ShippingStub(channel)

# Function to get consignment
def get_consignment(consignment_id):
    # create a valid request message
    consignment = consignment_pb2.GetConsignmentRequest(consignment_id = consignment_id)

    # make the call
    response = stub.GetConsignment(consignment)
    # return response in JSON format rather than object
    return json_format.MessageToJson(response)

# function to get vessels for consignment
def get_vessel(consignment_id, consignment_name, consignment_weight):
    print "getting vessel for consignment"
    # request messgae
    vessel = consignment_pb2.Consignment(id = consignment_id, name = consignment_name, weight = consignment_weight)
    # make call
    vessel_response = stub.GetVesselForConsignment(vessel)
    # return response in JSON format rather than object
    return json_format.MessageToJson(vessel_response)