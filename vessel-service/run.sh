echo 'starting http server on port 9000'
./http2-test >> go.logs & 
echo 'starting gRPC server on port 443'
python server.py
