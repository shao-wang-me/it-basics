# React

1. What is React?

   React is a JavaScript library for building user interfaces. It is:

   1. Declarative: Instead of doing DOM manipulation manually, you declare the result based on the state and React manipulates the DOM for you.
   1. Component-based: Written properly, React components are encapsulated and re-usable.

1. How does React work?

   Conceptually, a React component is like a function. Given a state, it generates a DOM tree (HTML elements).

   ```
   component: state -> dom
   ```

1. Where does React run?

   React typically runs on the client (in the browser). It can also run on a server (Node.js) to generate pages.

1. How does `React` and `ReactDOM` work together?

   Conceptually, `React` "generates" an internal model of the final view, passes it to `ReactDOM` which manipulates the DOM to render the view. They are separated because React is used not only for Web but mobile apps (ReactNative) as well.

   ```js
   function Greetings(props) {
     return 'Hi';
     // or React.createElement(component, props, children)
     // e.g. return React.createElement('div', null, 'Hi');
   }

   const container = document.getElementById('greetings');
   ReactDOM.render(React.createElement(Greetings), container);
   ```

   `React.createElement()` creates a React element and `ReactDOM.render()` renders it.

1. What is `ReactDOMServer`?

   `ReactDOMServer` renders static markups. It is typically used in a Node.js server.

   It doesn't mean that we are losing the power of client-side React. With `ReactDOMServer.renderToString()` or `ReactDOMServer.renderToNodeStream()`, it generates HTML with additional attributes that are used by React internally, so you can use `ReactDOM.hydrate()`
