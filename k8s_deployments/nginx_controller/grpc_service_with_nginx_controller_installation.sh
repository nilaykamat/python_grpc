#!/bin/bash 

## --------------------------------------------------------------------------
## This script will configure Nginx Controller and deploy gRPC microservices.
## Create a new Clutser and login into the Cluster before running this script.
## You can use create_k8s_cluster.sh script in this repo to create a k8s cluster.
## --------------------------------------------------------------------------

RED='\033[0;31m'
NC='\033[0m'

echo -e "${RED}Prerequisites for using Role-Based Access Control ${NC}"

kubectl create clusterrolebinding cluster-admin-binding  --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

echo -e "${RED}Setting up namespaces ${NC}"

kubectl apply -f namespace.yaml 

echo -e "${RED}Setting up Role-Based Access Control (RBAC) ${NC}"

kubectl apply -f rbac.yaml 

echo -e "${RED}Setting up ConfigMap ${NC}"

kubectl apply -f config_map.yaml 

echo -e "${RED}Setting up TLS/SSL ${NC}"

kubectl create secret tls delivery-secret --key ../certs/tls.key --cert ../certs/tls.crt --namespace=kube-system

sleep 5

echo -e "${RED}Setting up default backend ${NC}"

kubectl apply -f default_http_backend.yaml

echo -e "${RED}Setting up nginx-ingress-controller ${NC}"

kubectl apply -f nginx_ingress_controller.yaml

echo -e "${RED}Setting up nginx-ingress-rules for REST and for gRPC ${NC}"

kubectl apply -f nginx_ingress_REST_rules.yaml

kubectl apply -f nginx_ingress_gRPC_rules.yaml
 
echo -e "${RED}Setting up carrier_service ${NC}"

kubectl apply -f ../carrier_service/carrier_service.yaml

echo -e "${RED}Setting up shipment-service ${NC}"

kubectl apply -f ../shipment_service/shipment_service.yaml

echo -e "${RED}Setting up client-service ${NC}"

kubectl apply -f ../client_service/client_service.yaml

echo -e "${RED}Setting up autoscaling for client-service ${NC}"

kubectl apply -f ../autoscaling/hpa_client.yaml

echo -e "${RED}Setting up autoscaling for carrier-service ${NC}"

kubectl apply -f ../autoscaling/hpa_carrier.yaml

echo -e "${RED}Setting up autoscaling for shipment-service ${NC}"

kubectl apply -f ../autoscaling/hpa_shipment.yaml

sleep 5

echo -e "${RED}Getting pods,svc,ing,endpoints,hpa ${NC}" 

kubectl get pods,svc,ing,endpoints,hpa -o wide --all-namespaces

echo -e "${RED}Get IP Address from 'kubectl get ing -o wide --all-namespaces' command and make entry in local hosts file to resolve domain name ${NC}"

echo -e "${RED}Access https://delivery.gship.com/ui ${NC}"
