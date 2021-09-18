# React

React 是 Facebook 开发的用于构建 UI 的 JavaScript 包。

## 特点

- 声明式的：直接声明需要的结果，React 会处理 DOM
- 基于组件的：封装、复用

## 运行位置和时间

通常在客户端（浏览器）运行，动态生成页面，也可以在服务器端（Node.js）生成页面，还可以在编译时用于生成静态（服务器端静态）页面。

## `React`、`ReactDOM` 和 `ReactDOMServer`

Facebook 想将 React 同时用于网站和移动应用开发，所以有 React 和 ReactDOM，React 用于声明组件，ReactDOM 实际操作网页 DOM。`ReactDOMServer` 用于在服务器端渲染页面。

```js
function Greetings(props) {
  return 'Hi';
  // 或 React.createElement(component, props, children)
  // 例如 return React.createElement('div', null, 'Hi');
}

const container = document.getElementById('greetings');
ReactDOM.render(React.createElement(Greetings), container);
```
