# HTTP

HyperText Transfer Protocol，超文本传输协议，是一个应用层协议。要求传输层协议是可靠的，但不一定是有连接的，通常使用 TCP。HTTP 本身是无状态的，但是可以有 cookie 控制的 session。

## Request / Response 格式

```http
GET https://example.com HTTP/1.1
Host: example.com

This is body.
```

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

缓存可以存在于请求发起到请求处理中间的任何环节：浏览器、本地电脑、ISP、负载均衡等。

相关 heaer：`Cache-Control``Expires` TODO

### `revving`

为了解决缓存过期时间长和需要不定期更新的矛盾，把每个资源都加上一个版本号或者一个 hash，而在 `index.html` 这种缓存过期时间短或者不允许缓存的页面中指向这些资源。对于 CSS 和 JavaScript 文件，这样还能消灭依赖问题。

[Caching Headers - Supercharged - YouTube](https://www.youtube.com/watch?v=aN8wMQVaNvs)

## Cookie

服务器设置 `Set-Cookie`，则浏览器会保存该 cookie，后续所有向该 domain 的请求都会通过 `Cookie` 发送所有 cookie。

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