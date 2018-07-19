import grpc
import os
from concurrent import futures
import time
# import the generated classes
from proto import consignment_pb2
from proto import consignment_pb2_grpc
# import the original consignment.py
import consignment
# create a class to define the server functions, derived from
# consignment_pb2_grpc.ShippingServicer
class ShippingServicer(consignment_pb2_grpc.ShippingServicer):
    # service to get consignments
    
    # service to get consignments
    def GetConsignment(self, request, context):
        create_log('Getting Consignment')
        consignmentResponse = consignment.get_consignment(request.consignment_id)
        # making response message
        response = consignment_pb2.Consignment()
        response.id = consignmentResponse['id']
        response.name = consignmentResponse['name']
        response.weight = consignmentResponse['weight']
        return response
    
    # service to get vessels
    def GetVesselForConsignment(self, request, context):
        create_log('Getting Vessel for consignment')
        # making proper response message
        response = consignment_pb2.ConsignmentVessel()
        vessel = consignment.get_vessel_for_consignment(request)
        response.id = vessel.id
        response.max_weight = vessel.max_weight
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
consignment_pb2_grpc.add_ShippingServicer_to_server(ShippingServicer(), server)

###--------
with open(os.path.join(os.path.split(__file__)[0], 'tls.key')) as f:
    private_key = f.read().encode()
with open(os.path.join(os.path.split(__file__)[0], 'tls.crt')) as f:
    certificate_chain = f.read().encode()
###-------


# listen on port 50051
print('Starting server. Listening on port 50051.')

###-------
# create server credentials
server_creds = grpc.ssl_server_credentials(((private_key, certificate_chain,),))
#server.add_secure_port('localhost:50051', server_creds)
server.add_secure_port('[::]:50051', server_creds)
###-------

#server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
