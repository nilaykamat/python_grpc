
import grpc
from protos import article_pb2
from protos import article_pb2_grpc

global users
users = [
    {
        'id' : 1,
        'name' : 'john doe',
        'email' : 'john_doe@gmail.com'
    },
    {
        'id' : 2,
        'name' : 'Jane doe',
        'email' : 'jane_doe@gmail.com'
    }
]

def get_user(user):
    return users[0]['name']

def create_user(user):
    return users[0]['name']

def get_article(user_id):
    print user_id
    print 'inside article'
    
    # open a gRPC channel
    channel = grpc.insecure_channel('localhost:50052')

    # create a stub (client)
    stub = article_pb2_grpc.ArticleStub(channel)

    # create a valid request message
    user = article_pb2.UserId(id=user_id)

    # make the call
    response = stub.GetArticle(user)
    print response.article

    return response.article