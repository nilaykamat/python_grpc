#!/bin/bash 

## ----------------------------------------------------------------------------
## This script will configure GLBC with NEG and deploy sample gRPC microservice.
## Create a new Clutser and login into the Cluster before running this script.
## You can use create_k8s_cluster.sh script in this repo to create a k8s cluster. 
## ----------------------------------------------------------------------------

RED='\033[0;31m'
NC='\033[0m'

check_cluster () {
	echo -e "${RED}Create a new Clutser and login into the Cluster before running this script.${NC}"
	echo -e "${RED}You can use create_k8s_cluster.sh script in this repo to create a k8s cluster.${NC}" 
	while true; do
    		echo -e "${GREEN}Press [C | c] to continue.${NC}"
		read input
    		case $input in
      		[Cc]* ) break;;
      		* ) exit 1 
    		esac
  	done
}

check_cluster

echo -e "${RED}$Setting up sercert{NC}"
kubectl apply -f fe-secret.yaml

echo -e "${RED}$Setting up grpc sample service Deployment object {NC}"
kubectl apply -f fe-deployment.yaml

echo -e "${RED}$Setting up grpc sample service Service Object{NC}"
kubectl apply -f fe-srv-ingress.yaml

echo -e "${RED}$Enabling NEGs for HTTP(S) Loadbalancer{NC}"
kubectl annotate service fe-srv-ingress cloud.google.com/neg='{"ingress": true}'

echo -e "${RED}$Setting up Ingress{NC}" 
kubectl apply -f fe-ingress.yaml 

echo -e "${RED}$Setting up LB Service Object{NC}" 
kubectl apply -f fe-srv-lb.yaml

echo -e "${RED}Getting pods,svc,ing,endpoints,hpa ${NC}" 
kubectl get pods,svc,ing,endpoints,hpa -o wide --all-namespaces
