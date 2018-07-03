import grpc

# import the generated classes
from protos import user_pb2
from protos import user_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = user_pb2_grpc.UserServiceStub(channel)

# create a valid request message
user = user_pb2.GetRequest()
userdata = user_pb2.User(id=3, name='nilay', email='nilay@gmail.com')
articleData = user_pb2.ArticleRequest(user_id=2)

# make the call
response1 = stub.GetUser(user)
response2 = stub.CreateUser(userdata)
response3 = stub.GetUserArticle(articleData)

print response1
print response2
print response3