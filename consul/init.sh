consul agent -dev -client 0.0.0.0 & until consul info; do sleep 1; done && consul kv import @/consul/init_kv.json && tail -f /dev/null