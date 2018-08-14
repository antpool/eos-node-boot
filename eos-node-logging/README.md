
## eos-node-logging
- [elk-stack](https://www.elastic.co/elk-stack)
- [influxdb](https://docs.influxdata.com/influxdb)

### Handle log with Elastic Stack
- [getting started with the Elastic Stack](https://www.elastic.co/guide/en/elastic-stack-overview/6.3/get-started-elastic-stack.html#get-started-elastic-stack)
- [logstash config](logstash)

### Handle incoming block log
- [launch Influxdb container](influxdb-container)
- run eos log handler
```
python eos_log_handler.py -id $(docker ps |grep nodeos |awk '{print $1}')
```


### Features in the work
- handle error log to [Sentry](https://github.com/getsentry/sentry)

### Config & Resource
- [logstash reference](https://www.elastic.co/guide/en/logstash/6.3/index.html)
- [influxdb-py](http://influxdb-python.readthedocs.io/en/latest/)
- [docker-py](https://docker-py.readthedocs.io/en/stable/)
