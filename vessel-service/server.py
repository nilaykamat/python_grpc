import grpc
import os
from concurrent import futures
import time
# import the generated classes
from proto import vessel_pb2
from proto import vessel_pb2_grpc
# import the original vessel.py
import vessel
# create a class to define the server functions, derived from
# vessel_pb2_grpc.VesselServicer
class VesselServicer(vessel_pb2_grpc.VesselServicer):
    # service endpoint to get vessels
    def GetVessel(self, request, context):
        create_log('Getting Vessels')
        vesselResponse = vessel.get_vessel(request.weight)
        
        response = vessel_pb2.VesselItem()
        response.id = vesselResponse['id']
        response.max_weight = vesselResponse['max_weight']
        return response
# function to create access logs
def create_log(comment):
    f = open("log","a")
    f.write(str(comment) + "\n")
    f.close()
    
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
# use the generated function `add_VesselServicer_to_server`
# to add the defined class to the server
vessel_pb2_grpc.add_VesselServicer_to_server(VesselServicer(), server)

print('Starting server. Listening on port 50052.')
server.add_insecure_port('[::]:50052')
server.start()
# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
