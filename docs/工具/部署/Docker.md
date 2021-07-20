# Docker

Docker 可以创建容器，创建的容器可以在几乎任何系统上运行，尤其是可以在现在很火的 Kubernetes 上运行。

## 概念

- 镜像（image）：镜像是构建好的静态的容器模版
- 容器（container）：一个容器是镜像的实例，一个镜像可以有多个容器实例

## 使用 Dockerfile 创建镜像

想要创建镜像，需要用 Dockerfile。

## 创建 Docker Compose

## CLI

```shell
# 运行某镜像，即创建一个该镜像的容器实例
docker run <image> <command>
# 保证交互性，比如 shell
docker run --interactive --tty <image> <command>
# 后台运行
docker --detach <image> <command>

# 查看所有运行的容器，不加 --all 只看在运行的容器
docker ps --all
docker container ls --all
# 查看日志
docker log <container>
# 停止容器
docker stop <container>
# 重启容器
docker restart <container>
# 在容器里执行命令
docker exec <container> <command>
docker exec --interactive --tty <container> /bin/bash

# 拉取镜像
docker pull <image>

# 构建镜像
docker build .
docker build -f Dockerfile .
```
