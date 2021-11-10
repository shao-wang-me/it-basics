# JWT

JSON Web Token

主要是代替 session cookie。Session cookie 需要在服务器端存储该 cookie。而 JWT 将用户数据加密存储在 cookie 中，只要能够正确解密，我们就知道是哪个用户了。

主要的优势是不需要在数据库或者服务器内存中存储 cookie 信息，更适用于大规模分布式系统和和微服务。

## 参考

- 维基百科：<https://en.wikipedia.org/wiki/JSON_Web_Token>
- 官方标准：<https://datatracker.ietf.org/doc/html/rfc7519>
- 很好的解释视频：<https://youtu.be/7Q17ubqLfaM>
- Auth0 做的相关网站：<https://jwt.io/>