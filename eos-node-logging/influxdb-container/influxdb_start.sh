#!/bin/bash

docker run --name influxdb --rm -it -p 8086:8086 \
      -v $PWD/influxdb.conf:/etc/influxdb/influxdb.conf:ro \
      -v /data/influxdb:/var/lib/influxdb \
      influxdb -config /etc/influxdb/influxdb.conf