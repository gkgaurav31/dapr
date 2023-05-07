# HELLO WORLD DAPR

This is a quickstart sample for using Dapr in Standalone Mode.

## COMMANDS

```bash
pip install -r requirements.txt

dapr run --app-id hello-dapr --app-port 5000 --dapr-http-port 8089 flask run
```

## DAPR RUN

```bash
dapr run --help
Run Dapr and (optionally) your application side by side. Supported platforms: Self-hosted

Usage:
  dapr run [flags]

Examples:

# Run a .NET application
dapr run --app-id myapp --app-port 5000 -- dotnet run

# Run a Java application
dapr run --app-id myapp -- java -jar myapp.jar

# Run a NodeJs application that listens to port 3000
dapr run --app-id myapp --app-port 3000 -- node myapp.js

# Run a Python application
dapr run --app-id myapp -- python myapp.py

# Run sidecar only
dapr run --app-id myapp

      --placement-host-address string    The address of the placement service. Format is either <hostname> for default port or <hostname>:<port> for custom port (default "localhost")
      --profile-port int                 The port for the profile server to listen on (default -1)
  -u, --unix-domain-socket string        Path to a unix domain socket dir. If specified, Dapr API servers will use Unix Domain Sockets

Global Flags:
      --log-as-json   Log output in JSON format
```

## STARTUP LOGS

```plainttext
dapr run --app-id hello-dapr --app-port 5000 --dapr-http-port 8089 flask run
Starting Dapr with id hello-dapr. HTTP Port: 8089. gRPC Port: 61672
time="2023-05-07T17:58:53.505176+05:30" level=info msg="starting Dapr Runtime -- version 1.8.3 -- commit 638a1fde84e67b9d2fcdc04f22c74c9c4768be85" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.505176+05:30" level=info msg="log level set to: info" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.505176+05:30" level=info msg="metrics server started on :61673/" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.metrics type=log ver=1.8.3
time="2023-05-07T17:58:53.5096729+05:30" level=info msg="standalone mode configured" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5096729+05:30" level=info msg="app id: hello-dapr" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.510191+05:30" level=info msg="mTLS is disabled. Skipping certificate request and tls validation" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5251635+05:30" level=info msg="local service entry announced: hello-dapr -> 192.168.0.104:61677" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.contrib type=log ver=1.8.3
time="2023-05-07T17:58:53.5251635+05:30" level=info msg="Initialized name resolution to mdns" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.525669+05:30" level=info msg="loading components" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5316686+05:30" level=info msg="component loaded. name: pubsub, type: pubsub.redis/v1" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5318769+05:30" level=info msg="waiting for all outstanding components to be processed" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5364044+05:30" level=info msg="detected actor state store: statestore" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5366944+05:30" level=info msg="component loaded. name: statestore, type: state.redis/v1" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5372027+05:30" level=info msg="all outstanding components processed" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5373874+05:30" level=info msg="gRPC proxy enabled" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5378944+05:30" level=info msg="enabled gRPC tracing middleware" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime.grpc.api type=log ver=1.8.3
time="2023-05-07T17:58:53.5384296+05:30" level=info msg="enabled gRPC metrics middleware" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime.grpc.api type=log ver=1.8.3
time="2023-05-07T17:58:53.5384296+05:30" level=info msg="API gRPC server is running on port 61672" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:53.5389491+05:30" level=info msg="enabled metrics http middleware" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime.http type=log ver=1.8.3
== APP ==    Use a production WSGI server instead.
== APP ==  * Debug mode: off
== APP == WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
== APP ==  * Running on http://127.0.0.1:5000
== APP == Press CTRL+C to quit
time="2023-05-07T17:58:54.4183821+05:30" level=info msg="application discovered on port 5000" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:54.4199156+05:30" level=warning msg="[DEPRECATION NOTICE] Adding a default content type to incoming service invocation requests is deprecated and will be removed in the future. See https://docs.dapr.io/operations/support/support-preview-features/ for more details. You can opt into the new behavior today by setting the configuration option `ServiceInvocation.NoDefaultContentType` to true." app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
== APP == 127.0.0.1 - - [07/May/2023 17:58:54] "GET /dapr/config HTTP/1.1" 404 -
time="2023-05-07T17:58:54.4282271+05:30" level=info msg="application configuration loaded" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:54.429385+05:30" level=info msg="actor runtime started. actor idle timeout: 1h0m0s. actor scan interval: 30s" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime.actor type=log ver=1.8.3
== APP == 127.0.0.1 - - [07/May/2023 17:58:54] "GET /dapr/subscribe HTTP/1.1" 404 -
time="2023-05-07T17:58:54.4395347+05:30" level=info msg="dapr initialized. Status: Running. Init Elapsed 929.8618ms" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime type=log ver=1.8.3
time="2023-05-07T17:58:54.4566707+05:30" level=info msg="placement tables updated, version: 0" app_id=hello-dapr instance=DESKTOP-526RVOF scope=dapr.runtime.actor.internal.placement type=log ver=1.8.3        
```

## TEST

```bash
curl http://localhost:8089/v1.0/invoke/hello-dapr/method/greeting
Hello, World!
```
