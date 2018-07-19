#!/bin/bash 

RED='\033[0;31m'
NC='\033[0m'
echo -e "${RED} ------------------------------------------------------------------------------------------------------------- ${NC}"
echo -e "${RED} Before executing the script read https://github.com/kubernetes/ingress-gce/tree/master/deploy/glbc carefully. ${NC}"
echo -e "${RED} This script is calling exisitng scipt present in glbc-controller/script.sh path. ${NC}"
echo -e "${RED} Before executing this script manually edit the glbc-controller/gce.conf file. ${NC}"
echo -e "${RED} Run this scipt in a newly created cluster. ${NC}"
echo -e "${RED} ------------------------------------------------------------------------------------------------------------- ${NC}"

while true; do
	echo -e "${RED}Press [Y | y] to continue.${NC}" 
        read input
        case $input in
        [Yy]* ) break;;
        * ) exit 1
        esac
done 

read -p " Enter name of the cluster : " cluster_name
read -p " Enter zone of the cluster : " cluster_zone
read -p " Enter USER_ACCOUNT ( USER_ACCOUNT is the user's email address) : " USER_ACCOUNT 

echo -e "${RED}Prerequisites for using Role-Based Access Control ${NC}"

echo -e "${RED}kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user [USER_ACCOUNT] ${NC}"

kubectl create clusterrolebinding cluster-admin-binding --clusterrole cluster-admin --user $USER_ACCOUNT

sleep 3


cd glbc-controller && bash script.sh -n $cluster_name -z $cluster_zone
[[ $? -eq 0 ]] || echo -e "${RED} Delete the exisitng role and service account by manually executing script 'bash glbc-controller/script.sh -n myCluster -z myZone -c' and re-run this script ${NC}" && exit 1


cd ~/python_grpc/k8s-configuration/

sleep 5

echo -e "${RED}Setting up namespaces ${NC}"

kubectl create -f glbc-controller/namespace.yaml 

echo -e "${RED}Setting up TLS/SSL ${NC}"

kubectl create secret tls shippy-secret --key glbc-controller/tls.key --cert glbc-controller/tls.crt --namespace=shippy-grpc

echo -e "${RED}Setting up glbc-ingress-rules ${NC}"

kubectl create -f glbc-controller/glbc_ingress_rules.yml 

echo -e "${RED}Setting up vessel-service ${NC}"

kubectl create -f vessel-service/vessel_servicec.yaml

echo -e "${RED}Setting up consignment-service ${NC}"

kubectl create -f consignment-service/consignment_service.yaml

echo -e "${RED}Setting up client-service ${NC}"

kubectl create -f client-service/client_service.yaml

sleep 5

echo -e "${RED}Getting pods,svc,ing,endpoints ${NC}" 

kubectl get pods,svc,ing,endpoints -o wide --all-namespaces 

echo -e "${RED}Get IP Address from 'kubectl get ing -o wide --all-namespaces' command and make entry in local hosts file to resolve domain name ${NC}"
echo -e "${RED}Wait for sometime to create Loadbalancer and then access https://shippy.example.com/ui ${NC}"
