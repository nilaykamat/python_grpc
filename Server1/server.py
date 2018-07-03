import grpc
from concurrent import futures
import time

# import the generated classes
from proto import user_pb2
from proto import user_pb2_grpc

# import the original user.py
import user

# create a class to define the server functions, derived from
# user_pb2_grpc.userServicer
class UserServiceServicer(user_pb2_grpc.UserServiceServicer):

    # user.square_root is exposed here
    # the request and response are of the data type
    # user_pb2.Number
    def GetUser(self, request, context):
	print('inside getUser')
        response = user_pb2.Response()
        response.success = True
        response.users = user.get_user(request)
        return response
    
    def CreateUser(self, request, context):
        print('inside createuser')
	response = user_pb2.Response()
        response.success = True
        response.users = user.create_user(request)
        return response
    
    def GetUserArticle(self, request, context):
	print('inside get user article')
        response = user_pb2.Response()
        response.success = True
        print request.user_id
        response.users = user.get_article(request.user_id)
        return response
    

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_userServicer_to_server`
# to add the defined class to the server
user_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
