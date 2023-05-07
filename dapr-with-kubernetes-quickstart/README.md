# Hello, World! with Dapr Kubernetes Mode

## CREATE AND CONNECT TO THE AKS CLUSTER

[Setup an Azure Kubernetes Service (AKS) cluster](https://docs.dapr.io/operations/hosting/kubernetes/cluster/setup-aks/)

```bash
az aks get-credentials -n [your_aks_cluster_name] -g [your_resource_group]
```

## BOOTSTRAP

```bash
dapr init --kubernetes

Making the jump to hyperspace...
Note: To install Dapr using Helm, see here: https://docs.dapr.io/getting-started/install-dapr-kubernetes/#install-with-helm-advanced

Container images will be pulled from Docker Hub
Deploying the Dapr control plane to your cluster...
Success! Dapr has been installed to namespace dapr-system. To verify, run `dapr status -k' in your terminal. To get started, go here: https://aka.ms/dapr-getting-started
```

> Helm Chart Deploys the Dapr pods under the dapr-system namespace

```bash
kubectl get pods -n dapr-system
NAME                                     READY   STATUS    RESTARTS   AGE
dapr-dashboard-57f5f47775-kpcw9          1/1     Running   0          54s
dapr-operator-5bbd5bddd4-wtsmz           1/1     Running   0          54s
dapr-placement-server-0                  1/1     Running   0          53s
dapr-sentry-598fbc67f4-fz4jm             1/1     Running   0          54s
dapr-sidecar-injector-686f6647d5-vppvq   1/1     Running   0          54s
```

## TEST THE RECEIVER APP

```bash
docker build -t <username>/node_receiver .
docker run --rm -p 8088:8088 <username>/node_receiver
docker push <username>/node_receiver
```

### SEND A POST REQUEST

```bash
curl --location 'http://localhost:8088/greeting' \
--header 'Content-Type: application/json' \
--data '{
"msg": "Hello, World!" }'
```

### Output

```plaintext
Receiver is running on port 8088
{ msg: 'Hello, World!' }
```

Similarly, you could test the Python Sender App.

### Create Deployment in K8S

```bash
kubectl apply -f ./app.yaml
deployment.apps/nodereceiver created
deployment.apps/pythonsender created
```

> If you get the error:
> Error creating: admission webhook "sidecar-injector.dapr.io" denied the request: value for the dapr.io/app-id annotation is empty
> Check if the annotation "dapr.io/app-id" has been added in the Deployment YAML.

```bash
kubectl get deployments
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
nodereceiver   1/1     1            1           14m
pythonsender   1/1     1            1           14m
```
