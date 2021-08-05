# IP 信息查询

- flask api, 集成了swagger ui
- 依赖 /data/ipip.ipdb 数据库，在项目根目录创建data文件夹，自行获取ipip.ipdb 数据库

## 本地启动
- python3 debug.py

## docker 启动

```sh
docker build . -t ipip-local-web;
docker run --rm -p 9090:8000 ipip-local-web;
```


