echo 'starting http server on port 9000'
python -m SimpleHTTPServer 9000 >> /dev/null &
echo 'starting gRPC server on port 50051'
python server.py
