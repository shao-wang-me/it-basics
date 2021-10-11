# React Router

!!! info "注意"
    建议新项目使用 @reach/router，详见 [React Router 作者公告](https://reacttraining.com/blog/reach-react-router-future/)。

```javascript
import React from "react";
import {BrowserRouter as Router, Switch, Route, Link, useRouteMatch, useParams} from "react-router-dom";

function App() {
  return (
      <Router>
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/users">Users</Link>

        <Switch>
          <Route path="/about">About</Route>
          <Route path="/users">
            <Users/>
          </Route>
          <Route path="/">Home</Route>
        </Switch>
      </Router>
  );
}

function Users() {
  // Route 匹配信息
  const match = useRouteMatch();
  return (
      <>
        <Link to={`${match.url}/components`}>Components</Link>
        <Link to={`${match.url}/props-v-state`}>Props v. State</Link>

        <Switch>
          <Route path={`${match.path}/:userId`}>
            <User/>
          </Route>
          <Route path={match.path}>All users: ...</Route>
        </Switch>
      </>
  );
}

function User() {
  let {userId} = useParams();
  return <>User ID: {userId}</>;
}
```

把所有的内容包在 `<Router>` 里，`<Link>` 就当 `<a>` 用。区别在 `<Switch>`，它会渲染当中第一个符合条件的 `<Route>`。
