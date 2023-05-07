# STATEFUL APPLICATION USING DAPR

[How-To: Save and get state](https://docs.dapr.io/developing-applications/building-blocks/state-management/howto-get-save-state/)

## COMMANDS

```bash
dapr run --app-id hello-dapr --app-port 5000 --dapr-http-port 8089 flask run
```

## TEST

```bash
curl http://localhost:8089/v1.0/invoke/hello-dapr/method/greeting
Greetings! You are visitor number 1.
```

## EXPLANATION

When you run the dapr init command, the Dapr CLI automatically creates the components folder with a default Redis state store configuration and a Redis messaging backbone configuration.  

For example, the following is the default redis.yaml configuration file the Dapr CLI generates:

```yaml
apiVersion: dapr.io/v1alpha1
kind: Component 
metadata:
    name: statestore 
spec:
    type: state.redis 
    metadata:
    - name: redisHost 
      value: localhost:6379 
    - name: redisPassword 
      value: ""
```

### GET THE CURRENT VALUE OF COUNT FROM STATESTORE

If the value is empty, set it to 1.

```python
count_url = "http://localhost:8089/v1.0/state/statestore/mystate"
count_response = requests.get(count_url)
count = count_response.text
```

### UPDATE THE VALUE OF COUNT TO STATESTORE

```python
import json
import requests

stateObj = [{"Key": "mystate", "Value": count}]
stateData = json.dumps(stateObj).encode("utf-8")
headers = {"Content-Type": "application/json"}
resp = requests.post("http://localhost:8089/v1.0/state/statestore", data=stateData, headers=headers)
```

### CHECK VALUES IN REDIS CONTAINER

```bash
docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED        STATUS                       PORTS                              NAMES
9473f383aa08   openzipkin/zipkin   "start-zipkin"           9 months ago   Up About an hour (healthy)   9410/tcp, 0.0.0.0:9411->9411/tcp   dapr_zipkin
42e835fc616a   daprio/dapr:1.8.3   "./placement"            9 months ago   Up About an hour             0.0.0.0:6050->50005/tcp            dapr_placement
d84a0c57285f   redis               "docker-entrypoint.s…"   9 months ago   Up About an hour             0.0.0.0:6379->6379/tcp             dapr_redis

docker exec -it dapr_redis redis-cli
127.0.0.1:6379> KEYS *
1) "hello-dapr||order_1"
2) "Sagerampant-Stone||color"
3) "hello-dapr||mystate"
127.0.0.1:6379> HGETALL hello-dapr||mystate
1) "data"
2) "27"
3) "version"
4) "27"
```
