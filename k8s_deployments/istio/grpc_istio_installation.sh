#!/bin/bash 

## --------------------------------------------------------------------------
## This script will configure istio and deploy gRPC microservices.
## --------------------------------------------------------------------------

RED='\033[0;31m'
NC='\033[0m'

echo -e "${RED}Prerequisites for using Role-Based Access Control ${NC}"

kubectl create clusterrolebinding cluster-admin-binding  --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

echo -e "${RED}Add the istioctl client to your PATH environment variable${NC}"

cd istio-1.0.0 && export PATH=$PWD/bin:$PATH 

echo -e "${RED}Installing Istio without mutual TLS authentication between sidecars${NC}"

kubectl apply -f install/kubernetes/istio-demo.yaml 

cd ..

echo -e "${RED}Setting up kubernetes Secret ${NC}" 

kubectl create -n istio-system secret tls istio-ingressgateway-certs --key /etc/istio/ingressgateway-certs/tls.key --cert /etc/istio/ingressgateway-certs/tls.crt

echo -e "${RED}Setting up istio gateway ${NC}"

kubectl apply -f istio/gtw.yaml

echo -e "${RED}Setting up Virtual Service  ${NC}"

kubectl apply -f istio/vs.yaml

echo -e "${RED}Setting up client-service ${NC}"

kubectl apply -f ../client_service/client_service.yaml 

echo -e "${RED}Enable Istio-Sidecar-injector ${NC}"

kubectl label namespace istio-system istio-injection=enabled

echo -e "${RED}Setting up carrier_service ${NC}"

kubectl apply -f ../carrier_service/carrier_service.yaml

echo -e "${RED}Setting up shipment-service ${NC}"

kubectl apply -f ../shipment_service/shipment_service.yaml

echo -e "${RED}Setting up autoscaling for client-service ${NC}"

kubectl apply -f ../autoscaling/hpa_client.yaml

echo -e "${RED}Setting up autoscaling for carrier-service ${NC}"

kubectl apply -f ../autoscaling/hpa_carrier.yaml

echo -e "${RED}Setting up autoscaling for shipment-service ${NC}"

kubectl apply -f ../autoscaling/hpa_shipment.yaml

sleep 5

echo -e "${RED}Getting pods,svc,ing,endpoints,hpa,gateway,VirtualService ${NC}" 

kubectl get pods,svc,ing,hpa,gateway,VirtualService -o wide --all-namespace

echo -e "${RED}Get IP Address from 'kubectl get svc istio-ingressgateway -n istio-system' command and make entry in local hosts file to resolve domain name ${NC}"
echo -e "${RED}Access https://delivery.gship.com/ui ${NC}" 
