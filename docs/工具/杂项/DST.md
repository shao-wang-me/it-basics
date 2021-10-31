# DST

~~Don't~~ Starve Together

```lua
-- 玩家列表
c_listallplayers()

-- Host 自己是 1 号，第二个玩家是 2 号
c_select(AllPlayers[2])  -- 选中第二个玩家
c_supergodmode()  -- 此时第二个玩家会变成超级无敌模式
c_maintainall()  -- 不是超级无敌模式，即会受伤，但是会持续回血


-- 移除鼠标下的物品
ConsoleWorldEntityUnderMouse():Remove()
-- 或者
c_select():Remove()
```

| 物品 | 代码 |
| --- | --- |
| 木头 | log |
| 树枝 |
| 草 |
| 金块 |