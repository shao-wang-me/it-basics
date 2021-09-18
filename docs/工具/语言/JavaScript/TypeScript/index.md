# TypeScript

```shell
# 安装
npm install -g typescript
# 编译（转译）
tsc hello.ts
```

```typescript
interface Book {
  name: string;
  author: Author;
  publisher: Publisher;
}

interface Author {
  firstName: string;
  lastName: string;
}

interface Publisher {
  name: string;
  address: string;
}

type Season = 'spring' | 'summer' | 'autumn' | 'winter'
```
