# main.py
Using the python flask library - create an implementation that uses http rest endpoints for this service

import and use Package from the data_model.py and the SessionMaker from connect_conector.py for packages data.

import and use Package from the data_model.py and the SessionMaker from connect_conector.py for packages data. Use host IP 0.0.0.0 and port 8000 for app.run

Create endpoint that retrieves package details based on the provided product ID.

# API spec
Generate an OpenAPI yaml specification for a service that provides shipping and package information given a numerical product id. The service should include information about the packages height, width, depth, weight and any special handling instructions.

# ops
Generate a Dockerfile for this application.

How do I create a GKE cluster?

How do I create a GKE cluster in in us-central1 region in a project called duet01 using gcloud?

How do I locally run a container using this Dockerfile

How do I build and push docker images to an artifact registry?

Generate a kubernetes deployment and service spec for a service called shipping for a container in artifact registry

gcloud projects remove-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:sqlgsa@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role="roles/cloudsql.admin"

gcloud projects add-iam-policy-binding ${PROJECT_ID} \
    --member="serviceAccount:sqlgsa@${PROJECT_ID}.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"

# Post a package to the DB
curl -X POST -H "Content-Type: application/json" -d '{"height": 10, "width": 10, "depth": 10, "weight": 10, "special_handling_instructions": "Handle with care"}' http://localhost:8080/packages/12345

curl -X POST \
  http://localhost:8080/packages/123 \
  -H "Content-Type: application/json" \
  -d '{"height": 10, "width": 12, "depth": 8, "weight": 5, "special_handling_instructions": "Handle with care"}'


  curl -X POST \
  http://localhost:8080/packages/123456 \
  -H 'Content-Type: application/json' \
  -d '{"height": 10, "width": 12, "depth": 8, "weight": 5, "special_handling_instructions": "Handle with care"}'


  curl -X POST http://localhost:8080/packages/240516001 \
-H "Content-Type: application/json" \
-d '{"height": 10, "width": 20, "depth": 30, "weight": 5, "special_handling_instructions": "Handle with care"}'

curl -X POST \
  http://localhost:5000/packages/999 \
  -H "Content-Type: application/json" \
  -d '{"height": 10, "width": 20, "depth": 30, "weight": 5, "special_handling_instructions": "Handle with care"}'


## Add and Delete
### first add
curl -X POST \
  http://localhost:5000/packages/24052201 \
  -H "Content-Type: application/json" \
  -d '{"height": 10, "width": 12, "depth": 8, "weight": 5, "special_handling_instructions": "Handle with care"}'

### then get
curl http://localhost:5000/packages/24052201 -s | jq

### then delete
curl -X DELETE http://localhost:5000/packages/24052201

### then get again
curl http://localhost:5000/packages/24052201 -s | jq


## Add, Update and Delete
### first add
curl -X POST \
  http://localhost:5000/packages/24052201 \
  -H "Content-Type: application/json" \
  -d '{"height": 10, "width": 12, "depth": 8, "weight": 5, "special_handling_instructions": "Fragile"}'

### then get
curl http://localhost:5000/packages/24052201 -s | jq

### then update
curl -X PUT \
  http://localhost:5000/packages/24052201 \
  -H "Content-Type: application/json" \
  -d '{"height": 15, "width": 10, "special_handling_instructions": "UPDATED! AntiFragile!"}'

### then get again after update
curl http://localhost:5000/packages/24052201 -s | jq


### then delete
curl -X DELETE http://localhost:5000/packages/12345

### then get again
curl http://localhost:5000/packages/12345 -s | jq



## Valeo demo
curl -X POST -H "Content-Type: application/json" -d '{ "product_id": "12345", "height": 10, "width": 5, "depth": 3, "weight": 2.5, "special_handling_instructions": "Fragile - Handle with care"}' http://localhost:8080/packages



curl -X POST -H "Content-Type: application/json" -d '{"product_id": 1234321, "height": 10, "width": 5, "depth": 3, "weight": 2.5, "special_handling_instructions": "Fragile, handle with care"}' http://localhost:8080/packages


curl -X POST -H "Content-Type: application/json" -d '{"product_id": "123", "height": "10.5", "width": "15.2", "depth": "8.7", "weight": "2.5", "special_handling_instructions": "Handle with care"}' http://localhost:8000/packages
