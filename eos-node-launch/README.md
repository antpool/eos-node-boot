## eos-node-launch

- [EOS-Mainnet](https://github.com/EOS-Mainnet/eos/tree/master/Docker)

### Build eos image

```
docker build -t ap/eosmainnet:latest --build-arg branch=mainnet-1.0.10 --build-arg symbol=EOS ./
```

---

### Init

```
./init.sh
```

copy backup block data to DATA_DIR, eg:
```
wget http://osshkbk01.oss-cn-hongkong.aliyuncs.com/eosarch/eosmainnet/docker-20180717.tar.bz2
tar -jxvf docker-20180717.tar.bz2
mv docker-20180717/* $DATA_DIR
```

---

### Start

```
./start.sh
```

get chain info

```
./cleos.sh get info
```
or
```
curl http://127.0.0.1:8888/v1/chain/get_info
```

### Restart

```
docker-compose down
docker-compose up -d
```

### Ship log with Fluentd

- [Launch Fluentd container](fluentd-container)
- start with the fluentd logging driver:

```
docker-compose -f docker-compose-fluentd.yml up -d
```

### Features in the work
- using [kubernetes](https://github.com/kubernetes/kubernetes) schedule and manage Node container


