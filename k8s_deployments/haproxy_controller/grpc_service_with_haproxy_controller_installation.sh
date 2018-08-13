#!/bin/bash 

## ----------------------------------------------------------------------------
## This script will configure HAProxy Controller and deploy gRPC microservices.
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

echo -e "${RED}Prerequisites for using Role-Based Access Control ${NC}"

kubectl create clusterrolebinding cluster-admin-binding  --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

echo -e "${RED}Deploying namespaces ${NC}"

kubectl apply -f namespace.yaml 

echo -e "${RED}Deploying Role-Based Access Control (RBAC) ${NC}"

kubectl apply -f rbac.yaml 

echo -e "${RED}Deploying ConfigMap ${NC}"

kubectl apply -f config_map.yaml 

sleep 5

echo -e "${RED}Deploying default backend ${NC}"

kubectl apply -f default_http_backend.yaml

echo -e "${RED}Deploying haproxy-ingress-controller ${NC}"

kubectl apply -f haproxy_ingress_controller.yaml

echo -e "${RED}Deploying haproxy-ingress-rules ${NC}"

kubectl apply -f haproxy_ingress_rules_carrier.yaml 

echo -e "${RED}Deploying carrier_service ${NC}"

kubectl apply -f ../carrier_service/carrier_service.yaml

echo -e "${RED}Deploying autoscaling for carrier-service ${NC}"

kubectl apply -f ../autoscaling/hpa_carrier.yaml

sleep 5

echo -e "${RED}Getting pods,svc,ing,endpoints,hpa ${NC}" 

kubectl get pods,svc,ing,endpoints,hpa -o wide --all-namespaces
