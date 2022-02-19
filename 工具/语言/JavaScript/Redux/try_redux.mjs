// 这个是 Redux Core，只用最基本的 API
import redux from 'redux';

const {createStore} = redux;

function reducer(state = 0, action) {
  if (action.type === '加') {
    return state + 1;
  } else if (action.type === '减') {
    return state - 1;
  } else {
    return state;
  }
}

const store = createStore(reducer);

store.subscribe(() => console.log(store.getState()));

store.dispatch({type: '加'});
store.dispatch({type: '减'});
store.dispatch({type: '乘'});
