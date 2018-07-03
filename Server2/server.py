import grpc
from concurrent import futures
import time

# import the generated classes
from proto import article_pb2
from proto import article_pb2_grpc

# import the original article.py
import article

# create a class to define the server functions, derived from
class ArticleServicer(article_pb2_grpc.ArticleServicer):

    def GetArticle(self, request, context):
        create_log('inside getRaticle')
        response = article_pb2.ArticlesResponse()
        response.article = article.get_article(request.id)
        return response
        
def create_log(comment):
    f = open("log","a")
    f.write(str(comment) + "\n")
    f.close()
# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_ArticleServicer_to_server`
# to add the defined class to the server
article_pb2_grpc.add_ArticleServicer_to_server(ArticleServicer(), server)

# listen on port 50052 -since bothe are running on same environmanet and 50051 is already taken by server1
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