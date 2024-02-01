# http-monitoring-system
this is a simple http monitoring system that monitors the status of a list of websites.

there are two ways to run the project, using docker or kubernetes.

## docker
to run the project using docker, you need to have docker installed on your machine and a .env file like .env_template that we provided.

then just run the following commands to start the project:
```bash
docker-compose build
docker-compose up
```
the SERVER_PORT in environment file is the port that the server will be running on, and the CLIENT_PORT is the port that the project will be running on.

## kubernetes
to run the project using kubernetes, you need to have kubectl and minikube installed on your computer and a .env file like the .env_template that we provided.

you can start you cluster with helm or manually.
### helm
go to the following directory:
```bash
cd kubernetes
```
and install cluster like following:
```bash
helm install http-monitor-1 http-monitor
```
you can uninstall the cluster with the following command:
```bash
helm uninstall http-monitor-1
```
### manually
go to the following directory:
```bash
cd kubernetes
```
and run following command:
```bash
 make run_kube
```

### port forwarding
in order to test the project APIs in kubernetes, you need to port forward the server pod to your local machine, you can do that by running the following command:
```bash
  kubectl port-forward <server-pod-name> <server-port>:<server-port>
```
example:
```bash
  kubectl port-forward services/http-monitoring-service 2030:2020
```
which forwards port 2020 in http-monitoring-service pod to port 2030 in your local machine.

#### note
this repository is an implementation of my cloud computing course project in university, and it may has some issues.

also the image has been pushed to a local docker registry, so you need to change the image name in the kubernetes deployment file and docker-compose to your own image name.
