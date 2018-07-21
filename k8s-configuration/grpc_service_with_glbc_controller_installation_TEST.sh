#!/bin/bash 

RED='\033[0;31m'
NC='\033[0m'

cd ~/python_grpc/k8s-configuration/
sleep 5
echo -e "${RED}Setting up namespaces ${NC}"
kubectl create -f glbc-controller/namespace.yaml
echo -e "${RED}Setting up TLS/SSL ${NC}"
kubectl create secret tls shippy-secret --key glbc-controller/tls.key --cert glbc-controller/tls.crt --namespace=shippy-grpc
echo -e "${RED}Setting up glbc-ingress-rules ${NC}"
kubectl create -f glbc-controller/glbc_ingress_rules.yml
echo -e "${RED}Setting up vessel-service ${NC}"
#kubectl create -f vessel-service/vessel_servicec.yaml
kubectl create -f vessel-service/vessel_servicec_LB.yaml
echo -e "${RED}Setting up consignment-service ${NC}"
#kubectl create -f consignment-service/consignment_service.yaml
kubectl create -f consignment-service/consignment_service_LB.yaml
echo -e "${RED}Setting up client-service ${NC}"
#kubectl create -f client-service/client_service.yaml
kubectl create -f client-service/client_service_LB.yaml
sleep 5
echo -e "${RED}Getting pods,svc,ing,endpoints ${NC}" 
kubectl get pods,svc,ing,endpoints -o wide --all-namespaces
echo -e "${RED}Get IP Address from 'kubectl get ing -o wide --all-namespaces' command and make entry in local hosts file to resolve domain name ${NC}"
echo -e "${RED}Wait for sometime to create Loadbalancer and then access https://shippy.example.com/ui ${NC}"
