#!/bin/bash

CONFIG_DIR=/opt/eos-mainnet/config
DATA_DIR=/opt/eos-mainnet/data

mkdir -p $CONFIG_DIR
mkdir -p $DATA_DIR

cp -r config/* $CONFIG_DIR

# wget http://osshkbk01.oss-cn-hongkong.aliyuncs.com/eosarch/eosmainnet/docker-20180717.tar.bz2
# tar -jxvf docker-20180717.tar.bz2
# mv docker-20180717/* $DATA_DIR

