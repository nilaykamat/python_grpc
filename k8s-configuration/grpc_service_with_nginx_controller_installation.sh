#!/bin/bash 

RED='\033[0;31m'
NC='\033[0m'

read -p "Enter USER_ACCOUNT ( USER_ACCOUNT is the user's email address) : " USER_ACCOUNT 

echo -e "${RED}Prerequisites for using Role-Based Access Control ${NC}"

echo -e "${RED}kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user [USER_ACCOUNT] ${NC}"

kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $USER_ACCOUNT 

echo -e "${RED}Setting up namespaces ${NC}"

kubectl create -f nginx-controller/namespace.yaml 

echo -e "${RED}Setting up Role-Based Access Control (RBAC) ${NC}"

kubectl create -f nginx-controller/RBAC.yaml 

echo -e "${RED}Setting up ConfigMap ${NC}"

kubectl create -f nginx-controller/config_map.yaml 

echo -e "${RED}Setting up TLS/SSL ${NC}"

kubectl create secret tls shippy-secret --key nginx-controller/tls.key --cert nginx-controller/tls.crt --namespace=shippy-grpc

sleep 5

echo -e "${RED}Setting up default backend ${NC}"

kubectl create -f nginx-controller/default_http_backend.yaml

echo -e "${RED}Setting up nginx-ingress-controller ${NC}"

kubectl create -f nginx-controller/nginx_ingress_controller.yaml

echo -e "${RED}Setting up nginx-ingress-rules for REST and for gRPC ${NC}"

kubectl create -f nginx-controller/nginx_ingress_REST_rules.yaml

kubectl create -f nginx-controller/nginx_ingress_gRPC_rules.yaml
 
echo -e "${RED}Setting up vessel-service ${NC}"

#kubectl create -f vessel-service/vessel_servicec.yaml
kubectl create -f vessel-service/vessel_servicec_test.yaml

echo -e "${RED}Setting up consignment-service ${NC}"

#kubectl create -f consignment-service/consignment_service.yaml
kubectl create -f consignment-service/consignment_service_test.yaml

echo -e "${RED}Setting up client-service ${NC}"

#kubectl create -f client-service/client_service.yaml
kubectl create -f client-service/client_service_test.yaml

sleep 5

echo -e "${RED}Getting pods,svc,ing,endpoints ${NC}" 

kubectl get pods,svc,ing,endpoints -o wide --all-namespaces

echo -e "${RED}Get IP Address from 'kubectl get ing -o wide --all-namespaces' command and make entry in local hosts file to resolve domain name ${NC}"

echo -e "${RED} Access https://shippy.example.com/ui ${NC}"

