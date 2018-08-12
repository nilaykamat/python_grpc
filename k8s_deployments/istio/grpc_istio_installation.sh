#!/bin/bash 

## --------------------------------------------------------------------------
## This script will configure istio and deploy gRPC microservices.
## Create a new Clutser and login into the Cluster before running this script.
## You can use create_k8s_cluster.sh script in this repo to create a k8s cluster. 
## --------------------------------------------------------------------------

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

ssl_copy() {
## Copy certificate and the private key to "/etc/istio/ingressgateway-certs", or the gateway will fail to load them. 
echo -e "${RED}For this sample we are terminating SSL Certificate at istio-gateway.${NC}"
echo -e "${RED}The location of the certificate and the private key MUST be /etc/istio/ingressgateway-certs, or the istio-gateway will fail to load them.${NC}"
while true; do
        echo -e "${RED}Do you want to copy certificate and the private key to /etc/istio/ingressgateway-certs\?${NC}"
        echo -e "${RED}Press [Y | y] to continue.${NC}"
        read input
        case $input in
        [Yy]* ) 
		mkdir -p /etc/istio/ingressgateway-certs/ 
		cp ../certs/tls.crt ../certs/tls.key  /etc/istio/ingressgateway-certs/ 
		if [[ $? == 0 ]] ; then
			echo -e "${RED}Copy done!!${NC}" 
		else
			echo -e "${RED}Copy error!! User need proper permissions to create dir and copy files to /etc/istio/ingressgateway-certs/.${NC}"
			echo -e "${RED}Give Proper permission to the user.${NC}" 
			exit 1
		fi
 		break;;
        * ) exit 1
        esac
done
}

check_cluster
ssl_copy

echo -e "${RED}Prerequisites for using Role-Based Access Control ${NC}"

echo -e "${RED}kubectl create clusterrolebinding cluster-admin-binding  --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)${NC}"
kubectl create clusterrolebinding cluster-admin-binding  --clusterrole=cluster-admin --user=$(gcloud config get-value core/account)

echo -e "${RED}Add the istioctl client to your PATH environment variable${NC}"

cd istio-1.0.0 && export PATH=$PWD/bin:$PATH 

echo -e "${RED}Installing Istio without mutual TLS authentication between sidecars${NC}"

kubectl apply -f install/kubernetes/istio-demo.yaml 

cd ..

echo -e "${RED}Creating kubernetes Secret ${NC}" 
if [[ ! -f "/etc/istio/ingressgateway-certs/tls.crt" && "/etc/istio/ingressgateway-certs/tls.key" ]] ; then 
	echo -e "${RED}NO Certificate and Private key found in /etc/istio/ingressgateway-certs/${NC}"  
	ssl_copy
	exit 1 
else 
kubectl create -n istio-system secret tls istio-ingressgateway-certs --key /etc/istio/ingressgateway-certs/tls.key --cert /etc/istio/ingressgateway-certs/tls.crt
fi 

exit 1
echo -e "${RED}Deploying istio gateway ${NC}"

kubectl apply -f istio/gtw.yaml

echo -e "${RED}Deploying Virtual Service  ${NC}"

kubectl apply -f istio/vs.yaml

echo -e "${RED}Deploying client-service ${NC}"

kubectl apply -f ../client_service/client_service.yaml 

echo -e "${RED}Enableing Istio-Sidecar-injector ${NC}"

kubectl label namespace istio-system istio-injection=enabled

echo -e "${RED}Deploying carrier_service ${NC}"

kubectl apply -f ../carrier_service/carrier_service.yaml

echo -e "${RED}Deploying shipment-service ${NC}"

kubectl apply -f ../shipment_service/shipment_service.yaml

echo -e "${RED}Deploying autoscaling for client-service ${NC}"

kubectl apply -f ../autoscaling/hpa_client.yaml

echo -e "${RED}Deploying autoscaling for carrier-service ${NC}"

kubectl apply -f ../autoscaling/hpa_carrier.yaml

echo -e "${RED}Deploying up autoscaling for shipment-service ${NC}"

kubectl apply -f ../autoscaling/hpa_shipment.yaml

sleep 5

echo -e "${RED}Getting pods,svc,ing,endpoints,hpa,gateway,VirtualService ${NC}" 

kubectl get pods,svc,ing,hpa,gateway,VirtualService -o wide --all-namespace

echo -e "${RED}Get IP Address from 'kubectl get svc istio-ingressgateway -n istio-system' command and make entry in local hosts file to resolve domain name ${NC}"
echo -e "${RED}Access https://delivery.gship.com/ui ${NC}" 
