import grpc
from google.protobuf import json_format
# import the generated classes
from consignment_protos import consignment_pb2
from consignment_protos import consignment_pb2_grpc

with open('tls.crt') as f:
    trusted_certs = f.read().encode()
# create credentials
credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
#channel = grpc.secure_channel('localhost:50051', credentials)
channel = grpc.secure_channel('shippy.example.com:443', credentials)
# open a gRPC channe

# create a stub (client)
stub = consignment_pb2_grpc.ShippingStub(channel)


# function to get vessels for consignment

def get_consignment(consignment_id):
    # create a valid request message
    consignment = consignment_pb2.GetConsignmentRequest(consignment_id = consignment_id)
    # make the call
    response = stub.GetConsignment(consignment)
    # return response in JSON format rather than object
    return json_format.MessageToJson(response)

def get_vessel(consignment_id, consignment_name, consignment_weight):
    print "getting vessel for consignment"
    # request messgae
    vessel = consignment_pb2.Consignment(id = consignment_id, name = consignment_name, weight = consignment_weight)
    # make call
    vessel_response = stub.GetVesselForConsignment(vessel)
    # return response in JSON format rather than object
    return json_format.MessageToJson(vessel_response)

#print get_vessel(1,'sample',200)
print get_consignment(1) 
