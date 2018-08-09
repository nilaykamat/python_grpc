gcloud container clusters create neg-grpc \
  --cluster-version=1.10.5 \
  --enable-ip-alias \
  --create-subnetwork="" \
  --network=default \
  --zone=us-east1-d \
  --disk-type "pd-standard" \
  --disk-size "30"

