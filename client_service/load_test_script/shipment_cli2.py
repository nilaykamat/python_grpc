## This is a test script for shipment service cli.
## --------------------------------------------
import grpc
from google.protobuf import json_format
# import the generated classes
from shipment_protos import shipment_pb2
from shipment_protos import shipment_pb2_grpc
# open a gRPC channel

###--------

with open('certs/tls.crt') as f:
     trusted_certs = f.read().encode()
# create credentials
credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)
#channel = grpc.secure_channel('localhost:50051', credentials)
channel = grpc.secure_channel('delivery.gship.com:443', credentials)

###--------

#channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = shipment_pb2_grpc.ShipmentStub(channel)

# function to get shipment
def get_shipment(shipment_id):
    # create a valid request message
    shipment = shipment_pb2.GetShipmentRequest(shipment_id = shipment_id)
    # make the call
    response = stub.GetShipment(shipment)
    # return response in JSON format rather than object
    return json_format.MessageToJson(response)

# function to get carrier for shipment
def get_carrier(shipment_id, shipment_name, shipment_weight):
    print "getting carrier for shipment"
    # request messgae
    carrier = shipment_pb2.ShipmentItem(id = shipment_id, name = shipment_name, weight = shipment_weight)
    # make call
    carrier_response = stub.GetCarrierForShipment(carrier)
    # return response in JSON format rather than object
    return json_format.MessageToJson(carrier_response)

#print get_carrier(1,'sample',200)
print get_shipment(1)
