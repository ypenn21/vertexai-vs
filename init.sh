
#1. pull source code from git repo: https://github.com/rick-c-goog/sbcrudapp
git clone https://github.com/rick-c-goog/sbcrudapp

#2. run terraform init again terraform directory to create the infrastructure
cd terraform
terraform init

#3. run terraform apply to create the infrastructure
terraform apply

#4. change directory to src directory, run command to build image and store to artifactory registry
cd src
docker build -t gcr.io/my-project/sbcrudapp .
docker push gcr.io/my-project/sbcrudapp

#5. run cloud deploy command deploy the image to cloud run service
gcloud run deploy sbcrudapp --image gcr.io/my-project/sbcrudapp

#
EOF
#write bash scripts with the following commands:
#1. pull source code from git repo: https://github.com/rick-c-goog/sbcrudapp
#2. run terraform init again terraform directory to create the infrastructure
#3. run terraform apply to create the infrastructure
#4. change directory to src directory, run command to build image and store to artifactory registry
#5. run cloud deploy command deploy the image to cloud run service

#