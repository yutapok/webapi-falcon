# webapi-falcon
Simple web api

* run falcon
```
   gunicorn -b 0.0.0.0:8000 swooping:app

```

* request
```
   e.x)
   $ curl http://example.com:8000/hook.pokkun.rss-update -X POST -d '{"text" : "tweet:urls"}'
   $ {"tw_status": 200}
   ---> tweet somthing thorough twitter developers api

```
