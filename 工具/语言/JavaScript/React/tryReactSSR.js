const React = require('react');
const ReactDOMServer = require('react-dom/server')

function Greetings() {
    return 'Hi';
}

const rendered = ReactDOMServer.renderToString(React.createElement(Greetings));

console.log(rendered);
