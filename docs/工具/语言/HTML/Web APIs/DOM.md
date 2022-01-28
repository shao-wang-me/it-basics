# DOM

## 窗口、文档加载事件监听器

1. `window.load`：全部加载完成
2. `window.DOMContentLoaded`：DOM 加载完成，其他资源（图片、JS、CSS）尚未完成
3. `document.DOMContentLoaded`：同上，但 `event.target` 是 `document`
4. `document.readystatechange`：当 `document.readyState` 改变时
   `document.readyState` 有三个可能的值：`loading`、interactive`（类似上述 `DOMContentLoaded`）、`complete`