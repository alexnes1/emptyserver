# Empty Server

A web server that accepts all kinds of URLs an arguments and prints gathered info to response and stdout.
Can be used for testing and observing behaviour of various clients.

## Installing

```
pip install -r requirements.txt
```

## Running

Runs on Flask's built-in web server. It is convenient to use start.sh script to start the server.

### start.sh command line arguments

* host
```
-h or --host
```

* port
```
-p or --port
```

* production
```
-pr or --production
```

* certificate
```
-c or --cert
```

* key
```
-k or --key
```

### Examples

```
./start.sh -h localhost -p 8088
```
or

```
./start.sh -h 0.0.0.0 -p 8430 --key=key.pem --cert=cert.pem --production
```