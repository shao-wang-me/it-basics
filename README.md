# IT Basics

Basics for an IT student or early career professional.

## Road Map

Aside from the actual content in [`pages/`](pages/), convert them to HTML pages.

### Three steps:

1. Convert all the Markdown files to HTML pages.
2. Add header, footer and sidebar to each file.
3. Generate `index.html` for each folder.

### Possible tools:

Whichever tool is used, the Markdown files in [`pages/`](pages/) shouldn't have to cater for the tool, they must remain in the simplest form.

1. Pandoc

    Convert each Markdown file to a standalone HTML file.

    Pandoc is also able to generate PDFs via Latex, although HTML and PDF generation might use different tools.

    - `--toc/--table-of-contents` generates a table of content.
    - `--template` uses a template.
    - `-H/--include-before-body` includes the content of a file at the end of `<head>`.
    - `-B/--include-before-body` includes the content of a file at the beginning of `<body>`.
    - `-A/--include-after-body` includes the content of a file at the end of `<body>`.
    - `-c/--css`: links to a CSS.

2. ReactDOMServer and a Markdown converter

    [`ReactDOMServer.renderToStaticMarkup()`](https://reactjs.org/docs/react-dom-server.html#rendertostaticmarkup) renders a React element to a static HTML string. It runs in Node.js environment and doesn't any client side scripting.

    Gatsby uses `ReactDOMServer` to generate static HTML as well, except that it uses `ReactDOMServer.renderToString()` at build-time and with `ReactDOM.hydrate()` at client run-time.

---

Naming: [difference - Foundations vs. Fundamentals vs. Basics - English Language Learners Stack Exchange](https://ell.stackexchange.com/q/93696).