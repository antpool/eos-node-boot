
## eos-node-monitoring
- reference: [vegasbrianc/prometheus](https://github.com/vegasbrianc/prometheus)
- stack: [Prometheus](https://prometheus.io/) & [Grafana](https://grafana.com/) & [cAdvisor](https://github.com/google/cadvisor) & [Node_Exporter](https://github.com/prometheus/node_exporter)
- cAdvisor to gather containers metrics
- Node_Exporter to gather machine(host) metrics

### Quickstart
```
docker-compose up -d
```
```
docker-compose down
```

### Features in the work
- using [kubernetes](https://github.com/kubernetes/kubernetes) schedule and manage Monitoring container

### Config & Resource
- [grafana support for prometheus](https://prometheus.io/docs/visualization/grafana/)
- [grafana provisioning](http://docs.grafana.org/administration/provisioning/)
- [prometheus alerting](https://prometheus.io/docs/alerting/overview/)