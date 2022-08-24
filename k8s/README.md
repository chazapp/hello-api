# Hello-API Kubernetes Deployment
This directory contains the Kustomize deployment of the Hello-API on
Chaz's Kubernetes Cluster.

## Usage
Provide `secrets.yml` file and apply it to the cluster:

```
---
kind: Secret
metadata:
    name: hello-secret
type: Opaque
stringData:
    DB_USER: ...
    DB_PASSWORD: ...
    DB_NAME: ...
    DB_URI: ...
```  
  
Provide a PV and PVC to be mounted by the Postgres Pod. 

Provide the Ingress DNS Records.

Apply this Kustomize directory to your cluster:

```
$ kubectl apply -k k8s/
```  
  
An `Application` ArgoCD CRD is available to automate the deployment procedure.
