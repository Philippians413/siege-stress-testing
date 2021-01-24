### Installation

1. Start postgres container
```
$ docker run -d \
  --name postgres \
  --net postgres \
  --user "$(id -u):$(id -g)" \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=password \
  -v ${PWD}/postgres/:/var/lib/postgresql/data \
  postgres
```

2. Install requirements

```$ pip install -r requirements.txt```

3. Run application

```$ python3 application.py```

4. Run siege tests
### Results:

```
$ siege -c10 -t2m 127.0.0.1:5000/api/v1/resources/clubs/epl
** SIEGE 4.0.4
** Preparing 10 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        3191 hits
Availability:		      100.00 %
Elapsed time:		        9.66 secs
Data transferred:	       11.95 MB
Response time:		        0.03 secs
Transaction rate:	      330.33 trans/sec
Throughput:		        1.24 MB/sec
Concurrency:		        9.96
Successful transactions:        3191
Failed transactions:	           0
Longest transaction:	        0.06
Shortest transaction:	        0.01

$ siege -c25 -t2m 127.0.0.1:5000/api/v1/resources/clubs/epl
** SIEGE 4.0.4
** Preparing 25 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        2411 hits
Availability:		      100.00 %
Elapsed time:		        7.24 secs
Data transferred:	        9.03 MB
Response time:		        0.07 secs
Transaction rate:	      333.01 trans/sec
Throughput:		        1.25 MB/sec
Concurrency:		       24.88
Successful transactions:        2411
Failed transactions:	           0
Longest transaction:	        0.12
Shortest transaction:	        0.02
 
$ siege -c50 -t2m 127.0.0.1:5000/api/v1/resources/clubs/epl
** SIEGE 4.0.4
** Preparing 50 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        2979 hits
Availability:		      100.00 %
Elapsed time:		        9.25 secs
Data transferred:	       11.16 MB
Response time:		        0.15 secs
Transaction rate:	      322.05 trans/sec
Throughput:		        1.21 MB/sec
Concurrency:		       49.44
Successful transactions:        2979
Failed transactions:	           0
Longest transaction:	        0.23
Shortest transaction:	        0.03
 
$ siege -c100 -t2m 127.0.0.1:5000/api/v1/resources/clubs/epl
** SIEGE 4.0.4
** Preparing 100 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        3568 hits
Availability:		      100.00 %
Elapsed time:		       10.66 secs
Data transferred:	       13.37 MB
Response time:		        0.29 secs
Transaction rate:	      334.71 trans/sec
Throughput:		        1.25 MB/sec
Concurrency:		       98.37
Successful transactions:        3568
Failed transactions:	           0
Longest transaction:	        0.34
Shortest transaction:	        0.03
 
$ siege -c200 -t2m 127.0.0.1:5000/api/v1/resources/clubs/epl
** SIEGE 4.0.4
** Preparing 200 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		        3602 hits
Availability:		      100.00 %
Elapsed time:		       10.74 secs
Data transferred:	       13.49 MB
Response time:		        0.46 secs
Transaction rate:	      335.38 trans/sec
Throughput:		        1.26 MB/sec
Concurrency:		      154.70
Successful transactions:        3602
Failed transactions:	           0
Longest transaction:	        8.08
Shortest transaction:	        0.02

$ siege -c250 -t2m 127.0.0.1:5000/api/v1/resources/clubs/epl
** SIEGE 4.0.4
** Preparing 250 concurrent users for battle.
The server is now under siege...^C
Lifting the server siege...
Transactions:		       10994 hits
Availability:		      100.00 %
Elapsed time:		       33.26 secs
Data transferred:	       41.18 MB
Response time:		        0.60 secs
Transaction rate:	      330.55 trans/sec
Throughput:		        1.24 MB/sec
Concurrency:		      199.10
Successful transactions:       10994
Failed transactions:	           0
Longest transaction:	       27.76
Shortest transaction:	        0.10
```
