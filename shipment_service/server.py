import grpc
import os
from concurrent import futures
import time
# import the generated classes
from proto import shipment_pb2
from proto import shipment_pb2_grpc
# import the original shipment.py
import shipment
# create a class to define the server functions, derived from
# shipment_pb2_grpc.ShipmentServicer
class ShipmentServicer(shipment_pb2_grpc.ShipmentServicer):
    
    # service to get shipments
    def GetShipment(self, request, context):
        create_log('Getting Shipment')
        shipmentResponse = shipment.get_shipment(request.shipment_id)
        # making response message
        response = shipment_pb2.ShipmentItem()
        response.id = shipmentResponse['id']
        response.name = shipmentResponse['name']
        response.weight = shipmentResponse['weight']
        return response
    
    # service to get carrier
    def GetCarrierForShipment(self, request, context):
        create_log('Getting Carrier for Shipment')
        # making proper response message
        response = shipment_pb2.ShipmentCarrier()
        carrier = shipment.get_carrier_for_shipment(request)
        response.id = carrier.id
        response.max_weight = carrier.max_weight
        return response
    
# creating logs for each access
def create_log(comment):
    f = open("log","a")
    f.write(str(comment) + "\n")
    f.close()
    

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_ShippingServicer_to_server`
# to add the defined class to the server
shipment_pb2_grpc.add_ShipmentServicer_to_server(ShipmentServicer(), server)

###--------
# with open(os.path.join(os.path.split(__file__)[0], 'tls.key')) as f:
#     private_key = f.read().encode()
# with open(os.path.join(os.path.split(__file__)[0], 'tls.crt')) as f:
#     certificate_chain = f.read().encode()
###-------


# listen on port 50051
print('Starting server. Listening on port 50051.')

###-------
# create server credentials
# server_creds = grpc.ssl_server_credentials(((private_key, certificate_chain,),))
#server.add_secure_port('localhost:50051', server_creds)
#server.add_secure_port('[::]:50051', server_creds)
###-------

server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
