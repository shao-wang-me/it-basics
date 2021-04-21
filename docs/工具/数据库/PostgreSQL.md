# PostgreSQL

1. 自增列有哪些实现办法？

   <https://www.cnblogs.com/wy123/p/13367486.html>

   - sequence
   - identity
   - serial

## 序列 Sequence

文档：<https://www.postgresql.org/docs/current/sql-createsequence.html>

自增序列，默认从1开始，递增1。基于bigint，八字节整数，从9223372036854775808到9223372036854775807。

```postgresql
create sequence id;
-- 这个last_value是上一个被指派的值
-- 特殊的一点是序列刚创建还没有nextval()过的，last_value是1
select last_value from id;
-- 序列前进到下一个值，并返回该值
-- 注意用单引号括起来序列名字
select nextval('id');
-- 当前session的当前值和上一个值
select currval('id');
select lastval('id');
insert into book values (nextval('id'), '史记');
-- 序列和实际表格内容不匹配的话，手动更新序列
select setval('id', max(id)) FROM book;
```
