#!/bin/bash

docker build -t ap/fluentd:latest .

docker run --name fluentd --rm -it -p 24224:24224 -v $PWD/fluentd.conf:/fluentd/etc/fluentd.conf -v /data/fluent/logs:/fluentd/log -e FLUENTD_CONF=fluentd.conf ap/fluentd:latest