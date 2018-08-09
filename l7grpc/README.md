
# SETUP:

gcloud container  clusters create cluster-grpc --machine-type "n1-standard-1" --cluster-version=1.10.5 --zone us-central1-a  --num-nodes 4

gcloud container clusters get-credentials cluster-grpc --zone us-central1-a

kubectl apply -f fe-deployment.yaml  -f fe-ingress.yaml -f fe-secret.yaml  -f fe-srv-ingress.yaml -f fe-srv-lb.yaml


----------------------------------------------

# DEPLOY

kubectl get po,deployment,svc,ing

NAME                                READY     STATUS    RESTARTS   AGE
po/fe-deployment-86f75cbf8c-5z8bz   1/1       Running   0          3m
po/fe-deployment-86f75cbf8c-bh5hk   1/1       Running   0          3m
po/fe-deployment-86f75cbf8c-qlp67   1/1       Running   0          3m
po/fe-deployment-86f75cbf8c-tbr9m   1/1       Running   0          3m

NAME                   DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deploy/fe-deployment   4         4         4            4           3m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)                        AGE
svc/fe-srv-ingress   NodePort       10.23.255.193   <none>         443:30611/TCP,8081:30847/TCP   3m
svc/fe-srv-lb        LoadBalancer   10.23.244.154   35.188.81.16   443:31531/TCP,8081:30295/TCP   3m
svc/kubernetes       ClusterIP      10.23.240.1     <none>         443/TCP                        5m

NAME             HOSTS     ADDRESS         PORTS     AGE
ing/fe-ingress   *         35.241.11.172   80, 443   3m

------------------------



## LoadBalancer
================

docker run --add-host main.esodemoapp2.com:35.188.81.16 -t salrashid123/grpcserver /grpc_client --host main.esodemoapp2.com:443
2018/07/29 17:11:58 RPC Response: 0 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:11:59 RPC Response: 1 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:00 RPC Response: 2 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:01 RPC Response: 3 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:02 RPC Response: 4 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:03 RPC Response: 5 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:04 RPC Response: 6 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:05 RPC Response: 7 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:06 RPC Response: 8 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67" 
2018/07/29 17:12:07 RPC Response: 9 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67"

docker run --add-host main.esodemoapp2.com:35.188.81.16 -t salrashid123/grpcserver /grpc_client --host main.esodemoapp2.com:443
2018/07/29 17:23:20 RPC Response: 0 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:21 RPC Response: 1 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:22 RPC Response: 2 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:23 RPC Response: 3 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:24 RPC Response: 4 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:25 RPC Response: 5 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:26 RPC Response: 6 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:27 RPC Response: 7 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:28 RPC Response: 8 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:23:29 RPC Response: 9 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m"

## Ingress

docker run --add-host main.esodemoapp2.com:35.241.11.172 -t salrashid123/grpcserver /grpc_client --host main.esodemoapp2.com:443
2018/07/29 17:18:48 RPC Response: 0 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-bh5hk" 
2018/07/29 17:18:49 RPC Response: 1 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-5z8bz" 
2018/07/29 17:18:50 RPC Response: 2 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-5z8bz" 
2018/07/29 17:18:51 RPC Response: 3 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:18:52 RPC Response: 4 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:18:53 RPC Response: 5 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-5z8bz" 
2018/07/29 17:18:55 RPC Response: 6 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-5z8bz" 
2018/07/29 17:18:56 RPC Response: 7 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-bh5hk" 
2018/07/29 17:18:57 RPC Response: 8 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-tbr9m" 
2018/07/29 17:18:58 RPC Response: 9 message:"Hello unary RPC msg   from hostname fe-deployment-86f75cbf8c-qlp67"
 
