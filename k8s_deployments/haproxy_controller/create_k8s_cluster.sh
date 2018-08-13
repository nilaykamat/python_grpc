#!/bin/bash 
## Create a k8s cluster 
## --------------------

RED='\033[0;31m'
NC='\033[0m'

read -p "Enter Project name: " project_name
read -p "Enter Cluster name: " cluster_name
read -p "Enter Zone : " zone

gcloud beta container --project "$project_name" clusters create "$cluster_name" --zone "$zone" --username "admin" --cluster-version "1.10.5-gke.4" --machine-type "n1-standard-1" --image-type "COS" --disk-type "pd-standard" --disk-size "50" --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --num-nodes "3" --enable-stackdriver-kubernetes --network "projects/pso-suchit/global/networks/default" --subnetwork "projects/pso-suchit/regions/us-east1/subnetworks/default" --enable-autoscaling --min-nodes "3" --max-nodes "6" --addons HorizontalPodAutoscaling,HttpLoadBalancing,KubernetesDashboard --no-enable-autoupgrade --enable-autorepair 

## Login in to cluster 

while true; do
	echo -e "${RED}Do you want to log into the $cluster_name\?${NC}"
	echo -e "${RED}Press [Y | y] to continue.${NC}" 
        read input
        case $input in
        [Yy]* ) gcloud container clusters get-credentials $cluster_name --zone $zone --project $project_name && echo -e "${RED}Successfully Logged into $cluster_name Cluster${NC}" && break;;
        * ) exit 1
        esac
done 

