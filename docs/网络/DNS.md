# DNS 域名系统

DNS（Domain Name System），域名系统是一个应用层的系统。它既是一个分布式系统，也可以看作一个协议。

## DNS 记录

[DNS 域名解析中 A、AAAA、CNAME、MX、NS、TXT、SRV、SOA、PTR 各项记录的作用 | IT 笔录](https://itbilu.com/other/relate/EyxzdVl3.html)

比如对 shaowang.me，常用的记录类型有：

| 类型 | 意义 |
| --- | --- |
| A | IPv4 地址 |
| AAAA | IPv6 地址 |
| CNAME | 指向另一个域名，比如说 shao-wang-me.github.io，这样访问 shaowang.me 就和访问后者一样，但是在地址栏还是 shaowang.me |
| MX | 邮箱服务器 |


1. Which transport layer protocol does DNS use?

    DNS uses UDP. A 16-bit identifier is included in each query and copied to the response to match answers to the corresponding query.

2. Is DNS only used in application layer?

3. How are domain names managed?

4. Can one domain name be mapped to multiple IP addresses?

5. How does a domain resource record look like?

    A domain resource record is a five-tuple in the form of `domain_name time_to_live class type value`.

6. What is a zone?

7. What is a root server?

8. What is a authoritative record and a non-authoritative one?

9.  How does a name resolution work in action?

10. How does a reverse lookup work in action?

11. What are recursive query and iterative query?

12. How does DNS caching work?


## Reference

Computer Networks, fifth edition, 9780132553179, by Andrew S. Tanenbaum & David J. Wetherall, 2011
