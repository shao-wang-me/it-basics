# HTTP

HyperText Transfer Protocol，超文本传输协议，是一个应用层协议。要求传输层协议是可靠的，但不一定是有连接的，通常使用 TCP。HTTP 本身是无状态的，但是可以有 cookie 控制的 session。

## HTTP 方法（Method）

| Method | 描述 |
| --- | --- |
| GET | 获取资源 |
| HEAD | 只获取 response 的 header |
| POST | 发送信息 |
| PUT | 替换资源 |
| DELETE | 删除资源 |
| TRACE | 让服务器 echo 发送的 request |
| CONNECT | 通过一个代理服务器连接 |
| OPTIONS | 询问可用的方法 |

## 缓存

## Authentication

`WWW-Authenticate` 及类似的 header，或者用 cookies 实现。

## Origin control



1. What is the difference between PUT and POST?

1. What is the structure of a HTTP message?

1. How does HTTP connect to the destination machine?

1. Who and what specifies HTTP?

1. What is HTTPS?

1. How does the performance of HTTPS compare to HTTP?

1. How does the performance of HTTP compare to TCP?

1. When I visit a website, why can I see TCP message (segment) in Wireshark?

    Because HTTP normally uses TCP as the transport layer protocol. The HTTP client needs to establish the TCP connection first.

1. What happens when I visit a web page in the browser?

1. What is HTTP 1.1, HTTP2 and HTTP3?