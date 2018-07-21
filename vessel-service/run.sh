echo 'starting http server on port 9000'
python -m SimpleHTTPServer 9000 >> /dev/null &
echo 'starting gRPC server on port 50052'
python server.py
