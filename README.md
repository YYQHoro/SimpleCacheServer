# Simple Cache Server
Python实现的具有简单内存缓存功能的Web服务器

# Environment
- Python3
- Flask

# Quick Start
```shell
pip3 install flask
python3 simple_cache_server.py --port 5001
```

1. write a dictionary by a key
```shell
curl -d '<value>' localhost:5001/dict/<keyname>
```

2. read a dictionary by a key
```shell
curl localhost:5001/dict/<keyname>
```
