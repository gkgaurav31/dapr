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
