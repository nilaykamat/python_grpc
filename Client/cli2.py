import grpc

    # import the generated classes
from protos import article_pb2
from protos import article_pb2_grpc

channel = grpc.insecure_channel('35.226.146.110:50052')

# create a stub (client)
stub = article_pb2_grpc.ArticleStub(channel)

# create a valid request message
user = article_pb2.UserId(id=1)

# make the call
response1 = stub.GetArticle(user)
print response1
