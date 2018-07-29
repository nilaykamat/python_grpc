import grpc
import os
from concurrent import futures
import time
# import the generated classes
from proto import carrier_pb2
from proto import carrier_pb2_grpc
# import the original carrier.py
import carrier
# create a class to define the server functions, derived from
# carrier_pb2_grpc.carrierServicer
class CarrierServicer(carrier_pb2_grpc.CarrierServicer):
    # service endpoint to get carriers
    def GetCarrier(self, request, context):
        create_log('Getting Carriers')
        carrierResponse = carrier.get_carrier(request.weight)
        
        response = carrier_pb2.CarrierItem()
        response.id = carrierResponse['id']
        response.max_weight = carrierResponse['max_weight']
        return response
# function to create access logs
def create_log(comment):
    f = open("log","a")
    f.write(str(comment) + "\n")
    f.close()
    
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
# use the generated function `add_carrierServicer_to_server`
# to add the defined class to the server
carrier_pb2_grpc.add_CarrierServicer_to_server(CarrierServicer(), server)


###--------
with open(os.path.join(os.path.split(__file__)[0], 'certs/tls.key')) as f:
     private_key = f.read().encode()
with open(os.path.join(os.path.split(__file__)[0], 'certs/tls.crt')) as f:
     certificate_chain = f.read().encode()
###-------

# listen on port 50052
print('Starting server. Listening on port 50052.')

###-------
# create server credentials
server_creds = grpc.ssl_server_credentials(((private_key, certificate_chain,),))
#server.add_secure_port('localhost:50052', server_creds)
server.add_secure_port('[::]:50052', server_creds)
###-------

#server.add_insecure_port('localhost:50052')
#server.add_insecure_port('[::]:50052')
server.start()
# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
