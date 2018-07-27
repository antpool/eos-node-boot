#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import argparse

import docker
docker_client = docker.from_env()

from influxdb import InfluxDBClient
influxdb_client = InfluxDBClient('localhost', 8086, 'root', 'root', 'eos_mainnet')

timestamp_pattern = '\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}'
line_pattern = '^\d{4}-\d{2}-\d{2}'

def handle_log():
    container = docker_client.containers.get(container_id)
    pre_line = ""
    for line in container.logs(stream=True):
        line = line.rstrip('\n')
        pre_line = handle_line(pre_line, line)

def handle_line(pre_line, line):
    try:
        log = pre_line + line
        if not re.match(line_pattern, line):
            return log
        if pre_line == "":
            return line
        log = pre_line
        log_dict = extract_log(log)
        if log_dict['method'] == 'on_incoming_block':
            msg_dict = extract_incoming_block(log_dict['message'])
            if msg_dict == None:
                return line
            handle_incoming_block(msg_dict)
        # TODO handle error log
    except Exception as e:
        print(str(e))
    return line


def extract_log(log):
    #"2018-07-25T08:43:35.167 thread-0   producer_plugin.cpp:327       on_incoming_block    ] Received block 7e8ab6e087df5242... #7672330 @ 2018-07-25T08:43:35.000 signed by eos42freedom [trxs: 1, lib: 7672005, conf: 0, latency: 167 ms]"
    pattern = '(?P<timestamp>{})\s+(?P<thread_name>thread-\d+)\s+(?P<file>.+):(?P<line>\d+)\s+(?P<method>\w+).*\]\s+(?P<message>.*)'.format(timestamp_pattern)
    return extract_dict(pattern, log)

def extract_incoming_block(message):
    # Received block 7e8ab6e087df5242... #7672330 @ 2018-07-25T08:43:35.000 signed by eos42freedom [trxs: 1, lib: 7672005, conf: 0, latency: 167 ms]
    pattern = '.*?#(?P<block_header_num>\d+)\s+@\s+(?P<timestamp>{})\s+?signed by\s+?(?P<producer_name>.+?)\s.*' \
              '\[trxs: (?P<trx_count>\d+), lib: (?P<last_irreversible_block_num>\d+), conf: (?P<confirm_count>\d+), latency: (?P<latency>.*) ms\]'.format(timestamp_pattern)
    if not re.match(pattern, message):
        # TODO errorLog report
        return
    return extract_dict(pattern, message)

def extract_dict(pattern, text):
    if text == '':
        return
    res = re.search(pattern, text)
    return res.groupdict()

def handle_incoming_block(msg_dict):
    measurement = 'incoming_block'
    tags = {"block_header_num": msg_dict['block_header_num'], "producer_name": msg_dict['producer_name'], "last_irreversible_block_num": msg_dict['last_irreversible_block_num']}
    fields = {"trx_count": msg_dict['trx_count'], "confirm_count": msg_dict['confirm_count'], "latency": msg_dict['latency']}
    time = msg_dict['timestamp']
    points = [{"measurement": measurement, "tags": tags, "time": time, "fields": fields}]
    influxdb_client.write_points(points)

def main():
    handle_log()

def usage():
    global container_id
    parser = argparse.ArgumentParser(description='EOS Mainnet Node Log Handler')
    parser.add_argument('-id', '--container_id', required=True, help='eos container id')
    args = parser.parse_args()
    container_id = args.container_id

if __name__ == '__main__':
    usage()
    main()