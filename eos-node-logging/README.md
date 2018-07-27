
## eos-node-logging
- [influxdb](https://docs.influxdata.com/influxdb)
- [influxdb-py](http://influxdb-python.readthedocs.io/en/latest/)
- [docker-py](https://docker-py.readthedocs.io/en/stable/)

### Handle incoming block log

- Start Influxdb
```
./influxdb_start.sh
```

- Create database
```
docker exec -it influxdb influx
```
```
create database eos_mainnet
```

- Run eos log handler
```
docker ps |grep nodeos |awk '{print $1}'

python eos_log_handler.py --id
```

### Features in the work
- handle error log to [Sentry](https://github.com/getsentry/sentry)