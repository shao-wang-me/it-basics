# JWT

JSON Web Token

主要是代替 session cookie。Session cookie 需要在服务器端存储这个 cookie。而 JWT 将用户数据加密存储在 cookie 种，只要能够正确解密，我们就知道是哪个用户了。

主要的优势是不需要在数据库或者服务器内存中存储 cookie 信息，更适用大规模于分布式系统和和微服务。

很好的解释视频：<https://youtu.be/7Q17ubqLfaM>