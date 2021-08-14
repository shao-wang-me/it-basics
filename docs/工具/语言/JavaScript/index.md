# 基础

[JavaScript 指南 | MDN (mozilla.org)](https://developer.mozilla.org/zh-CN/docs/orphaned/Web/JavaScript/Guide)

## 需要学习

> 1. 闭包
>     1. 全局
>     1. 作用域
> 1. 异步
>     1. `setTimeOut`、`setInterval`
>     1. AJAX
>     1. `Promise`
>     1. `async`、`await`
>     1. 异步机制
> 1. 线程机制
> 1. TypeScript


## 作用域

### 变量

新的 JavaScript 中不建议用 `var` 了，暂不表，只说 `let` 和 `const`。

`let` 和 `const` 都是提供局部作用域，比方说：

```javascript
if (true) {
  let x = 1;
}
console.log(x);  // 会出错因为 x 是局部的，只在上面的 if 中有用
```

### 函数

只有这样定义的函数才会有函数提升：

```javascript
f()  // 可以执行因为有变量提升

function f () {
  console.log('Hi')
}
```

## 异常处理

```javascript
try {
  console.log('try');
  throw 'error';
} catch (e) {
  console.log('catch', e);
} finally {
  console.log('finally');
}
```

输出：

```text
try
catch error
finally
```

```javascript
throw 'error';
throw Error('Error');  // 直接 Error 是没有问题的
throw new Error('Error');  // 有没有 new 都是一样的
throw Error;  // 这个不行，括号还是要有的，但是语法上没问题，理论上可以 throw 任何东西
throw {firstName: 'Shao', lastName: 'Wang'};  // 对象也行
throw 12;

try {
  throw 'Error';
} catch (e) {
  typeof e;  // 'string'
  e instanceof Error;  // false
}

try {
   throw Error('Error');
} catch (e) {
   typeof e;  // 'object'
   e instanceof Error;  // true
}
```
