# webpack

静态模块打包器（static module bundler）

## 概念

webpack 把 JavaScript、JSON、CSS、图片等文件都视为模块。

1. Entry：打包入口文件
1. Output：输出文件
1. Loader：webpack 默认支持 JavaScript 和 JSON 文件，需要添加额外的 loader 来支持其它文件
1. Plugin：更多功能
1. Mode：development、production 或 none