import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import store from './redux/store'


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
)

// 检测redux中状态改变，如果redux的状态发生改变，那么重新渲染App组件
store.subscribe(() => {
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
)
})